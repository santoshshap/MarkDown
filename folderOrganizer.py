import sys
import shutil
from pathlib import Path
from string import ascii_uppercase
import re
import argparse
from urllib.parse import urlsplit


IMAGE_EXTS = ["*.jpg", "*.jpeg", "*.png", "*.svg", "*.tiff", "*.gif", "*.bmp", "*.webp"]


def basename_from_src(src: str) -> str:
    src = src.strip()
    path = urlsplit(src).path  # strips ?query/#fragment
    return Path(path).name

def validate_inputs(work_item: str, language: str) -> None:
    if not work_item.startswith("WI00") or len(work_item) != 10 or not work_item[-8:].isdigit():
        print("❌ WorkItemsNumber must look like WI00######## (10 chars)")
        sys.exit(1)
    if len(language) != 2 or not language.isalpha():
        print("❌ LanguageCode must be 2 letters")
        sys.exit(1)

def candidate_rel_path(work_item: str, letter: str, language: str) -> str:
    return f"{work_item}-{letter}/{work_item}-{letter}-{language}-{language}"


def get_next_folder_union(work_item: str, language: str, product: str, create_root: Path, scan_root: Path) -> Path:
    """
    Match original behavior: create NEXT available letter folder.
    But treat a letter as 'taken' if it exists on EITHER:
      - target branch workspace (create_root)
      - origin/main worktree (scan_root)
    Returns the CREATE path in create_root.
    """
    create_product_root = create_root / product
    scan_product_root = scan_root / product

    for letter in ascii_uppercase:
        rel = candidate_rel_path(work_item, letter, language)

        exists_on_branch = (create_product_root / rel).exists()
        exists_on_main = (scan_product_root / rel).exists()

        if (not exists_on_branch) and (not exists_on_main):
            return create_product_root / rel

    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--folder_to_organize", required=True)  # e.g. new
    p.add_argument("--work_item", required=True)          # e.g. WI00001111
    p.add_argument("--language", required=True)           # e.g. EN
    p.add_argument("--product", required=True)            # e.g. CargoWise
    p.add_argument("--scan_root", default="_main")        # worktree path for origin/main
    args = p.parse_args()

    folder_to_organize = args.folder_to_organize
    work_item = args.work_item.upper()
    language = args.language.upper()
    product = args.product

    validate_inputs(work_item, language)

    create_root = Path(".")
    scan_root = Path(args.scan_root)

    # Source folder must exist in the CURRENT workspace (same as original intent)
    source_folder = create_root / product / folder_to_organize
    if not source_folder.exists():
        print(f"❌ Source folder not found: {source_folder}")
        sys.exit(1)

    # Pick next available letter based on branch + main
    folder_path = get_next_folder_union(work_item, language, product, create_root, scan_root)

    # Create target folder and _images
    folder_path.mkdir(parents=True, exist_ok=True)
    image_folder = folder_path / "_images"
    image_folder.mkdir(parents=True, exist_ok=True)

    # Collect images (deterministic ordering)
    all_images = []
    for pattern in IMAGE_EXTS:
        all_images.extend(source_folder.glob(pattern))
    all_images = sorted(all_images, key=lambda p: p.name.lower())

    rename_map = {}  # "old.png" -> "<folder_path.name>.1.png"
    for i, img_file in enumerate(all_images, start=1):
        new_img_name = f"{folder_path.name}.{i}{img_file.suffix.lower()}"
        rename_map[img_file.name] = new_img_name
        shutil.copy2(img_file, image_folder / new_img_name)
        print(f"Copied image: {img_file.name} → {new_img_name}")

    # If no images, keep folder trackable in git
    if not all_images:
        (image_folder / ".gitkeep").write_text("", encoding="utf-8")

    # Rewrite markdown
    img_md_pattern = re.compile(r"!\[(?P<alt>.*?)\]\((?P<path>[^)]+)\)")

    md_files = list(source_folder.glob("*.md"))
    if not md_files:
        print(f"⚠️ No .md files found in: {source_folder}")
    else:
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")

            def replace_md_image(match: re.Match) -> str:
                alt = match.group("alt")
                orig_path = match.group("path").strip()
                old_name = basename_from_src(orig_path)
                new_name = rename_map.get(old_name, old_name)  # fallback if not found
                return f"![{alt}](_images/{new_name})"

            new_text = img_md_pattern.sub(replace_md_image, text)

            # Handle HTML <img src="...">
            def replace_html_img(m: re.Match) -> str:
                old_name = basename_from_src(m.group(2))
                new_name = rename_map.get(old_name, old_name)
                return m.group(1) + f"_images/{new_name}" + m.group(3)

            new_text = re.sub(
                r'(<img\s+[^>]*src=["\'])([^"\']+)(["\'])',
                replace_html_img,
                new_text,
            )

            dest_md = folder_path / f"{folder_path.name}.md"
            dest_md.write_text(new_text, encoding="utf-8")

    print(f"✅ Done. Output folder: {folder_path}")


if __name__ == "__main__":
    main()
