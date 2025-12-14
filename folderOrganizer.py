import sys
import shutil
from pathlib import Path
from string import ascii_uppercase
import re

# Fill out this details and run the code
FolderToOrganize = 'new'
WorkItemsNumber = 'wi00001247'
LanguageCode = 'en'
product = 'CargoWise'


#------------------------------------------------------------------------
# Code start from here (Do not change)
#------------------------------------------------------------------------

# ---- Change Case ----
WorkItemsNumber = WorkItemsNumber.upper()
LanguageCode = LanguageCode.upper()


if not WorkItemsNumber.startswith('WI0000'):
    print("WorkItemsNumber must start with WI0000, Please check the value, and run the code again")
    sys.exit(1)
elif len(WorkItemsNumber) != 10:
    print("WorkItemsNumber must be 10 characters, Please check the value, and run the code again")
    sys.exit(1)
elif len(LanguageCode) != 2:
    print("LanguageCode must be 2 characters, Please check the value, and run the code again")
    sys.exit(1)
elif not LanguageCode.isalpha():
    print("LanguageCode must contain only letters, Please check the value, and run the code again")
    sys.exit(1)


# ---- Helpers ----
def folder_exists(folder_path: Path) -> bool:
    return folder_path.is_dir()



def get_next_folder(work_item: str, language: str, root_dir: Path) -> Path:
    for letter in ascii_uppercase:  # 'A' .. 'Z'
        candidate = root_dir / f"{work_item}-{letter}/{work_item}-{letter}-{language}-{language}"
        if not candidate.exists():
            return candidate
    raise ValueError("No free letter (A–Z) left for this WorkItemsNumber")

# ---- Main logic ----
root = Path(product)
baseFolder = root / f'{WorkItemsNumber}-A'

folder_path = get_next_folder(WorkItemsNumber, LanguageCode, root)  

if folder_exists(baseFolder):
    print(f"Folder {baseFolder} already exists.")
    signal = input(
        f"Type yes (y) to continue, this will create a new {folder_path}, "
        "else change the WorkItemsNumber or LanguageCode and run again: "
    )
    while signal.lower() not in ['y', 'yes']:
        signal = input("Invalid input, Type yes (y) to continue, else change the WorkItemsNumber or LanguageCode and run again: ")
else:
    print(f"Creating new folder: {folder_path}")
    signal = input("Type yes (y) to continue: ")
    while signal.lower() not in ['y', 'yes']:
        signal = input("Invalid input, Type yes (y) to continue, or re-run the code with different WorkItemsNumber or LanguageCode: ")

# Actually create the folder
folder_path.mkdir(parents=True, exist_ok=True)

# Copy template 
source_folder = Path(f"{product}/{FolderToOrganize}")

# Create _images subfolder
image_folder = folder_path / '_images'
image_folder.mkdir(parents=True, exist_ok=True)
image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.svg", "*.tiff", "*.gif", "*.bmp", "*.webp"]

# Copy each image found in the source folder
for pattern in image_extensions:
    for img_file in source_folder.glob(pattern):
        shutil.copy2(img_file, image_folder / img_file.name)
        print(f"Copied image: {img_file.name} → {image_folder}")


# 2. Process and copy .md files
img_md_pattern = re.compile(r'!\[(?P<alt>.*?)\]\((?P<path>[^)]+)\)')

for md_file in source_folder.glob("*.md"):
    # Read original markdown
    text = md_file.read_text(encoding="utf-8")

    # Replace image paths: any path -> _images/<basename>
    def replace_md_image(match: re.Match) -> str:
        alt = match.group('alt')
        orig_path = match.group('path').strip()

        # Take just the filename part, drop any subfolders
        filename = Path(orig_path).name
        new_path = f"_images/{filename}"

        return f"![{alt}]({new_path})"

    new_text = img_md_pattern.sub(replace_md_image, text)

    #Handle HTML <img src="..."> tags
    new_text = re.sub(
        r'(<img\s+[^>]*src=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + f"_images/{Path(m.group(2)).name}" + m.group(3),
        new_text,
    )


    new_name = f"{folder_path.name}.md"  
    dest_md = folder_path / new_name

    # Write processed markdown instead of copying raw file
    dest_md.write_text(new_text, encoding="utf-8")

print(f"Markdown and images processed into: {folder_path}")
