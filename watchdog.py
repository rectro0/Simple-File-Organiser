import os
import shutil
from pathlib import Path
from watchdog.events import FileSystemEventHandler

class EventHandler(FileSystemEventHandler):
    def __init__(self, download_path, files, file_types):
        self.download_path = Path(download_path)
        self.files = files
        self.file_types = file_types

        
        for folder in self.files.values():
            folder.mkdir(exist_ok=True)

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)
        name, ext = os.path.splitext(file_path.name)
        ext = ext.lower()

        moved = False
        for category, extensions in self.file_types.items():
            if ext in extensions:
                dest = self.files[category] / file_path.name
                if not dest.exists():
                    shutil.move(str(file_path), str(dest))
                    print(f"Moved {file_path.name} to {self.files[category]}")
                else:
                    print(f"{dest} already exists, skipped!")
                moved = True
                break

        if not moved:
            dest = self.files["others"] / file_path.name
            if not dest.exists():
                shutil.move(str(file_path), str(dest))
                print(f"Unknown file type for {file_path.name}, moved to Others")
            else:
                print(f"{dest} already exists, skipped!")
