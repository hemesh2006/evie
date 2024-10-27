import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPoint, QTimer

class ImageOverlay(QMainWindow):
    def __init__(self, images):
        super().__init__()

        # Set window to be frameless, transparent, always on top, and full screen
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set the window to full screen
        self.showFullScreen()

        # Create a central widget to hold the images
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setAttribute(Qt.WA_TranslucentBackground)  # Make the central widget transparent

        self.image_labels = []  # To store image labels
        self.blink_timers = []  # To store timers for blinking
        self.blink_counts = []  # To keep track of blink counts for each image

        # Load images initially
        self.load_images(images)

        # Timer to check if all images have finished blinking
        self.check_blink_timer = QTimer(self)
        self.check_blink_timer.timeout.connect(self.check_all_blinks_completed)
        self.check_blink_timer.start(100)  # Check every 100 ms for faster updates

    def load_images(self, images):
        """Load images from the provided list."""
        self.clear_images()  # Clear existing images

        for image_data in images:
            # Unpack the image data
            image_path, position, blink_count, blink_interval = image_data
            position = QPoint(position[0], position[1])  # Convert list to QPoint
            label = QLabel(self)
            pixmap = QPixmap(image_path)

            if pixmap.isNull():
                print(f"Failed to load image: {image_path}")
                continue  # Skip this image if it failed to load

            # Set the image in the label at its original size
            label.setPixmap(pixmap)
            label.setAttribute(Qt.WA_TranslucentBackground)  # Make the label background transparent
            label.adjustSize()  # Adjust the label size to fit the pixmap
            label.move(position)  # Move the label to the specified position
            label.show()  # Ensure the label is shown immediately

            # Add the label and blink count to the overlay
            self.image_labels.append(label)
            self.blink_counts.append(blink_count)  # Store the blink count for this image

            # Set up blinking if blink_count is greater than zero
            if blink_count > 0:
                self.start_blinking(label, blink_count, blink_interval)

    def start_blinking(self, label, blink_count, blink_interval):
        """Start blinking the label."""
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.blink_image(label, timer))
        timer.start(blink_interval)  # Start timer with the specific blink interval
        self.blink_timers.append(timer)  # Store the timer

    def blink_image(self, label, timer):
        """Toggle visibility of the label and handle blink count."""
        label.setVisible(not label.isVisible())
        
        # Find the index of the label to update the blink count
        index = self.image_labels.index(label)
        self.blink_counts[index] -= 1  # Decrease the blink count for this image

        # Check if the blink count has reached zero
        if self.blink_counts[index] <= 0:
            label.hide()  # Hide the label when blink count reaches zero
            timer.stop()  # Stop the timer for this image
            self.blink_timers.remove(timer)  # Remove the timer from the list

    def clear_images(self):
        """Clear existing images from the overlay."""
        for label in self.image_labels:
            label.hide()  # Hide label before removing
        self.image_labels.clear()  # Clear the list of labels
        self.blink_counts.clear()  # Clear the blink counts

    def check_all_blinks_completed(self):
        """Check if all images have completed blinking."""
        if all(count <= 0 for count in self.blink_counts):
            print("All blink counts reached. Updating images from JSON...")
            self.update_images()  # Update images from JSON after all blinks are done

    def update_images(self):
        """Read images from JSON file and update overlay."""
        print("Reading JSON file...")
        try:
            with open("images.json", "r") as file:
                images = json.load(file)
                self.load_images(images)
        except Exception as e:
            print(f"Error reading JSON file: {e}")

    def show_overlay(self):
        """Show the overlay window."""
        self.show()

def main():
    app = QApplication(sys.argv)

    # Initially load images from a JSON file
    overlay = ImageOverlay([])  # Start with empty images

    # Show the overlay
    overlay.show_overlay()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
#image,postion,count,intervel 