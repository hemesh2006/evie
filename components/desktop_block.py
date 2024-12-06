import os
import shutil
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Define your directories
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
LOG_FILE = os.path.join(DESKTOP, "actions_log.json")

# Get the list of existing files and directories
EXISTING_ITEMS = set(os.listdir(DESKTOP))

# Initialize the log file
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        print(LOG_FILE)
        json.dump([], f)

def log_action(action, target, error=None):
    """Log the action in a JSON file."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "target": target,
        "error": error
    }
    with open(LOG_FILE, 'r+') as f:
        logs = json.load(f)
        print("OPOOO",LOG_FILE)
        logs.append(entry)
        f.seek(0)
        json.dump(logs, f, indent=4)

class DesktopMonitor(FileSystemEventHandler):
    """Handler for desktop changes."""

    def on_created(self, event):
        try:
            if event.is_directory:
                # If the folder is new, delete it
                if os.path.basename(event.src_path) not in EXISTING_ITEMS:
                    shutil.rmtree(event.src_path)
                    log_action("Deleted folder", event.src_path)
            else:
                # If the file is new, delete it
                if os.path.basename(event.src_path) not in EXISTING_ITEMS:
                    os.remove(event.src_path)
                    log_action("Deleted file", event.src_path)
        except Exception as e:
            log_action("Error", event.src_path, error=str(e))

def maiin():
    # Set up watchdog observer
    observer = Observer()
    handler = DesktopMonitor()
    observer.schedule(handler, DESKTOP, recursive=False)

    try:
        print(f"Monitoring {DESKTOP} for changes...")
        observer.start()
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped monitoring.")
    observer.join()

