import sys
import shutil
import base64
from pathlib import Path
from string import ascii_uppercase
import argparse

def get_next_folder(work_item: str, language: str, product: str, create_root: Path, scan_root: Path) -> Path:
    """
    create_root: repo root where we create folders (target branch workspace)
    scan_root:   repo root we scan for existing folders (origin/main worktree at ./_main)
    Picks next free letter not used on main AND not used on the target branch.
    Returns the CREATE path (in create_root).
    """
    create_product_root = create_root / product
    scan_product_root = scan_root / product

    for letter in ascii_uppercase:  # 'A' .. 'Z'
        candidate_rel = f"{work_item}-{letter}/{work_item}-{letter}-{language}"

        candidate_create = create_product_root / candidate_rel
        candidate_on_main = scan_product_root / candidate_rel
        candidate_on_branch = create_product_root / candidate_rel

        if (not candidate_on_main.exists()) and (not candidate_on_branch.exists()):
            return candidate_create

    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--work_item", required=True)
    p.add_argument("--language", required=True)
    p.add_argument("--product", required=True)
    p.add_argument("--template", default="UpdateNoteTemplate.md")
    args = p.parse_args()

    work_item = args.work_item.upper()
    language = args.language.upper()

    language = language[language.find("(")+1 : language.rfind(")")]
    product = args.product

    if not work_item.startswith("WI00") or len(work_item) != 10 or not work_item[-8:].isdigit():
        print("❌ WorkItemsNumber must look like WI00######## (10 chars)")
        sys.exit(1)
        
    template = Path(args.template)
    if not template.exists():
        print(f"❌ Template not found: {template}")
        sys.exit(1)

    create_root = Path(".")     # current branch workspace
    scan_root = Path("_main")   # origin/main worktree (created by workflow)

    folder_path = get_next_folder(work_item, language, product, create_root, scan_root)

    folder_path.mkdir(parents=True, exist_ok=True)

    md_name = f"{folder_path.name}.md"
    shutil.copy2(template, folder_path / md_name)

    image_folder = folder_path / "_images"
    image_folder.mkdir(parents=True, exist_ok=True)

    # 1x1 transparent PNG (base64)
    blank_png_b64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/"
        "P9x9WQAAAABJRU5ErkJggg=="
    )

    sample_image_path = image_folder / f"{folder_path.name}-1.png"
    sample_image_path.write_bytes(base64.b64decode(blank_png_b64))

    print(f"✅ Created: {folder_path}")
    print(f"✅ Copied template to: {folder_path / md_name}")
    print(f"✅ Created images folder: {image_folder}")
    print(f"✅ Sample image created: {sample_image_path}")

if __name__ == "__main__":
    main()
