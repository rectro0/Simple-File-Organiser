import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog import EventHandler

filePath = input("Paste your Folder path here --> ")

download_path = Path(filePath)


files = {
    "PDFs": Path(download_path) / "PDFs",
    "Images": Path(download_path) / "Images",
    "Archives": Path(download_path) / "Zip",
    "Videos": Path(download_path) / "Videos",
    "Music": Path(download_path) / "Audio",
    "Documents": Path(download_path) / "Document",
    "Torrents": Path(download_path) / "torrents",
    "others": Path(download_path) / "others",
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

event_handler = EventHandler(download_path, files, file_types)
observer = Observer()
observer.schedule(event_handler, download_path, recursive=False)
observer.start()

try:
    print(f"Watching for changes in: {download_path}")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
