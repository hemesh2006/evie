import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QSize

class ImageButtonOverlay(QMainWindow):
    def __init__(self, config_file_path):
        super().__init__()

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Paths to JSON files
        self.config_file_path = config_file_path
        self.event_log_file = "button_events.json"

        # Load button configuration and initialize buttons
        self.buttons = {}
        self.load_buttons_from_json()

    def load_buttons_from_json(self):
        """Load buttons from the configuration JSON file."""
        try:
            with open(self.config_file_path, "r") as file:
                button_data = json.load(file)

                for button_info in button_data:
                    # Unpack details
                    button_id = button_info["id"]
                    image_path = button_info["image_path"]
                    position = button_info["position"]
                    size = button_info["size"]

                    # Create a button
                    button = QPushButton(self)
                    button.setObjectName(button_id)
                    button.setStyleSheet("background-color: transparent;")
                    button.clicked.connect(lambda _, b=button_id: self.log_click_event(b))

                    # Set button icon and size
                    pixmap = QPixmap(image_path)
                    if not pixmap.isNull():
                        button.setIcon(QIcon(pixmap))
                        button.setIconSize(QSize(size[0], size[1]))

                    # Set position and add to button dictionary
                    button.move(QPoint(position[0], position[1]))
                    button.resize(size[0], size[1])
                    button.show()
                    self.buttons[button_id] = button

        except Exception as e:
            print(f"Error loading buttons from JSON: {e}")

    def log_click_event(self, button_id):
        """Log the number of clicks for the button."""
        events = self.read_event_log()

        # Initialize or increment the click count for the button
        if button_id not in events:
            events[button_id] = {"click_count": 1}
        else:
            # If click_count is missing, initialize it to 1
            events[button_id]["click_count"] = events[button_id].get("click_count", 0) + 1

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

    def show_overlay(self):
        """Show the overlay window."""
        self.show()

def main():
    app = QApplication(sys.argv)

    # JSON file path with button configurations
    config_file_path = r"components\button_details.json"

    # Create overlay with image buttons
    overlay = ImageButtonOverlay(config_file_path)

    # Show the overlay
    overlay.show_overlay()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
