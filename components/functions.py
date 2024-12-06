import psutil
import pyautogui
import cv2
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import comtypes.client
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
import sys
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

def sleeep():
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

def get_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "System":
            print(f"Current system volume: {volume.GetMasterVolume() * 100}%")



# Example usage
if __name__ == "__main__":
    upload_speed, download_speed = get_current_network_speed_kbs()
    print(f"Upload Speed: {upload_speed:.2f} KB/s")
    print(f"Download Speed: {download_speed:.2f} KB/s")


import speech_recognition as sr

def mic():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something:")
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google's speech recognition API
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the recognition service.")
            return None

import requests
from bs4 import BeautifulSoup

def weather_forecast():
    url = "https://www.google.com/search?q=weather+now"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the temperature element based on class or id (this may need adjustment if Google changes their layout)
    temp_element = soup.find("span", attrs={"id": "wob_tm"})
    
    if temp_element:
        temperature = temp_element.text
        return f"{temperature}°C"
    else:
        return "Weather information not found."
def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Accept": "text/html"  # This header specifies HTML format
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the joke in the page's HTML structure
    joke_element = soup.find("p", class_="subtitle")
    
    if joke_element:
        joke = joke_element.text.strip()
        return joke
    else:
        return "No joke found."


def open_chrome(url):
    try:
        # Path to Chrome executable (adjust paths for your system)
        if sys.platform == "win32":
            # For Windows
            chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        elif sys.platform == "darwin":
            # For macOS
            chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        else:
            # For Linux
            chrome_path = "google-chrome"

        # Run the subprocess to open Chrome with the given URL
        subprocess.run([chrome_path, url], check=True)
        print(f"Opening Chrome with URL: {url}")

    except FileNotFoundError:
        print("Google Chrome is not installed or the path is incorrect.")
    except subprocess.CalledProcessError:
        print("Failed to open Chrome. Please check if Chrome is installed and the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def open_vlc():
    try:
        # Path to VLC executable (adjust paths for your system)
        if sys.platform == "win32":
            # For Windows, default VLC installation path
            vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe"
        elif sys.platform == "darwin":
            # For macOS
            vlc_path = "/Applications/VLC.app/Contents/MacOS/VLC"
        else:
            # For Linux, assume VLC is in system PATH
            vlc_path = "vlc"

        # Run the subprocess to open VLC
        subprocess.run([vlc_path], check=True)
        print("Opening VLC Media Player.")

    except FileNotFoundError:
        print("VLC is not installed or the path is incorrect.")
    except subprocess.CalledProcessError:
        print("Failed to open VLC. Please check if VLC is installed and the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def open_edge(url=""):
    try:
        # Path to Microsoft Edge executable (adjust paths for your system)
        if sys.platform == "win32":
            # For Windows, Microsoft Edge is usually installed at this location
            edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        elif sys.platform == "darwin":
            # For macOS
            edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
        else:
            # For Linux, Edge can be launched using the `microsoft-edge` command (if installed)
            edge_path = "microsoft-edge"

        # If URL is provided, open the URL in Edge; otherwise, just open Edge
        if url:
            subprocess.run([edge_path, url], check=True)
        else:
            subprocess.run([edge_path], check=True)

        print(f"Opening Microsoft Edge with URL: {url}" if url else "Opening Microsoft Edge.")

    except FileNotFoundError:
        print("Microsoft Edge is not installed or the path is incorrect.")
    except subprocess.CalledProcessError:
        print("Failed to open Microsoft Edge. Please check if Edge is installed and the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def open_vscode():
    try:
        # Path to VS Code executable (adjust paths for your system)
        if sys.platform == "win32":
            # For Windows, default installation path
            vscode_path = r"D:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        elif sys.platform == "darwin":
            # For macOS
            vscode_path = "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
        else:
            # For Linux, assume VS Code is installed and available in the system's PATH
            vscode_path = "code"

        # Run the subprocess to open VS Code
        subprocess.run([vscode_path], check=True)
        print("Opening Visual Studio Code.")

    except FileNotFoundError:
        print("Visual Studio Code is not installed or the path is incorrect.")
    except subprocess.CalledProcessError:
        print("Failed to open Visual Studio Code. Please check if VS Code is installed and the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
import subprocess

def open_windows_settings():
    try:
        # Command to open Windows Settings
        subprocess.run(["start", "ms-settings:"], check=True, shell=True)
        print("Opening Windows Settings.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open Windows Settings. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


import ctypes
import os

def empty_recycle_bin():
    try:
        # Constants from the Windows Shell API
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI = 0x00000002
        SHERB_NOSOUND = 0x00000004

        # Call the Windows Shell API to empty the Recycle Bin
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
        print("Recycle Bin emptied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


import screen_brightness_control as sbc

def set_screen_brightness(brightness):
    try:
        # Set the screen brightness to the desired value (0 to 100)
        if 0 <= brightness <= 100:
            sbc.set_brightness(brightness)
            print(f"Screen brightness set to {brightness}%.")
        else:
            print("Brightness value must be between 0 and 100.")
    except Exception as e:
        print(f"Failed to set screen brightness. Error: {e}")

import screen_brightness_control as sbc

def get_current_brightness():
    try:
        # Get the current screen brightness
        current_brightness = sbc.get_brightness(display=0)  # Display 0 for primary monitor
        print(f"Current screen brightness is {current_brightness}%")
        return current_brightness
    except Exception as e:
        print(f"Failed to get current screen brightness. Error: {e}")

# Get and print the current screen brightness



from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_system_volume(volume_level):
    try:
        # Get the audio interface for the default audio device
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 
            0, None)

        # Get the current volume interface
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # Set the volume level (between 0.0 and 1.0)
        if 0 <= volume_level <= 100:
            volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
            print(f"Volume set to {volume_level}%")
        else:
            print("Volume level must be between 0 and 100.")

    except Exception as e:
        print(f"Failed to set system volume. Error: {e}")
import winreg
import os

def set_dark_mode(enabled):
    try:
        # Registry key for dark/light mode settings
        reg_key = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        
        # Open the registry key
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
            # Set the 'AppsUseLightTheme' value
            if enabled:
                # Set to dark mode
                winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
                winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 0)
                print("Dark mode enabled.")
            else:
                # Set to light mode
                winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 1)
                winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 1)
                print("Light mode enabled.")
    except Exception as e:
        print(f"Error setting theme: {e}")

# Enable dark mode (True) or light mode (False)
import pyautogui
import time

def show_desktop():
    try:
        # Simulate the Windows + D hotkey to show the desktop
        pyautogui.hotkey('win', 'd')
        print("Desktop is now visible.")
    except Exception as e:
        print(f"Error showing desktop: {e}")
from plyer import notification

def show_notification(title: str, message: str, timeout: int = 5):
    """
    Display a desktop notification.

    Args:
        title (str): The title of the notification.
        message (str): The message content of the notification.
        timeout (int): Duration (in seconds) for the notification to appear. Default is 5 seconds.
    """
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=timeout  # Notification will disappear after this time
        )
        print("Notification displayed successfully.")
    except Exception as e:
        print(f"Error displaying notification: {e}")

# Example usage


# Call the function to show the desktop

