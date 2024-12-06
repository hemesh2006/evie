
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
if __name__ == "__main__":
    hacking_scroll(hacking_text, speed=0.05)  # Adjust the speed for your preference
    print("\n")  # Move to the next line after the scroll completes
time .sleep(1)
show_desktop()
while(1):
    try:
        create_signup_page()
        root.mainloop()
    except:
        break


if (1):
    scripts = [r"components\text_overlay.py", r"components\gif_overlay.py",r"components\image_overlay.py",r"C:\Users\HP\Desktop\evie\program_main.py",r"C:\Users\HP\Desktop\evie\components\inputoverlay.py",r"components\button.py","components\\videodetection.py","components\\desktop_block.py"]
    processes = []
    for script in scripts:
        process = subprocess.Popen(["python", script])
        processes.append(process)

# Wait for all processes to complete
    for process in processes:
       process.wait()

    print("All scripts have finished execution.ok h")
