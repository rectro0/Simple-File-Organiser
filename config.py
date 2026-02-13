import json
from pathlib import Path

CONFIG_FILE = "config.json"

if not Path(CONFIG_FILE).exists():
    print("First time setup.")
    print("Enter folder paths to watch.")
    print("Type 'done' when finished.\n")

    folders = []

    while True:
        folder = input("Folder path: ")

        if folder.lower() == "done":
            break

        if Path(folder).exists():
            folders.append(folder)
            print("Added.")
        else:
            print("Path does not exist.")

    if not folders:
        print("No folders provided. Exiting.")
        exit()

    data = {
        "watched_folders": folders
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("Setup complete. Restart program.")
else:
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)

    print("Loaded config:")
    print(config)
