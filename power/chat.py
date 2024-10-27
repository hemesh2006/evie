import psutil
import pyautogui
import cv2
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
def battery_info():
    battery = psutil.sensors_battery()
    return battery
def screen_shot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
def take_photo():
# Initialize the webcam
    cap = cv2.VideoCapture(0)

# Capture a single frame
    ret, frame = cap.read()

# Save the frame as a photo
    cv2.imwrite("photo.jpg", frame)

# Release the camera
    cap.release()
    cv2.destroyAllWindows()


def set_volume(target_percentage):
    """
    Sets the system volume to a specific percentage.
    
    Parameters:
    target_percentage (float): The desired volume level as a percentage (0-100).
    
    Returns:
    float: The new volume level in percentage.
    """
    # Ensure target percentage is between 0 and 100
    target_percentage = max(0, min(100, target_percentage))

    # Get audio devices
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Convert percentage to a scalar between 0.0 and 1.0
    target_scalar = target_percentage / 100

    # Set the volume level
    volume.SetMasterVolumeLevelScalar(target_scalar, None)

    print(f"Volume set to: {target_percentage}%")
    return target_percentage



