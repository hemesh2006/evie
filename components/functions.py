import psutil
import pyautogui
import cv2
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame
import time
import subprocess
import webbrowser
import pygetwindow as gw
import pyautogui
import time
import pygetwindow as gw
import os
import time
import subprocess
import pyautogui
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




# Initialize pygame mixer
pygame.mixer.init()

def play_music(file_path):
    """Play a music file."""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("Playing music...")

    # Keep program running while music is playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Check every second if the music is still playing

    print("Music playback has ended.")

def pause_music():
    """Pause the music."""
    pygame.mixer.music.pause()
    print("Music paused.")

def resume_music():
    """Resume the paused music."""
    pygame.mixer.music.unpause()
    print("Music resumed.")

def stop_music():
    """Stop the music."""
    pygame.mixer.music.stop()
    print("Music stopped.")

# Example usage:
# play_music("your_song.mp3")  # Replace with the path to your music file
# pause_music()
# resume_music()
# stop_music()
def open_application(app_path):
    """Open an application given its executable file path."""
    try:
        # Open the application
        subprocess.Popen([app_path])
        print(f"Opened application: {app_path}")
    except Exception as e:
        print(f"Failed to open application: {e}")

def google_search(query):
    """Perform a Google search for the specified query."""
    # Construct the Google search URL
    url = f"https://www.google.com/search?q={query}"
    # Open the URL in the default web browser
    webbrowser.open(url)


def search_youtube(query):
    """Search YouTube for the specified query."""
    # Construct the YouTube search URL
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    # Open the search URL in the default web browser
    webbrowser.open(search_url)


def click(x=None, y=None):
    """Click at the specified coordinates (x, y). If no coordinates are given, click at the current mouse position."""
    if x is not None and y is not None:
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
    else:
        pyautogui.click()
        print("Clicked at current position")

def scroll_down(amount):
    """Scroll down by the specified amount."""
    pyautogui.scroll(-amount)  # Negative value to scroll down
    print(f"Scrolled down by {amount}")

def scroll_up(amount):
    """Scroll up by the specified amount."""
    pyautogui.scroll(amount)  # Positive value to scroll up
    print(f"Scrolled up by {amount}")



def close_tab():
    """Close the current active tab in the web browser."""
    # Simulate pressing Ctrl + W
    pyautogui.hotkey('ctrl', 'w')
    print("Closed the current tab.")



def close_current_window():
    try:
        # Get the currently active window
        active_window = gw.getActiveWindow()
        if active_window:
            active_window.close()
            print("Closed the active application.")
        else:
            print("No active window found.")
    except Exception as e:
        print(f"Error: {e}")



def search_wikipedia(query):
    """Search Wikipedia for the specified query."""
    # Construct the Wikipedia search URL
    search_url = f"https://en.wikipedia.org/wiki/Special:Search?search={query.replace(' ', '+')}"
    # Open the search URL in the default web browser
    webbrowser.open(search_url)

def shutdown():
    """Shut down the computer."""
    os.system("shutdown /s /t 1")  # Shutdown command for Windows

def sleep():
    """Put the computer to sleep."""
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def hybrid_sleep():
    """Put the computer into hybrid sleep."""
    os.system("powercfg /h on")  # Enable hibernation
    os.system("rundll32.exe powrprof.dll,SetSuspendState 1,1,0")

def deep_sleep():
    """Put the computer into deep sleep (hibernation)."""
    os.system("shutdown /h")  # Hibernate command for Windows

def wifi_on():
    """Enable Wi-Fi."""
    subprocess.call(["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"])

def wifi_off():
    """Disable Wi-Fi."""
    subprocess.call(["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"])
import pygetwindow as gw

def minimize_current_window():
    """Minimize the currently active window."""
    try:
        # Get the currently active window
        active_window = gw.getActiveWindow()
        if active_window:
            active_window.minimize()
            print(f"Minimized: {active_window.title}")
        else:
            print("No active window found.")
    except Exception as e:
        print(f"Error: {e}")


def type_keyboard(text, delay=0.1):
    """Type the specified text on the keyboard with an optional delay between keystrokes."""
    # Give a brief pause before typing
    time.sleep(1)  # Adjust this delay as necessary for focus
    for char in text:
        pyautogui.press(char)  # Type each character
        time.sleep(delay) 


def maximize_current_window():
    """Maximize the currently active window."""
    try:
        # Get the currently active window
        active_window = gw.getActiveWindow()
        if active_window:
            active_window.maximize()
            print(f"Maximized: {active_window.title}")
        else:
            print("No active window found.")
    except Exception as e:
        print(f"Error: {e}")



def execute_command(command):
    """Execute a command in CMD and print the output."""
    try:
        # Open CMD, execute the command, and capture the output
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print("Command Output:\n", result.stdout)
        if result.stderr:
            print("Command Error:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def get_disk_space(disk):
    """Return the available disk space as a percentage for the specified disk."""
    try:
        # Get disk usage
        usage = psutil.disk_usage(disk)
        available_percent = (usage.free / usage.total) * 100
        return available_percent
    except Exception as e:
        print(f"Error: {e}")
        return None
# disk space C:/



def ram_usage():
    # Get the memory details
    memory_info = psutil.virtual_memory()
    # Calculate RAM usage in percentage
    ram_usage = memory_info.percent
    return ram_usage

# Example usage
def mouse_position():
    # Get the current mouse position
    position = pyautogui.position()
    return position



def network_speed(interval=1):
    # Capture initial network stats
    net_before = psutil.net_io_counters()
    bytes_sent_before = net_before.bytes_sent
    bytes_recv_before = net_before.bytes_recv

    # Wait for a short interval
    time.sleep(interval)

    # Capture new network stats
    net_after = psutil.net_io_counters()
    bytes_sent_after = net_after.bytes_sent
    bytes_recv_after = net_after.bytes_recv

    # Calculate the difference in bytes sent and received
    bytes_sent = bytes_sent_after - bytes_sent_before
    bytes_recv = bytes_recv_after - bytes_recv_before

    # Convert to kilobytes and calculate speed in KB/s
    upload_speed_kbs = bytes_sent / 1024 / interval  # KB/s
    download_speed_kbs = bytes_recv / 1024 / interval  # KB/s

    return upload_speed_kbs, download_speed_kbs

# Example usage
if __name__ == "__main__":
    upload_speed, download_speed = get_current_network_speed_kbs()
    print(f"Upload Speed: {upload_speed:.2f} KB/s")
    print(f"Download Speed: {download_speed:.2f} KB/s")


