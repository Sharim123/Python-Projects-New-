from pathlib import Path

root_dir = Path("C:/Users/shari/Desktop/Automate Eerything with Python/Rename All Files")
file_paths = root_dir.iterdir()

for path in file_paths:
    print(path)