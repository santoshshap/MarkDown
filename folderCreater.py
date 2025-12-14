import sys
import shutil
from pathlib import Path
from string import ascii_uppercase

# Fill out this details and run the code
WorkItemsNumber = 'WI00786995'
LanguageCode = 'EN'
product = 'CargoWise'




#------------------------------------------------------------------------
# Code start from here (Do not change)
#------------------------------------------------------------------------

# ---- Change Case ----
WorkItemsNumber = WorkItemsNumber.upper()
LanguageCode = LanguageCode.upper()


if not WorkItemsNumber.startswith('WI00'):
    print("WorkItemsNumber must start with WI00, Please check the value, and run the code again")
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

template = Path("UpdateNoteTemplate.md")

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

folder_path = get_next_folder(WorkItemsNumber, LanguageCode, root)  # <-- this is a Path


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


print(folder_path)

# Actually create the folder
folder_path.mkdir(parents=True, exist_ok=True)

new_name = f"{folder_path.name}.md"  
shutil.copy2(template, folder_path / new_name)

# Copy template 


# Create _images subfolder
image_folder = folder_path / '_images'
image_folder.mkdir(parents=True, exist_ok=True)

print(f"Folder {folder_path} created successfully with {new_name} copied and _images folder created.")
