import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class InputOverlay(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window to be frameless, transparent, always on top, and full screen
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set the window to full screen
        self.showFullScreen()

        # Create a central widget to hold the input fields
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setAttribute(Qt.WA_TranslucentBackground)  # Make the central widget transparent

        # Create a layout to arrange the input fields
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # No margin for full coverage

        # Create input fields and initialize their positions
        self.single_line_input = None
        self.multi_line_input = None
        self.json_file_path = r"components\json_folder\inputs.json"
        self.last_json_mod_time = 0

        # Load initial inputs from the JSON file
        self.load_inputs()

        # Set a timer to check for JSON changes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_json_changes)
        self.timer.start(1000)  # Check every second

    def load_inputs(self):
        """Load inputs from a JSON file and create input fields."""
        try:
            with open(self.json_file_path, "r") as json_file:
                inputs = json.load(json_file)

                # Clear existing inputs
                self.clear_inputs()

                if isinstance(inputs, list) and inputs:  # Ensure it's a list and not empty
                    for placeholder, start_pos, end_pos, rgb_color, font_size, is_single in inputs:
                        # Convert RGB list to a string format for stylesheet
                        color = f"rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})"

                        if is_single:
                            self.single_line_input = self.create_single_line_input(placeholder, start_pos, end_pos, color, font_size)
                        else:
                            self.multi_line_input = self.create_multi_line_input(placeholder, start_pos, end_pos, color, font_size)

                    # Show the input fields
                    if self.single_line_input:
                        self.single_line_input.show()
                        self.single_line_input.setFocus()  # Set focus to the single line input
                    if self.multi_line_input:
                        self.multi_line_input.show()
                        self.multi_line_input.setFocus()  # Set focus to the multi line input
                else:
                    print("No input definitions found in JSON or the format is incorrect.")

        except json.JSONDecodeError:
            print("Error: JSON file is not in readable format.")
        except Exception as e:
            print(f"Error loading inputs from JSON: {e}")

    def clear_inputs(self):
        """Clear existing input fields."""
        if self.single_line_input:
            self.single_line_input.hide()
            self.single_line_input.deleteLater()
            self.single_line_input = None
        if self.multi_line_input:
            self.multi_line_input.hide()
            self.multi_line_input.deleteLater()
            self.multi_line_input = None

    def create_single_line_input(self, placeholder, start_pos, end_pos, color, font_size):
        """Create a single-line input field."""
        single_line_input = QLineEdit(self)
        single_line_input.setPlaceholderText(placeholder)
        single_line_input.setStyleSheet(f"background-color: rgba(0, 0, 0, 0); color: {color}; border: 0px solid rgba(255, 255, 255, 0.5); border-radius: 5px; padding: 5px; font-size: {font_size}px;")
        single_line_input.setFocusPolicy(Qt.StrongFocus)  # Set focus policy to allow focus with other overlays
        single_line_input.returnPressed.connect(self.save_single_line_input)  # Connect Enter key
        single_line_input.setGeometry(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        return single_line_input

    def create_multi_line_input(self, placeholder, start_pos, end_pos, color, font_size):
        """Create a multi-line input field."""
        multi_line_input = QTextEdit(self)
        multi_line_input.setPlaceholderText(placeholder)
        multi_line_input.setStyleSheet(f"background-color: rgba(0, 0, 0, 0); color: {color}; border: 0px solid rgba(255, 255, 255, 0.5); border-radius: 5px; padding: 5px; font-size: {font_size}px;")
        multi_line_input.setFocusPolicy(Qt.StrongFocus)  # Set focus policy to allow focus with other overlays
        multi_line_input.installEventFilter(self)  # Install event filter for key press
        multi_line_input.setGeometry(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        return multi_line_input

    def eventFilter(self, source, event):
        """Handle key press events."""
        if event.type() == event.KeyPress:
            if source is self.multi_line_input:
                if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                    if event.modifiers() == Qt.ShiftModifier:
                        # Allow Shift + Enter to insert a new line
                        cursor = self.multi_line_input.textCursor()
                        cursor.insertText("\n")  # Correctly insert a new line
                        return True  # Prevent further handling of the event
                    else:
                        self.save_multi_line_input()  # Call save_multi_line_input when Enter is pressed without Shift
                        return True  # Prevent further handling of the event
        return super().eventFilter(source, event)

    def save_single_line_input(self):
        """Save single line input to a JSON file and erase the input file contents."""
        single_line_value = self.single_line_input.text() if self.single_line_input else ""

        # Save the data to output.json
        data = {
            "single_line": single_line_value,
            "multi_line": ""
        }

        try:
            with open("output.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            print("Single line input saved to output.json")

            # Erase the contents of inputs.json (write an empty list)
            self.erase_json_contents()

        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def save_multi_line_input(self):
        """Save multi-line input to a JSON file and erase the input file contents."""
        multi_line_value = self.multi_line_input.toPlainText() if self.multi_line_input else ""

        # Save the data to output.json
        data = {
            "single_line": "",
            "multi_line": multi_line_value
        }

        try:
            with open("output.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            print("Multi-line input saved to output.json")

            # Erase the contents of inputs.json (write an empty list)
            self.erase_json_contents()

        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def erase_json_contents(self):
        """Erase the contents of the JSON file.""" 
        try:
            with open(self.json_file_path, "w") as json_file:
                json.dump([], json_file)  # Write empty list
            print(f"Contents of {self.json_file_path} erased.")
        except Exception as e:
            print(f"Error erasing JSON contents: {e}")

    def check_json_changes(self):
        """Check if the JSON file has been modified."""
        try:
            current_mod_time = os.path.getmtime(self.json_file_path)
            if current_mod_time != self.last_json_mod_time:
                self.last_json_mod_time = current_mod_time
                print("JSON file has been updated. Reloading inputs...")
                self.load_inputs()  # Reload inputs from JSON when changes are detected
        except Exception as e:
            print(f"Error checking JSON file: {e}")

    def show_overlay(self):
        """Show the overlay window and force focus to the inputs."""  
        self.raise_()  # Bring the window to the front
        self.activateWindow()  # Activate the window
        self.show()

def main():
    app = QApplication(sys.argv)

    # Create and show the input overlay
    overlay = InputOverlay()
    overlay.show_overlay()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
