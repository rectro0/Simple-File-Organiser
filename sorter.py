import os
import shutil
from pathlib import Path

class FileSorter:
    def __init__(self, download_path, files, file_types):
        self.download_path = Path(download_path)
        self.files = files
        self.file_types = file_types

        for folder in self.files.values():
            folder.mkdir(exist_ok=True)

    def sort_file(self, file_path):
        file_path = Path(file_path)
        if not file_path.exists() or not file_path.is_file():
            return

        ext = file_path.suffix.lower()
        moved = False

        for category, extensions in self.file_types.items():
            if ext in extensions:
                dest = self.files[category] / file_path.name
                if not dest.exists():
                    shutil.move(str(file_path), str(dest))
                    print(f"Moved {file_path.name} → {category}")
                moved = True
                break

        if not moved:
            dest = self.files["others"] / file_path.name
            if not dest.exists():
                shutil.move(str(file_path), str(dest))
                print(f"Moved {file_path.name} → others")
