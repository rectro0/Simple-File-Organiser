import json
import time
from pathlib import Path
from watchdog.observers import Observer
from watcher import EventHandler
from sorter import FileSorter

CONFIG_FILE = "config.json"


watched_folders = []

if not Path(CONFIG_FILE).exists():
    print("Enter folders to watch. Type 'done' when finished.")
    while True:
        folder = input("Folder path → ").strip()
        if folder.lower() == "done":
            break
        if Path(folder).exists() and Path(folder).is_dir():
            watched_folders.append(folder)
        else:
            print("Invalid folder, try again.")

    # Save config for next launch
    if watched_folders:
        with open(CONFIG_FILE, "w") as f:
            json.dump({"watched_folders": watched_folders}, f, indent=4)
else:
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
        watched_folders = data.get("watched_folders", [])

if not watched_folders:
    print("No valid folders to watch. Exiting.")
    exit()


subfolders = {
    "PDFs": "PDFs",
    "Images": "Images",
    "Archives": "Zip",
    "Videos": "Videos",
    "Music": "Audio",
    "Documents": "Document",
    "Torrents": "torrents",
    "others": "others",
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

#observing in backroound

observers = []

for folder_path in watched_folders:
    folder_path = Path(folder_path)
    files = {key: folder_path / name for key, name in subfolders.items()}

    sorter = FileSorter(folder_path, files, file_types)

    for item in folder_path.iterdir():
        sorter.sort_file(item)

    event_handler = EventHandler(sorter)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    observers.append(observer)

print("\nWatching folders:")
for folder in watched_folders:
    print(folder)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for observer in observers:
        observer.stop()

for observer in observers:
    observer.join()
