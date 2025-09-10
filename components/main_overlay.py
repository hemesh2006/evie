
import subprocess

from functions import *
import time
import sys
from tkintersignin import *
# Function to simulate the scrolling text effect
def hacking_scroll(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)  # Print each character
        sys.stdout.flush()  # Force the output to appear
        time.sleep(speed)  # Wait for a short time before printing the next character

# Hacking-like text
hacking_text = """
Initializing system...
Accessing database...
Loading files...
Decryption in progress...
Connection established...
Intelligent Assistant  ....
>>> _ 
"""
# Main execution



if (1):
    scripts = [r"components\text_overlay.py", r"components\gif_overlay.py",r"components\image_overlay.py",r"C:\Users\HP\Desktop\evie\components\inputoverlay.py",r"components\button.py"]
    processes = []
    for script in scripts:
        process = subprocess.Popen(["python", script])
        processes.append(process)

# Wait for all processes to complete
    for process in processes:
       process.wait()


