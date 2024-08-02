import os

# Define the directory structure
directories = [
    "data/input",
    "data/output",
    "modules",
    "tests"
]

# Define the files to be created
files = {
    "main.py": "",
    "requirements.txt": "",
    "README.md": "",
    "modules/__init__.py": "",
    "modules/text_extraction.py": "",
    "modules/text_masking.py": "",
    "modules/image_processing.py": "",
    "modules/ocr.py": "",
    "modules/utils.py": "",
    "tests/__init__.py": "",
    "tests/test_masking.py": ""
}

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create the files
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)

print("Project structure created successfully.")
