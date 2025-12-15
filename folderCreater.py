import sys
import shutil
from pathlib import Path
from string import ascii_uppercase
import argparse

def get_next_folder(work_item: str, language: str, root_dir: Path) -> Path:
    for letter in ascii_uppercase:  # 'A' .. 'Z'
        candidate = root_dir / f"{work_item}-{letter}/{work_item}-{letter}-{language}-{language}"
        if not candidate.exists():
            return candidate
    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--work_item", required=True)
    p.add_argument("--language", required=True)
    p.add_argument("--product", required=True)
    p.add_argument("--template", default="UpdateNoteTemplate.md")
    args = p.parse_args()

    WorkItemsNumber = args.work_item.upper()
    LanguageCode = args.language.upper()
    product = args.product

    if not WorkItemsNumber.startswith("WI00") or len(WorkItemsNumber) != 10 or not WorkItemsNumber[-8:].isdigit():
        print("❌ WorkItemsNumber must look like WI00######## (10 chars)")
        sys.exit(1)
    if len(LanguageCode) != 2 or not LanguageCode.isalpha():
        print("❌ LanguageCode must be 2 letters")
        sys.exit(1)

    template = Path(args.template)
    if not template.exists():
        print(f"❌ Template not found: {template}")
        sys.exit(1)

    root = Path(product)
    folder_path = get_next_folder(WorkItemsNumber, LanguageCode, root)

    folder_path.mkdir(parents=True, exist_ok=True)

    new_name = f"{folder_path.name}.md"
    shutil.copy2(template, folder_path / new_name)

    image_folder = folder_path / "_images"
    image_folder.mkdir(parents=True, exist_ok=True)

    print(f"✅ Created: {folder_path}")
    print(f"✅ Copied template to: {folder_path / new_name}")
    print(f"✅ Created images folder: {image_folder}")

if __name__ == "__main__":
    main()
