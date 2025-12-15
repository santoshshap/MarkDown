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
    if not work_item.startswith("WI0000"):
        print("❌ WorkItemsNumber must start with WI0000")
        sys.exit(1)
    if len(work_item) != 10:
        print("❌ WorkItemsNumber must be 10 characters")
        sys.exit(1)
    if len(language) != 2 or not language.isalpha():
        print("❌ LanguageCode must be 2 letters")
        sys.exit(1)


def candidate_rel_path(work_item: str, letter: str, language: str) -> str:
    # WI00001111-A/WI00001111-A-EN-EN
    return f"{work_item}-{letter}/{work_item}-{letter}-{language}-{language}"


def find_existing_letters(work_item: str, language: str, product: str, repo_root: Path) -> list[str]:
    """Return list of letters that exist in this repo_root (branch or _main)."""
    product_root = repo_root / product
    found = []
    for letter in ascii_uppercase:
        rel = candidate_rel_path(work_item, letter, language)
        if (product_root / rel).exists():
            found.append(letter)
    return found


def ensure_folder_on_branch(
    work_item: str,
    language: str,
    product: str,
    letter: str,
    create_root: Path,
    scan_root: Path,
) -> Path:
    """
    Ensures the target WI folder exists on the branch workspace.
    - If it exists on branch: use it
    - Else if exists on main: copy it into branch workspace
    - Else: error
    Returns branch workspace folder Path.
    """
    rel = candidate_rel_path(work_item, letter, language)

    branch_path = create_root / product / rel
    main_path = scan_root / product / rel

    if branch_path.exists():
        return branch_path

    if main_path.exists():
        # Copy from main to branch
        branch_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(main_path, branch_path, dirs_exist_ok=True)
        return branch_path

    print(f"❌ Target folder does not exist on branch or main for letter {letter}: {rel}")
    sys.exit(1)


def resolve_source_folder(product: str, folder_to_organize: str, create_root: Path, scan_root: Path) -> Path:
    """
    Prefer source folder from branch; if missing, read it from main worktree.
    """
    branch_src = create_root / product / folder_to_organize
    if branch_src.exists():
        return branch_src

    main_src = scan_root / product / folder_to_organize
    if main_src.exists():
        return main_src

    print(f"❌ Source folder not found on branch or main: {product}/{folder_to_organize}")
    sys.exit(1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--folder_to_organize", required=True)  # e.g. new
    p.add_argument("--work_item", required=True)          # e.g. WI00001111
    p.add_argument("--language", required=True)           # e.g. EN
    p.add_argument("--product", required=True)            # e.g. CargoWise
    p.add_argument("--letter", required=False)            # optional: A/B/C...
    args = p.parse_args()

    work_item = args.work_item.upper()
    language = args.language.upper()
    product = args.product
    folder_to_organize = args.folder_to_organize
    letter_arg = (args.letter or "").strip().upper()

    validate_inputs(work_item, language)

    create_root = Path(".")     # target branch workspace
    scan_root = Path("_main")   # origin/main worktree (created by workflow)

    # Choose which WI letter folder to organize
    if letter_arg:
        if letter_arg not in ascii_uppercase:
            print("❌ --letter must be A-Z")
            sys.exit(1)
        chosen_letter = letter_arg
    else:
        # Prefer latest existing letter on branch; else latest on main
        branch_letters = find_existing_letters(work_item, language, product, create_root)
        if branch_letters:
            chosen_letter = branch_letters[-1]  # letters are discovered in A..Z order
        else:
            main_letters = find_existing_letters(work_item, language, product, scan_root)
            if not main_letters:
                print("❌ No existing WI folders found on branch or main for this WorkItem+Language.")
                sys.exit(1)
            chosen_letter = main_letters[-1]

    # Ensure the folder exists on branch workspace (copy from main if needed)
    folder_path = ensure_folder_on_branch(work_item, language, product, chosen_letter, create_root, scan_root)

    # Resolve source folder (branch preferred; else main)
    source_folder = resolve_source_folder(product, folder_to_organize, create_root, scan_root)

    # Recreate _images to avoid stale files
    image_folder = folder_path / "_images"
    if image_folder.exists():
        shutil.rmtree(image_folder)
    image_folder.mkdir(parents=True, exist_ok=True)

    # Collect images (deterministic order)
    all_images = []
    for pattern in IMAGE_EXTS:
        all_images.extend(source_folder.glob(pattern))
    all_images = sorted(all_images, key=lambda p: p.name.lower())

    rename_map = {}  # old_name -> "<folder_path.name>.<i>.ext"
    for i, img_file in enumerate(all_images, start=1):
        new_img_name = f"{folder_path.name}.{i}{img_file.suffix.lower()}"
        rename_map[img_file.name] = new_img_name
        shutil.copy2(img_file, image_folder / new_img_name)
        print(f"Copied image: {img_file.name} → {new_img_name}")

    # If no images, keep folder visible in git
    if not all_images:
        (image_folder / ".gitkeep").write_text("", encoding="utf-8")

    # Update markdown files
    img_md_pattern = re.compile(r"!\[(?P<alt>.*?)\]\((?P<path>[^)]+)\)")

    wrote_md = False
    for md_file in source_folder.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")

        def replace_md_image(match: re.Match) -> str:
            alt = match.group("alt")
            orig_path = match.group("path").strip()
            old_name = basename_from_src(orig_path)
            new_name = rename_map.get(old_name, old_name)
            return f"![{alt}](_images/{new_name})"

        new_text = img_md_pattern.sub(replace_md_image, text)

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
        wrote_md = True

    if not wrote_md:
        print(f"⚠️ No .md found in source folder: {source_folder}")

    print("✅ Organized folder:", folder_path)
    print("✅ Used source folder:", source_folder)
    print("✅ Images folder:", image_folder)


if __name__ == "__main__":
    main()
