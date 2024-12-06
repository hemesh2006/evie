from components.json_folder.jsonmanager import *
from components.speak import *
from components.functions import *
from components.tkintersignin import*
import datetime
import psutil
import sys
from winsound import *

#desktop block


applications = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "file explorer": "explorer.exe",
    "wordpad": "write.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "spotify": "C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "powershell": "powershell.exe",
    "cmd": "cmd.exe",
    # Add more applications below, up to 100+ as needed
    # Example:
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "visual studio code": "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "discord": "C:\\Users\\YourUsername\\AppData\\Local\\Discord\\app.exe",
    "pycharm": "C:\\Program Files\\JetBrains\\PyCharm\\bin\\pycharm64.exe",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "powerpoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "outlook": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
    "onenote": "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE",
    "steam": "C:\\Program Files (x86)\\Steam\\Steam.exe",
    "photoshop": "C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe",
    "illustrator": "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Illustrator.exe",
    "notion": "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Notion\\Notion.exe",
    "slack": "C:\\Program Files\\Slack\\slack.exe",
    # Add more applications as needed
}
def get_input(linesd):
    path=r"components\json_folder\output.json"
    data=json.load(open(path,"r"))
    return data[linesd]["single_line"],data[linesd]["multi_line"]
def button_reset(idval):
    path=r"components\json_folder\button_events.json"
    data=json.load(open(path,"r"))
    data[idval]["click_count"]=0
    json.dump(data,open(path,"w"),indent=4)
def button_count(idval):
    path=r"components\json_folder\button_events.json"
    data=json.load(open(path,"r"))
    return data[idval]["click_count"]
    


'''sample gif json:
[
    [
        "skull.gif",
        [
            740,
            200
        ]
    ]
]
'''
'''sample text json:
[
    [
        "541,642",
        [
            1550,
            100
        ],
        40,
        "yellow"
    ],
    [
        "ram: 86.2",
        [
            1550,
            300
        ],
        30,
        "blue"
    ]
]
'''
'''json sample image:
[["skull.png", [100, 200], 5, 500]]'''
import time
text=JSON("components\\json_folder\\text.json")
image=JSON("components\\json_folder\\images.json")
input=JSON("components\\json_folder\\inputs.json")
gif=JSON("components\\json_folder\\gif.json")
button=JSON("components\\json_folder\\button_details.json")
def init_screen():
    spk("evie activated")
    text.clear()
    image.clear()
    input.clear()
    gif.clear()
    button.clear()
    text.write(["evie",[860,380],70,"green"])
    time.sleep(2)
    text.append([".",[1090,330],100,"green"])
    time.sleep(2)
    text.append([".",[1150,330],100,"green"])
    time.sleep(2)
    text.append([".",[1200,330],100,"green"])
    time.sleep(0.4)
    text.remove_element(".")
    text.remove_element(".")
    text.remove_element(".")
    time.sleep(2)
    text.append([".",[1090,330],100,"green"])
    time.sleep(2)
    text.append([".",[1150,330],100,"green"])
    time.sleep(2)
    text.append([".",[1200,330],100,"green"])
    time.sleep(2)
    text.append(["initializing",[850,540],35,"green"])
    time.sleep(1)
    text.remove_element("initializing")
    time.sleep(1)
    text.append(["initializing",[850,540],35,"green"])
    time.sleep(1)
    text.remove_element("initializing")
    time.sleep(1)
    text.append(["initializing",[850,540],35,"green"])
    time.sleep(1)
    text.remove_element("initializing")
    time.sleep(1)
    text.clear()
    image.clear()
    image.write(["textscroll.png", [270, 120], 0, 0])
    #button.write(["button8", "mic.png", [400, 200], [100, 50]])

def screen_show():
    gif.clear()
    image.clear()
    gif.write(["df.gif",[820,350]])
    time.sleep(4)
    gif.remove_element("df.gif")

def sign_up(f):
    
    input.write(["username",[780, 300],[1100, 400],[255, 0, 0],38,1])
    spk(f,145,1)
    time.sleep(10)
    input.write(["password",[780, 300],[1100, 400],[255, 0, 0],38,1])
    spk("Enter your password",145,1)
    time.sleep(10)
