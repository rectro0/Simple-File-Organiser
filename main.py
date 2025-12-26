from pathlib import Path
import time
from watchdog.observers import Observer
from watcher import EventHandler
from sorter import FileSorter

download_path = Path(input("Paste your Folder path here → "))

files = {
    "PDFs": download_path / "PDFs",
    "Images": download_path / "Images",
    "Archives": download_path / "Zip",
    "Videos": download_path / "Videos",
    "Music": download_path / "Audio",
    "Documents": download_path / "Document",
    "Torrents": download_path / "torrents",
    "others": download_path / "others",
}

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".xls", ".mdb", ".mpp", ".doc", ".xml", ".ppt", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "PDFs": [".pdf"],
    "Torrents": [".torrent"],
    "others": [],
}

sorter = FileSorter(download_path, files, file_types)

# sort existing files first
for item in download_path.iterdir():
    sorter.sort_file(item)

observer = Observer()
event_handler = EventHandler(sorter)
observer.schedule(event_handler, download_path, recursive=False)
observer.start()

print(f"Watching folder: {download_path}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
