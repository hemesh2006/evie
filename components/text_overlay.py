import sys
import json
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class TextOverlay(QMainWindow):
    def __init__(self, json_path):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.json_path = json_path
        self.labels = []

        # Set up a timer to read the JSON file every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_overlays)
        self.timer.start(1000)

    def update_overlays(self):
        try:
            with open(self.json_path, 'r') as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error reading JSON file: {e}")
            return

        # Clear old labels
        for label in self.labels:
            label.deleteLater()
        self.labels.clear()

        # Create new labels based on JSON data
        for item in data:
            if len(item) < 2:
                print("Invalid item format in JSON. Expected [text, [x, y], font_size, color].")
                continue

            text = item[0]
            position = item[1]
            font_size = item[2] if len(item) > 2 else 12  # Default font size
            color = item[3] if len(item) > 3 else "black"  # Default color

            if not isinstance(position, list) or len(position) != 2:
                print("Invalid position format. Expected [x, y].")
                continue

            x, y = position

            # Set up the QLabel for displaying text
            label = QLabel(self)
            label.setText(text)
            label.setStyleSheet(f"color: {color};")
            label.setFont(QFont("Arial", font_size))
            label.move(x, y)
            label.adjustSize()  # Adjust label size to fit text
            label.show()
            self.labels.append(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Replace 'overlay_text_config.json' with the path to your JSON file
    json_path = r'components\json_folder\text.json'
    overlay = TextOverlay(json_path)
    overlay.show()

    sys.exit(app.exec_())
