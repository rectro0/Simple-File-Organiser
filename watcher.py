from watchdog.events import FileSystemEventHandler
from sorter import FileSorter

class EventHandler(FileSystemEventHandler):
    def __init__(self, sorter):
        self.sorter = sorter

    def on_created(self, event):
        if not event.is_directory:
            self.sorter.sort_file(event.src_path)
