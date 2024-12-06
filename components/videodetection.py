from ultralytics import YOLO
import cv2
import os
import ctypes
import time

# Path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Constants
HIDDEN_ATTR = 2  # File attribute for hidden files in Windows
DELAY = 1  # Delay between frames in seconds

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Function to set hidden attribute to desktop files
def set_hidden(hidden=True):
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path) or os.path.isdir(file_path):
            # Set or remove the hidden attribute
            attrs = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            if hidden:
                ctypes.windll.kernel32.SetFileAttributesW(file_path, attrs | HIDDEN_ATTR)
            else:
                ctypes.windll.kernel32.SetFileAttributesW(file_path, attrs & ~HIDDEN_ATTR)

# Open video capture (0 for webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the camera.")
    exit()

hidden_state = False  # Track the current hidden state

try:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform detection
        results = model(frame)
        detections = results[0].boxes  # Get detected bounding boxes

        # Check if any person is detected (class ID for person in YOLO is usually 0)
        person_detected = any(result.cls == 0 for result in detections)

        if person_detected and hidden_state:
            print("Person detected! Restoring files...")
            set_hidden(hidden=False)
            hidden_state = False
        elif not person_detected and not hidden_state:
            print("No person detected! Hiding files...")
            set_hidden(hidden=True)
            hidden_state = True
            

        # Optional: Display the video feed with detections
        annotated_frame = results[0].plot()
        cv2.imshow("Person Detection", annotated_frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(DELAY)

finally:
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    # Ensure files are restored when exiting
    set_hidden(hidden=False)
    print("Restored desktop files.")
