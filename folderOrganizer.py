import sys
import shutil
from pathlib import Path
from string import ascii_uppercase
import re
import argparse
from urllib.parse import urlsplit

def folder_exists(folder_path: Path) -> bool:
    return folder_path.is_dir()

def get_next_folder(work_item: str, language: str, root_dir: Path) -> Path:
    for letter in ascii_uppercase:  # 'A' .. 'Z'
        candidate = root_dir / f"{work_item}-{letter}/{work_item}-{letter}-{language}-{language}"
        if not candidate.exists():
            return candidate
    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")

def basename_from_src(src: str) -> str:
    src = src.strip()
    path = urlsplit(src).path  # strips ?query/#fragment
    return Path(path).name

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--folder_to_organize", required=True)  # e.g. new
    p.add_argument("--work_item", required=True)          # e.g. WI00001111
    p.add_argument("--language", required=True)           # e.g. EN
    p.add_argument("--product", required=True)            # e.g. CargoWise
    args = p.parse_args()

    FolderToOrganize = args.folder_to_organize
    WorkItemsNumber = args.work_item.upper()
    LanguageCode = args.language.upper()
    product = args.product

    # Validation (kept close to your original)
    if not WorkItemsNumber.startswith("WI0000"):
        print("WorkItemsNumber must start with WI0000")
        sys.exit(1)
    if len(WorkItemsNumber) != 10:
        print("WorkItemsNumber must be 10 characters")
        sys.exit(1)
    if len(LanguageCode) != 2 or (not LanguageCode.isalpha()):
        print("LanguageCode must be 2 letters")
        sys.exit(1)

    root = Path(product)
    baseFolder = root / f"{WorkItemsNumber}-A"

    # Non-interactive behavior:
    # - always create next available letter folder
    folder_path = get_next_folder(WorkItemsNumber, LanguageCode, root)

    folder_path.mkdir(parents=True, exist_ok=True)

    source_folder = Path(f"{product}/{FolderToOrganize}")
    if not source_folder.exists():
        print(f"Source folder not found: {source_folder}")
        sys.exit(1)

    # Create _images
    image_folder = folder_path / "_images"
    image_folder.mkdir(parents=True, exist_ok=True)

    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.svg", "*.tiff", "*.gif", "*.bmp", "*.webp"]

    # Collect + sort images (deterministic order)
    all_images = []
    for pattern in image_extensions:
        all_images.extend(source_folder.glob(pattern))
    all_images = sorted(all_images, key=lambda p: p.name.lower())

    rename_map = {}  # old_name -> "<folder_path.name>.<i>.ext"
    for i, img_file in enumerate(all_images, start=1):
        new_img_name = f"{folder_path.name}.{i}{img_file.suffix.lower()}"
        rename_map[img_file.name] = new_img_name
        shutil.copy2(img_file, image_folder / new_img_name)
        print(f"Copied image: {img_file.name} → {new_img_name}")

    # Update markdown files
    img_md_pattern = re.compile(r"!\[(?P<alt>.*?)\]\((?P<path>[^)]+)\)")

    for md_file in source_folder.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")

        def replace_md_image(match: re.Match) -> str:
            alt = match.group("alt")
            orig_path = match.group("path").strip()
            old_name = basename_from_src(orig_path)
            new_name = rename_map.get(old_name, old_name)
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

    print(f"Done. Output folder: {folder_path}")

if __name__ == "__main__":
    main()
