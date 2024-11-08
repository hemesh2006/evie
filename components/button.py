import sys
import json
import os
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QSize, QTimer

class ImageButtonOverlay(QMainWindow):
    def __init__(self, config_file_path):
        super().__init__()

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Paths to JSON files
        self.config_file_path = config_file_path
        self.event_log_file = r"components\json_folder\button_events.json"

        # Initialize last_modified_time attribute
        self.last_modified_time = None

        # Load button configuration and initialize buttons
        self.buttons = {}
        self.load_buttons_from_json()

        # Reset click count to 0 on initial run
        self.reset_click_count()

        # Timer to continuously check for updates in the JSON file
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.check_and_update_json)
        self.update_timer.start(500)  # Check every 500 ms

    def load_buttons_from_json(self):
        """Load buttons from the configuration JSON file and synchronize with UI."""
        try:
            with open(self.config_file_path, "r") as file:
                button_data = json.load(file)

            # Remove buttons that are no longer in the JSON file
            current_button_ids = {button_info["id"] for button_info in button_data}
            for button_id in list(self.buttons.keys()):
                if button_id not in current_button_ids:
                    self.buttons[button_id].deleteLater()
                    del self.buttons[button_id]

            # Create or update buttons based on JSON file
            for button_info in button_data:
                button_id = button_info["id"]
                image_path = button_info["image_path"]
                position = button_info["position"]
                size = button_info["size"]

                if button_id in self.buttons:
                    # Update existing button if properties have changed
                    button = self.buttons[button_id]
                    if button.icon().name() != image_path or button.size() != QSize(*size) or \
                       button.pos() != QPoint(*position):
                        self.update_button(button, image_path, position, size)
                else:
                    # Create new button if it doesn't exist
                    self.create_button(button_id, image_path, position, size)

        except Exception as e:
            print(f"Error loading buttons from JSON: {e}")

    def create_button(self, button_id, image_path, position, size):
        """Create a button and add it to the overlay."""
        button = QPushButton(self)
        button.setObjectName(button_id)
        button.setStyleSheet("background-color: transparent;")
        button.clicked.connect(lambda _, b=button_id: self.log_click_event(b))

        # Set button icon and size
        pixmap = QPixmap("C:\\Users\\HP\\Desktop\\evie\\asset\\src_image\\"+image_path)
        if not pixmap.isNull():
            button.setIcon(QIcon(pixmap))
            button.setIconSize(QSize(size[0], size[1]))

        # Set position and add to button dictionary
        button.move(QPoint(position[0], position[1]))
        button.resize(size[0], size[1])
        button.show()
        self.buttons[button_id] = button
        print(f"Created button '{button_id}'")

    def update_button(self, button, image_path, position, size):
        """Update an existing button's image, position, and size."""
        # Update button icon
        pixmap = QPixmap("C:\\Users\\HP\\Desktop\\evie\\asset\\src_image\\"+image_path)
        if not pixmap.isNull():
            button.setIcon(QIcon(pixmap))
            button.setIconSize(QSize(size[0], size[1]))

        # Update button position and size
        button.move(QPoint(position[0], position[1]))
        button.resize(size[0], size[1])
        print(f"Updated button '{button.objectName()}' with new properties.")

    def reset_click_count(self):
        """Reset the click count of all buttons to 0 on initial run."""
        events = self.read_event_log()

        # Initialize click_count to 0 for all buttons
        for button_id in self.buttons:
            if button_id not in events:
                events[button_id] = {"click_count": 0}
            else:
                events[button_id]["click_count"] = 0

        self.write_event_log(events)

    def log_click_event(self, button_id):
        """Log the number of clicks for the button."""
        events = self.read_event_log()

        # Ensure click_count is an integer, even if the JSON file has unexpected data
        try:
            events.setdefault(button_id, {})  # Initialize if button_id not present
            events[button_id]["click_count"] = int(events[button_id].get("click_count", 0)) + 1
        except ValueError:
            # If click_count is not a valid integer, reset it to 1
            events[button_id]["click_count"] = 1

        print(f"{button_id} clicked. Total clicks: {events[button_id]['click_count']}")

        self.write_event_log(events)

    def read_event_log(self):
        """Read the event log JSON file."""
        try:
            with open(self.event_log_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def write_event_log(self, events):
        """Write the updated event log to the JSON file."""
        with open(self.event_log_file, "w") as file:
            json.dump(events, file, indent=4)

    def check_and_update_json(self):
        """Check if the JSON file has been updated, and if so, update button properties."""
        current_modified_time = self.get_json_file_modified_time()

        if current_modified_time != self.last_modified_time:
            print(f"JSON file has been updated at {current_modified_time}. Refreshing button properties.")
            self.last_modified_time = current_modified_time
            self.wait_for_valid_json()

    def wait_for_valid_json(self):
        """Wait for the JSON file to be valid before updating button data."""
        while True:
            try:
                # Try loading the JSON to ensure it's valid
                with open(self.config_file_path, "r") as file:
                    json.load(file)
                self.load_buttons_from_json()
                break  # Exit loop if JSON is valid
            except json.JSONDecodeError:
                print("JSON file is invalid. Waiting for a valid file...")
                time.sleep(0.5)  # Wait briefly before retrying

    def get_json_file_modified_time(self):
        """Get the last modified time of the JSON file."""
        try:
            return os.path.getmtime(self.config_file_path)
        except FileNotFoundError:
            return None

    def show_overlay(self):
        """Show the overlay window."""
        self.show()

def main():
    app = QApplication(sys.argv)

    # JSON file path with button configurations
    config_file_path = r"components\json_folder\button_details.json"

    # Create overlay with image buttons
    overlay = ImageButtonOverlay(config_file_path)

    # Show the overlay
    overlay.show_overlay()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
