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


def validate_inputs(work_item: str, language: str, variant: str) -> None:
    # Accept WI + 8 digits (e.g. WI00123456, WI01002345)
    if not re.fullmatch(r"WI\d{8}", work_item):
        print("❌ WorkItemsNumber must look like WI######## (e.g., WI00123456 or WI01002345)")
        sys.exit(1)

    # language is typically like EN-EN, EN-US etc. (we don't hard-validate further here)
    if not language:
        print("❌ Language code could not be parsed.")
        sys.exit(1)

    if not len(variant) < 2:
        print("❌ Languave Variant should be blank or a single character")
        sys.exit(1)


def candidate_rel_path(work_item: str, letter: str, language: str) -> str:
    return f"{work_item}-{letter}/{work_item}-{letter}-{language}"


def path_exists_on_branch_or_main(
    work_item: str, letter: str, language: str, product: str, create_root: Path, scan_root: Path
) -> bool:
    rel = candidate_rel_path(work_item, letter, language)
    create_product_root = create_root / product
    scan_product_root = scan_root / product
    return (create_product_root / rel).exists() or (scan_product_root / rel).exists()


def get_next_folder_union(work_item: str, language: str, product: str, create_root: Path, scan_root: Path) -> Path:
    """
    Current process: pick NEXT available letter A–Z.
    A letter is considered 'taken' if it exists on EITHER:
      - target branch workspace (create_root)
      - origin/main worktree (scan_root)
    Returns the CREATE path in create_root.
    """
    create_product_root = create_root / product

    for letter in ascii_uppercase:
        if not path_exists_on_branch_or_main(work_item, letter, language, product, create_root, scan_root):
            rel = candidate_rel_path(work_item, letter, language)
            return create_product_root / rel

    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")

def get_folder_with_optional_variant(
    work_item: str,
    language: str,
    product: str,
    create_root: Path,
    scan_root: Path,
    variant: str | None,
) -> Path:
    """
    Desired behavior:
    - If variant is blank/None => current process (next available letter)
    - If variant is provided AND that exact variant folder exists (branch OR main) for this language => EXIT
    - If variant is provided AND free => use it
    """
    if variant is None:
        variant = ""
    variant = variant.strip().upper()

    # Blank -> current process
    if variant == "":
        return get_next_folder_union(work_item, language, product, create_root, scan_root)

    # Validate variant: must be single A–Z
    if len(variant) != 1 or variant not in ascii_uppercase:
        print("❌ LanguageVariant must be a single letter A–Z (or left blank).")
        sys.exit(1)

    rel = candidate_rel_path(work_item, variant, language)

    # If it already exists on either branch or main -> STOP
    if path_exists_on_branch_or_main(work_item, variant, language, product, create_root, scan_root):
        print(
            f"❌ Variant already exists for this language: {(create_root / product) / rel} "
            f"(or in {scan_root / product / rel}). Aborting."
        )
        sys.exit(1)

    # Otherwise safe to use requested variant
    return (create_root / product) / rel



def parse_language_choice(raw: str) -> str:
    """
    Inputs look like: "English GB (EN-GB)" or "English (EN-EN)".
    Extract what's in parentheses. If no parentheses, use raw as-is.
    """
    s = (raw or "").strip()
    if "(" in s and ")" in s and s.rfind(")") > s.find("("):
        return s[s.find("(") + 1 : s.rfind(")")].strip().upper()
    return s.upper()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--folder_to_organize", required=True)   # e.g. new
    p.add_argument("--work_item", required=True)           # e.g. WI01002345
    p.add_argument("--language", required=True)            # e.g. "English (EN-EN)" or "EN-EN"
    p.add_argument("--product", required=True)             # e.g. CargoWise
    p.add_argument("--scan_root", default="_main")         # worktree path for origin/main
    p.add_argument("--variant", default="")       # e.g. A (optional)
    args = p.parse_args()

    folder_to_organize = args.folder_to_organize
    work_item = args.work_item.strip().upper()

    language = parse_language_choice(args.language)
    product = args.product.strip()
    variant = args.variant

    validate_inputs(work_item, language, variant)

    create_root = Path(".")
    scan_root = Path(args.scan_root)

    # Source folder must exist in the CURRENT workspace (target branch workspace)
    source_folder = create_root / product / folder_to_organize
    if not source_folder.exists():
        print(f"❌ Source folder not found: {source_folder}")
        sys.exit(1)

    # Decide target folder path (variant-aware)
    folder_path = get_folder_with_optional_variant(
        work_item=work_item,
        language=language,
        product=product,
        create_root=create_root,
        scan_root=scan_root,
        variant=variant,
    )

    # Create target folder and _images
    folder_path.mkdir(parents=True, exist_ok=True)
    image_folder = folder_path / "_images"
    image_folder.mkdir(parents=True, exist_ok=True)

    # Collect images (deterministic ordering)
    all_images: list[Path] = []
    for pattern in IMAGE_EXTS:
        all_images.extend(source_folder.glob(pattern))
    all_images = sorted(all_images, key=lambda p: p.name.lower())

    rename_map: dict[str, str] = {}  # "old.png" -> "<folder_path.name>.1.png"
    for i, img_file in enumerate(all_images, start=1):
        new_img_name = f"{folder_path.name}.{i}{img_file.suffix.lower()}"
        rename_map[img_file.name] = new_img_name
        shutil.copy2(img_file, image_folder / new_img_name)
        print(f"Copied image: {img_file.name} → {new_img_name}")

    # If no images, keep folder trackable in git
    if not all_images:
        (image_folder / ".gitkeep").write_text("", encoding="utf-8")

    # Rewrite markdown image references
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

            # Output markdown name matches folder_path.name
            dest_md = folder_path / f"{folder_path.name}.md"
            dest_md.write_text(new_text, encoding="utf-8")

    print(f"✅ Done. Output folder: {folder_path}")


if __name__ == "__main__":
    main()
