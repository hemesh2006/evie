import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer

class InputOverlay(QMainWindow):
    def __init__(self):
        super().__init__()

        # Overlay window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setAttribute(Qt.WA_TranslucentBackground)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Input fields
        self.single_line_input = None
        self.multi_line_input = None
        self.json_file_path = r"C:\Users\HP\Desktop\evie\components\json_folder\inputs.json"
        self.last_json_mod_time = 0

        # Load inputs initially
        self.load_inputs()

        # Timer to detect JSON changes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_json_changes)
        self.timer.start(1000)

    def load_inputs(self):
        """Load input definitions from inputs.json"""
        try:
            if not os.path.exists(self.json_file_path):
                return

            with open(self.json_file_path, "r") as f:
                inputs = json.load(f)

            # Clear previous inputs
            self.clear_inputs()

            if isinstance(inputs, list) and inputs:
                for placeholder, start_pos, end_pos, rgb_color, font_size, is_single in inputs:
                    color = f"rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})"
                    if is_single:
                        self.single_line_input = self.create_single_line_input(placeholder, start_pos, end_pos, color, font_size)
                    else:
                        self.multi_line_input = self.create_multi_line_input(placeholder, start_pos, end_pos, color, font_size)

                # Show inputs
                if self.single_line_input:
                    self.single_line_input.show()
                    self.single_line_input.setFocus()
                if self.multi_line_input:
                    self.multi_line_input.show()
                    self.multi_line_input.setFocus()

        except Exception as e:
            print(f"Error loading inputs: {e}")

    def clear_inputs(self):
        """Hide and remove current input fields"""
        if self.single_line_input:
            self.single_line_input.hide()
            self.single_line_input.deleteLater()
            self.single_line_input = None
        if self.multi_line_input:
            self.multi_line_input.hide()
            self.multi_line_input.deleteLater()
            self.multi_line_input = None

    def create_single_line_input(self, placeholder, start_pos, end_pos, color, font_size):
        widget = QLineEdit(self)
        widget.setPlaceholderText(placeholder)
        widget.setStyleSheet(
            f"background-color: rgba(0,0,0,0); color: {color}; border:0px; font-size:{font_size}px; padding:5px;"
        )
        widget.setFocusPolicy(Qt.StrongFocus)
        widget.returnPressed.connect(self.save_single_line)
        widget.setGeometry(start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
        return widget

    def create_multi_line_input(self, placeholder, start_pos, end_pos, color, font_size):
        widget = QTextEdit(self)
        widget.setPlaceholderText(placeholder)
        widget.setStyleSheet(
            f"background-color: rgba(0,0,0,0); color: {color}; border:0px; font-size:{font_size}px; padding:5px;"
        )
        widget.setFocusPolicy(Qt.StrongFocus)
        widget.installEventFilter(self)
        widget.setGeometry(start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
        return widget

    def eventFilter(self, source, event):
        if event.type() == event.KeyPress:
            if source is self.multi_line_input and event.key() in (Qt.Key_Return, Qt.Key_Enter):
                if event.modifiers() == Qt.ShiftModifier:
                    cursor = self.multi_line_input.textCursor()
                    cursor.insertText("\n")
                    return True
                else:
                    self.save_multi_line()
                    return True
        return super().eventFilter(source, event)

    def save_single_line(self):
        value = self.single_line_input.text() if self.single_line_input else ""
        self.save_output(single_line=value, multi_line="")
        self.erase_input_json()
        self.clear_inputs()  # Hide inputs but keep overlay alive

    def save_multi_line(self):
        value = self.multi_line_input.toPlainText() if self.multi_line_input else ""
        self.save_output(single_line="", multi_line=value)
        self.erase_input_json()
        self.clear_inputs()

    def save_output(self, single_line="", multi_line=""):
        data = {"single_line": single_line, "multi_line": multi_line}
        try:
            with open("output.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Saved to output.json")
        except Exception as e:
            print(f"Error saving output.json: {e}")

    def erase_input_json(self):
        try:
            with open(self.json_file_path, "w") as f:
                json.dump([], f)
            print("Erased inputs.json")
        except Exception as e:
            print(f"Error erasing inputs.json: {e}")

    def check_json_changes(self):
        try:
            if not os.path.exists(self.json_file_path):
                return
            mod_time = os.path.getmtime(self.json_file_path)
            if mod_time != self.last_json_mod_time:
                self.last_json_mod_time = mod_time
                print("inputs.json updated, reloading overlay...")
                self.load_inputs()
        except Exception as e:
            print(f"Error checking JSON changes: {e}")

    def show_overlay(self):
        self.raise_()
        self.activateWindow()
        self.show()

def main():
    app = QApplication(sys.argv)
    overlay = InputOverlay()
    overlay.show_overlay()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