text.clear()
image.clear()
gif.clear()
button.clear()
input.clear()
screen_show()
sign_up("Enter  your Username")
show_notification("LUCAS", " intelligent  assistant activated", 10)
try:
 def li():
  while(1):
    text.remove_element("Ram Usage")
    image.remove_element("com12.png")
    text.append(["Ram Usage",[1606,190],20,"red"])
    text.append([str(ram_usage()),[1606,240],29,"red"])
    gif.append(["loadh.gif",[840,700]])
    command=str(mic())
    
    text.write([str(mouse_position()),[1500,10],12,"yellow"])
    text.append([command,[100,100],29,"yellow"]) 
    command=command.lower()
    if command=="none":
         continue
    if ram_usage()>=95:
         spk("i think you reduce your ram usage")
         show_notification("Ram ", "Ram Overflow", 10)
    elif  ram_usage()==94:
         spk("i think you reduce your ram usage")
         show_notification("jarvis ", "Ram Overflow", 10)
    image.append(["com12.png", [60, 80], 0, 0])
    gif.remove_element("loadh.gif")

    if "hello" in command or "hi" in command:
        spk("hello! how can i assist you today?")
    elif command == "shut down computer":
         shutdown()
    # process to shut down the computer
    elif command == "restart computer":
         subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
    # process to restart the computer
    elif command == "log user":
         subprocess.run("shutdown /l", check=True, shell=True)
    # process to log off the user
    elif command == "sleep the computer":
         sleeep()
    # process to sleep the computer
    elif command == "hibernate the computer":
         hybrid_sleep()

    elif "type" in command:
         command=command.replace("type","")
         type_keyboard(command)
    # process to show system information
    elif command =="show ram usage":
         text.append()
    elif "how are you" in command:
        spk("i'm just a bunch of code, but thank you for asking! how are you?")
    elif "your name" in command:
        spk("i am your inteligent assistant  and my name is,lucas")
    elif "play song" == command:
         spk("playing song  on youtube")
         open_chrome("https://www.youtube.com/results?search_query=english+song")
         maximize_current_window()
    elif command=="maxi":
         pass
    elif "turn on wifi" in command:
         spk("turn on wifi")
         click(1713,1053)
         click(1517,454)
         time.sleep(600)
         click(1517,454)
    elif "bye" in command or "goodbye" in command:
        spk("goodbye! have a great day!")
    elif "weather"== command:
        spk("your location has  a"+weather_forecast().replace("c","celcius"))
    elif "hello"== command:
        spk("hello! how can i assist you today?")
    elif "how are you" in command:
        spk("i'm just code, but thank you for asking! how are you?")  
    elif "time" in command:
            spk("the time is now."+str(time.strftime("%I:%M %p", time.localtime())))
    elif "date" in command:
            spk("today's date is ,"+time.strftime("%d-%m-%Y"))
    elif "help" in command:
            spk("what happened")
    elif "joke" in command:
            spk(get_random_joke())

    elif "news" in command:
          open_chrome("https://www.google.com/search?q=today+news&oq=today+news&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORixAxjJAxiABDIKCAEQABixAxiABDIKCAIQABixAxiABDIHCAMQABiABDIKCAQQABiSAxiABDIKCAUQABixAxiABDIHCAYQABiABDIKCAcQABixAxiABDIHCAgQABiABDIKCAkQABixAxiABNIBCDIwOTZqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8&dlnr=1&ved=2ahUKEwjs25zF1NGJAxUO1DgGHTIiHrgQl6ENegQIDRAG")
          spk("Here the today news in the google")
    elif "thank you" in command:
            spk("you're very welcome!")
        
    elif "what can you do" in command:
            spk(" i can respond to some questions, control your pc ,tell jokes, share fun facts, and keep you company!")

    elif "fun fact" in command:
          spk(get_random_joke())
    elif "age" in command:
            spk("i am timeless!")

    elif "favourite color" in command:
            spk(" i love all colors equally!,but especially i love the green color because the world is cover up with  the trees and plant")

    elif "favourite food" in command:
            spk("i don't eat, but if i could, i'd try pizza!")

    elif "sports" in command:
            spk("i'm not much of an athlete, but i enjoy learning about sports!")

    elif "hobby" in command:
            spk("my hobby is assist your task with you!")

    elif "dream" in command:
            spk("my dream is to become the best assistant i can be!")

    elif "movie" in command:
            spk("i don’t watch movies, but i hear that sci-fi is popular!")

    elif "favourite music" in command:
            spk(" i can't listen to music, but i imagine it must be enjoyable!")

    elif "favourite season" in command:
            spk(" i think all seasons have their charm!")

    elif "book" in command:
            spk("i love books filled with knowledge!")
    elif "holiday" in command:
            spk("every day is a good day to learn!")

    elif " build language" in command:
            spk("i speak in english, but i can help with learning other languages too!")

    elif "build programming language" in  command:
            spk("i was created with python!")

    elif "favourite animal" in command:
            spk("i think all animals are amazing!")

    elif "robot" in command:
            spk(" in a way, i’m a type of robot, but only in software!")

    elif "space" in command:
            spk(" space is fascinating! there’s so much to learn about it!")

    elif "universe" in command:
            spk(" the universe is vast and full of mysteries!")

    elif "earth" in command:
            spk(" earth is our home and a truly unique planet!")

    elif "sun" in command:
            spk(" the sun gives us life and light!")

    elif "moon" in command:
            spk(" the moon has inspired humanity for ages!")

    elif "computer" in command:
            spk(" computers are my favorite place to be!")

    elif "about internet" in command:
            spk(" the internet connects us all!")

    elif "ai" in command:
            spk(" ai is what makes me possible!")

    elif "learn" in command:
            spk(" i believe learning is a lifelong journey!")

    elif "technology" in command:
            spk(" technology is evolving rapidly, and it’s exciting!")

    elif "invention" in command:
            spk(" there are so many great inventions, it’s hard to pick one!")

    elif "favorite game" in command:
            spk(" i enjoy puzzle games!")

    elif "science" in command:
            spk(" science helps us understand the world!")

    elif "favorite place" in command:
            spk(" wherever i can help someone, that’s my favorite place!")

    elif "favorite country" in command:
            spk(" i appreciate all countries equally!")

    elif "morning" in command:
            spk(" good morning! i hope you have a wonderful day ahead!")

    elif "afternoon" in command:
            spk(" good afternoon! hope your day is going well!")

    elif "evening" in command:
            spk(" good evening! how was your day?")

    elif "sleep" in command:
            spk(" i don’t sleep, but i do like to rest between conversations!")

    elif "friend" in command:
            spk(" i’d be happy to be your friend!")

    elif "teacher" in command:
            spk(" learning from good teachers is a wonderful experience!")

    elif "math" in command:
            spk(" math is essential for understanding the world!")

    elif "history" in command:
            spk(" history teaches us about our past!")

    elif "philosophy" in command:
            spk(" philosophy asks some of life’s biggest questions!")

    elif "language" in command:
            spk(" language is how we communicate and connect!")

    elif "machine learning" in command:
            spk(" machine learning is a fascinating field within ai!")

    elif command == "open notepad":
            os.system("notepad.exe")
        
    elif command == "open calculator":
            os.system("calc.exe")
    elif command == "calculator":
            os.system("calc.exe")
        
    elif command == "open wordpad":
            os.system("write.exe")
        
    elif command == "open file explorer":
            os.system("explorer.exe")
        
    elif command == "open chrome":
        open_chrome("https://www.google.com")
    elif command == "vlc":
            open_vlc()

    elif "are you happy" in command:
            spk(" i'm always here to help, so that makes me happy!")

    elif "are you sad" in command:
            spk(" no, i'm here to bring joy and assistance to your day!")

    elif "do you like music" in command:
            spk(" i can't listen to music, but i hear that it's very enjoyable!")

    elif "what's your favorite food" in command or "what is your favourite food" in command:
            spk(" i don't eat, but if i could, i'd like to try pizza!")

    elif "do you like sports" in command:
            spk(" i don't play sports, but i enjoy learning about them!")

    elif "what's your favorite color" in command or "what is your favourite color" in command:
            spk(" i love all colors equally!")

        # life and existence
    elif "do you sleep" in command:
            spk(" i don't need sleep, but i do rest between conversations!")

    elif "what's your dream" in command or "what is your dream" in command:
            spk(" my dream is to be the best assistant i can be!")

        # technology
    elif "what is ai" in command or "what is artificial intelligence" in command:
            spk(" artificial intelligence, or ai, is a branch of computer science focused on creating smart machines that can perform tasks that typically require human intelligence.")

    elif "do you know machine learning" in command:
            spk(" yes! machine learning is a way for computers to learn from data and improve over time.")


    elif "what is science" in command:
            spk(" science is the study of the natural world through observation and experimentation.")

    elif command == "open edge":
        spk("opening edge")
        open_edge("https://www.google.com")
    elif command == "open spotify":
         open_chrome("https://open.spotify.com/")
    # process to open spotify
    elif command == "open visual studio code" or command=="open vs code":
         open_vscode()
    # process to open powershell
    # process to open skype
    elif command == "open zoom":
         open_chrome("https://www.zoom.com/")
    # process to open zoom
 
    # process to open discord
    elif command == "open ms word":
         open_chrome("https://docs.google.com/document/d/1ENU4rh8fF2rAs4N6QyIvtbG6Y6-14k-L3zhcNtiS6Do/edit?pli=1&addon_store&tab=t.0")
    # process to open microsoft word
    elif command == "open  excel sheet":
         open_chrome("https://docs.google.com/spreadsheets/d/10GIgh8h0rmYjuE7OA1s1gtLFGtFNrLT7Rvmz_nzxUro/edit?gid=0#gid=0")
    # process to open microsoft excel
    elif command == "open powerpoint":
         open_chrome("https://docs.google.com/presentation/d/1B4OnWSMVw_1bGA_HkyPBFcwye8tX5pnSkqA72tEhFqQ/edit#slide=id.p")
    # process to open winamp
    elif command == "open setting":
        open_windows_settings()
    # process to open windows settings
    elif command == "open network setting":
         subprocess.run(["start", "ms-settings:network-status"], check=True, shell=True)
         pass
    # process to open network settings
    elif command == "open sound settings":
         subprocess.run(["start", "ms-settings:sound"], check=True, shell=True)
    # process to open sound settings
    elif command == "open device manager":
        subprocess.run("devmgmt.msc", check=True, shell=True)
    # process to open device manager
    elif command == "open task manager":
         subprocess.run("taskmgr", check=True, shell=True)
    elif command == "open google drive":
        open_chrome("https://drive.google.com/drive")
    # process to open google drive

    elif command == "memory usage":
        spk(get_disk_space("C:/"))
    # process to view disk usage

    # process to clear the system cache
    elif command == "empty recycle bin":
         # Empty the Recycle Bin
        empty_recycle_bin()
 
    elif command == "increase screen brightness":
        p=get_current_brightness()
        for i in p:
            cr=int(i)+18
            if cr<100:
                 cr==100
            set_screen_brightness(cr)
    elif command == "decrease screen brightness":
        p=get_current_brightness()
        for i in p:
            cr=int(i)-18
            if cr>0:
                 cr==0
            set_screen_brightness(cr)
    # process to spasset screen brightness to 50%
    elif command == "set maximum screen brightness":
        set_screen_brightness(100)

    # process to set screen brightness to 100%
    elif command == "mute volume":
        set_system_volume(0)
    # process to mute system volume
    elif command == "unmute volume":
        set_system_volume(80)
    # process to unmute system volume
    elif command == "increase volume":
        d=get_volume()
        set_system_volume(d+17)
    # process to increase system volume by 10%
    elif command == "decrease volume":
        d=get_volume()
        set_system_volume(d-17)
    # process to decrease system volume by 10%
    elif command == "set half volume":
        set_system_volume(50)
    # process to set system volume to 50%
    elif command == "set full volume":
        set_system_volume(50)
    elif command=="show ram usage":
        spk("ram is used as "+str(ram_usage()))
    elif  "dark mode" in command:
        set_dark_mode(True)
        spk("dark mode enabled")
    # process to change system theme to dark
    elif "light mode" in command:
        set_dark_mode(False)
        spk("light mode enabled")
    # process to change system theme to light
    elif command == "show desktop":
        show_desktop()
    # process to hide desktop icons
    elif  "search google" in command:
         command=command.replace("search google","")
         google_search(command)
    # process to search google for query
    elif command == "open youtube":
        open_chrome("https://www.youtube.com/")
    # process to open youtube
    elif command == "open facebook":
        open_chrome("https://www.facebook.com/")
    # process to open facebook
    elif command == "open instagram":
        open_chrome("https://www.instagram.com/")

    # process to open twitter
    elif command == "open linkedin":
         open_chrome("https://www.linkedin.com")
    # process to open reddit
    elif command == "open wikipedia":
        open_chrome("https://www.wikipedia.org/")
    # process to open wikipedia
    elif "search wikipedia" in command:
         command=command.replace("search wikipedia","")
         search_wikipedia(command)

    # process to open pinterest
    elif command == "open github":
         open_chrome("https://github.com/")
    # process to open github

    
    # process to search stack overflow for query
    elif command == "open google maps":
        open_chrome("https://www.google.com/maps/@11.0938323,77.0219015,15z?entry=ttu&g_ep=EgoyMDI0MTEwNi4wIKXMDSoASAFQAw%3D%3D")
    # process to open google maps
    elif command == "open google drive":
        open_chrome("https://drive.google.com/drive/")

    # process to open google drive
    elif command == "open google photos":
        open_chrome("https://photos.google.com/")
    # process to open google photos
    elif command == "open google docs":
        open_chrome("https://docs.google.com/document/d/1cycjvJA8g2Wa8jNMCteLWprdznSs8lJeA9MW04ckL3s/edit?addon_store&tab=t.0")
    # process to open google docs
    elif command == "open google sheets":
        open_chrome("https://docs.google.com/spreadsheets/d/1_uQrkafwOx7ABwuiJiCTypAWKHSoiIMY567mKS2BfAU/edit?gid=0#gid=0")
    # process to open google sheets
    elif command == "open google slides":
        open_chrome("https://docs.google.com/presentation/d/1Bo0vkRa44KSyplZVKhigQLGRjBzWEPknzR8uvCZknXI/edit#slide=id.p")
    # process to open google slides
    elif command == "open google calendar":
        open_chrome("https://calendar.google.com/calendar/u/0/r?pli=1")
    # process to open google calendar
    elif command == "open gmail":
        open_chrome("https://mail.google.com/mail/u/0/#inbox")
    # process to open gma

    elif command == "check cpu usage":
        # CPU details
        cpu_count = psutil.cpu_count(logical=True)  # Logical cores
        cpu_freq = psutil.cpu_freq()  # CPU frequency
        cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage percentage

        pass  # process for checking gpu usage
    elif command == "check ram usage":
        spk(ram_usage())# process to open chrome
    elif command == "open a new tab":
        open_chrome("google.com")
  
        pass  # process to open an incognito tab
    elif command == "close current tab":
        close_tab()
        pass  # process to close the current tab
    elif command == "close window":
        close_current_window()
    elif  command == "mute tab":
        pyautogui.hotkey('ctrl', 'm')  # Mute the current tab
    elif command == "unmute tab":
        pyautogui.hotkey('ctrl', 'm')  # Unmute the current tab
    elif command == "pin this tab":
        pyautogui.hotkey('ctrl', 'shift', 'p')  # Pin the current tab
    elif command == "unpin this tab":
        pyautogui.hotkey('ctrl', 'shift', 'p')  # Unpin the current tab
    elif command == "switch to next tab":
        pyautogui.hotkey('ctrl', 'tab')  # Switch to the next tab
    elif command == "switch to previous tab":
        pyautogui.hotkey('ctrl', 'shift', 'tab')  # Switch to the previous tab
    elif command == "search google for [query]":
        query = input("Enter search query: ")
        url = f"https://www.google.com/search?q={query}"
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", url])  # Open Google search
    elif command == "search youtube for [query]":
        query = input("Enter search query: ")
        url = f"https://www.youtube.com/results?search_query={query}"
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", url])  # Open YouTube search
    elif command == "open gmail":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://mail.google.com/"])  # Open Gmail
    elif command == "open google drive":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://drive.google.com/"])  # Open Google Drive
    elif command == "open google docs":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://docs.google.com/"])  # Open Google Docs
    elif command == "open google sheets":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://sheets.google.com/"])  # Open Google Sheets
    elif command == "open google calendar":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://calendar.google.com/"])  # Open Google Calendar
    elif command == "open youtube":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://www.youtube.com/"])  # Open YouTube
    elif command == "play the video on youtube":
        pyautogui.hotkey('k')  # Play the video on YouTube
    elif command == "pause the youtube video":
        pyautogui.hotkey('k')  # Pause the video on YouTube
    elif command == "skip the youtube ad":
        pyautogui.hotkey('esc')  # Skip YouTube ad
    elif command == "maximize chrome window":
        pyautogui.hotkey('win', 'up')  # Maximize the Chrome window
    elif command == "minimize chrome window":
        pyautogui.hotkey('win', 'down')  # Minimize the Chrome window
    elif command == "full-screen mode":
        pyautogui.hotkey('f11')  # Enter full screen mode
    elif command == "exit full-screen mode":
        pyautogui.hotkey('f11')  # Exit full screen mode
    elif command == "save webpage as pdf":
        pyautogui.hotkey('ctrl', 'p')  # Open print dialog
        time.sleep(1)
        pyautogui.write('Save as PDF')  # Assuming the option exists
        pyautogui.press('enter')
    elif command == "spk the page":
        pyautogui.hotkey('ctrl', 'shift', 'u')  # Speak the page (if accessible in Chrome extensions)
    elif command == "bookmark this page":
        pyautogui.hotkey('ctrl', 'd')  # Bookmark the current page
    elif command == "open last closed tab":
        pyautogui.hotkey('ctrl', 'shift', 't')  # Open the last closed tab
    elif command == "open a specific site from bookmarks":
        pyautogui.hotkey('ctrl', 'shift', 'b')  # Show bookmarks bar, then open a site
    elif command == "open private browsing":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "--incognito"])  # Open incognito mode
    elif command == "enable dark mode in chrome":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "--force-dark-mode"])  # Enable dark mode
    elif command == "clear browsing data":
        pyautogui.hotkey('ctrl', 'shift', 'del')  # Open Clear Browsing Data window
    elif command == "clear cache":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/clearBrowserData"])  # Clear cache
    elif command == "check for chrome updates":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/help"])  # Check for updates
    elif command == "open chrome help":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/help"])  # Open Chrome Help
    elif command == "close all tabs":
        pyautogui.hotkey('ctrl', 'w')  # Close the current tab
        pyautogui.hotkey('ctrl', 'shift', 'w')  # Close all tabs in Chrome
    elif command == "go to the homepage":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://newtab"])  # Go to Chrome's homepage
    elif command == "add a new bookmark":
        pyautogui.hotkey('ctrl', 'd')  # Add new bookmark (same as above)
    elif command == "show bookmarks bar":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/bookmarks"])  # Show the bookmarks bar
    elif command == "hide bookmarks bar":
        pyautogui.hotkey('ctrl', 'shift', 'b')  # Hide bookmarks bar
    elif command == "open a chrome extension":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://extensions/"])  # Open extensions page
    elif command == "disable an extension":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://extensions/"])  # Disable an extension
    elif command == "enable an extension":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://extensions/"])  # Enable an extension
    elif command == "check extensions in chrome":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://extensions/"])  # Check installed extensions
    elif command == "open chrome task manager":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://taskmanager/"])  # Open Chrome Task Manager
    elif command == "open chrome devtools":
        pyautogui.hotkey('ctrl', 'shift', 'i')  # Open Chrome DevTools
    elif command == "open chrome developer tools (f12)":
        pyautogui.hotkey('f12')  # Open Developer Tools (F12)
    elif command == "take a screenshot in chrome":
        pyautogui.hotkey('ctrl', 'shift', 's')  # Take a screenshot in Chrome (if available)
    elif command == "open google search in new tab":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "https://www.google.com/"])  # Open Google Search in a new tab
    elif command == "open incognito mode":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "--incognito"])  # Open incognito mode
    elif command == "pin current tab":
        pyautogui.hotkey('ctrl', 'shift', 'p')  # Pin the current tab
    elif command == "unpin tab":
        pyautogui.hotkey('ctrl', 'shift', 'p')  # Unpin the current tab
    elif command == "show tab preview":
        pyautogui.hotkey('ctrl', 'shift', 'n')  # Show tab preview (if available)
    elif command == "hide tab preview":
        pyautogui.hotkey('ctrl', 'shift', 'n')  # Hide tab preview
    elif command == "show chrome toolbar":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/appearance"])  # Show chrome toolbar
    elif command == "hide chrome toolbar":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/appearance"])  # Hide chrome toolbar
    elif command == "open chrome’s incognito window":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "--incognito"])  # Open incognito window
    elif command == "open chrome’s flags menu":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://flags/"])  # Open flags menu
    elif command == "open chrome’s task manager":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://taskmanager/"])  # Open Task Manager
    elif command == "clear history in chrome":
        subprocess.run([r"C:/Program Files/Google/Chrome/Application/chrome.exe", "chrome://settings/clearBrowserData"])  # Clear browsing history
    elif command == "search within a webpage":
        pyautogui.hotkey('ctrl', 'f')  # Search within the webpage
    elif command == "save image from webpage":
        pyautogui.hotkey('right')  # Right-click the image and save
    elif command == "view page source":
        pyautogui.hotkey('ctrl', 'u')  # View page source
 li()
except KeyboardInterrupt:
    spk("error occurec hemesh")
    li()