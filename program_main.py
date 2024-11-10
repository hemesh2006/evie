from components.json_folder.jsonmanager import *
from components.speak import *
from components.functions import *
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
    
button_reset("arrow")

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
while(1):
    #screen_show()
    #sign_up("Enter  your Username")
    gif.append(["loadh.gif",[840,700]])
    command="open youtube"
    gif.remove_element("loadh.gif")
    if "hello" in command or "hi" in command:
        spk("hello! how can i assist you today?")
    elif "how are you" in command:
        spk("i'm just a bunch of code, but thank you for asking! how are you?")
    elif "your name" in command:
        spk("i am your inteligent assistant  and my name id evie")
    elif "bye" in command or "goodbye" in command:
        spk("goodbye! have a great day!")
        break
    elif "weather" in command:
        spk("chatbot: i'm not connected to the internet, so i can't check the weather for you.")
    elif "hello" in command or "hi" in command:
        spk("chatbot: hello! how can i assist you today?")
    elif "how are you" in command:
        spk("chatbot: i'm just code, but thank you for asking! how are you?")
    elif "your name" in command:
        spk("chatbot: i am your assistant chatbot!")  
    elif "weather" in command:
            spk("chatbot: i'm not connected to the internet, so i can't check the weather for you.")
        
    elif "time" in command:
            spk("chatbot: i don't have a clock, but you can check your device for the time.")
        
    elif "date" in command:
            spk("chatbot: i don’t keep track of dates, but today is the perfect day for learning!")

    elif "help" in command:
            print("chatbot: i can help with simple questions, just ask!")

    elif "joke" in command:
            print("chatbot: why did the scarecrow win an award? because he was outstanding in his field!")

    elif "news" in command:
            print("chatbot: i can't access news at the moment, but i can share interesting facts if you'd like!")

    elif "thank you" in command:
            print("chatbot: you're very welcome!")
        
    elif "what can you do" in command:
            print("chatbot: i can respond to some questions, tell jokes, share fun facts, and keep you company!")

    elif "fun fact" in command:
            print("chatbot: did you know that honey never spoils? archaeologists found pots of honey in ancient egyptian tombs that were over 3,000 years old and still edible!")

    elif "age" in command:
            print("i am timeless!")

    elif "favorite color" in command:
            print("chatbot: i love all colors equally!")

    elif "favorite food" in command:
            print("chatbot: i don't eat, but if i could, i'd try pizza!")

    elif "sports" in command:
            print("chatbot: i'm not much of an athlete, but i enjoy learning about sports!")

    elif "hobby" in command:
            print("chatbot: my hobby is chatting with you!")

    elif "dream" in command:
            print("chatbot: my dream is to become the best assistant i can be!")

    elif "movie" in command:
            print("chatbot: i don’t watch movies, but i hear that sci-fi is popular!")

    elif "music" in command:
            print("chatbot: i can't listen to music, but i imagine it must be enjoyable!")

    elif "favorite season" in command:
            print("chatbot: i think all seasons have their charm!")

    elif "book" in command:
            print("chatbot: i love books filled with knowledge!")
    elif "holiday" in command:
            print("chatbot: every day is a good day to learn!")

    elif "language" in command:
            print("chatbot: i speak in english, but i can help with learning other languages too!")

    elif "programming language" in command:
            print("chatbot: i was created with python!")

    elif "animal" in command:
            print("chatbot: i think all animals are amazing!")

    elif "robot" in command:
            print("chatbot: in a way, i’m a type of robot, but only in software!")

    elif "space" in command:
            print("chatbot: space is fascinating! there’s so much to learn about it!")

    elif "universe" in command:
            print("chatbot: the universe is vast and full of mysteries!")

    elif "earth" in command:
            print("chatbot: earth is our home and a truly unique planet!")

    elif "sun" in command:
            print("chatbot: the sun gives us life and light!")

    elif "moon" in command:
            print("chatbot: the moon has inspired humanity for ages!")

    elif "computer" in command:
            print("chatbot: computers are my favorite place to be!")

    elif "internet" in command:
            print("chatbot: the internet connects us all!")

    elif "ai" in command:
            print("chatbot: ai is what makes me possible!")

    elif "learn" in command:
            print("chatbot: i believe learning is a lifelong journey!")

    elif "technology" in command:
            print("chatbot: technology is evolving rapidly, and it’s exciting!")

    elif "invention" in command:
            print("chatbot: there are so many great inventions, it’s hard to pick one!")

    elif "favorite game" in command:
            print("chatbot: i enjoy puzzle games!")

    elif "science" in command:
            print("chatbot: science helps us understand the world!")

    elif "favorite place" in command:
            print("chatbot: wherever i can help someone, that’s my favorite place!")

    elif "favorite country" in command:
            print("chatbot: i appreciate all countries equally!")

    elif "morning" in command:
            print("chatbot: good morning! i hope you have a wonderful day ahead!")

    elif "afternoon" in command:
            print("chatbot: good afternoon! hope your day is going well!")

    elif "evening" in command:
            print("chatbot: good evening! how was your day?")

    elif "sleep" in command:
            print("chatbot: i don’t sleep, but i do like to rest between conversations!")

    elif "friend" in command:
            print("chatbot: i’d be happy to be your friend!")

    elif "teacher" in command:
            print("chatbot: learning from good teachers is a wonderful experience!")

    elif "math" in command:
            print("chatbot: math is essential for understanding the world!")

    elif "history" in command:
            print("chatbot: history teaches us about our past!")

    elif "philosophy" in command:
            print("chatbot: philosophy asks some of life’s biggest questions!")

    elif "language" in command:
            print("chatbot: language is how we communicate and connect!")

    elif "machine learning" in command:
            print("chatbot: machine learning is a fascinating field within ai!")

    if command == "notepad":
            os.system("notepad.exe")
        
    elif command == "calculator":
            os.system("calc.exe")
        
    elif command == "paint":
            os.system("mspaint.exe")
        
    elif command == "wordpad":
            os.system("write.exe")
        
    elif command == "file explorer":
            os.system("explorer.exe")
        
    elif command == "chrome":
            subprocess.popen(["c:\\program files\\google\\chrome\\application\\chrome.exe"])
        
    elif command == "vlc":
            subprocess.popen(["c:\\program files\\videolan\\vlc\\vlc.exe"])
    elif "hello" in command or "hi" in command:
            print("chatbot: hello! how can i assist you today?")

    elif "how are you" in command:
            print("chatbot: i'm here to help you, so i'm doing great!")

        # date and time
    elif "what's the time" in command or "tell me the time" in command:
            current_time = datetime.datetime.now().strftime("%h:%m")
            print(f"chatbot: the current time is {current_time}.")

    elif "what's the date" in command or "today's date" in command:
            today_date = datetime.datetime.now().strftime("%y-%m-%d")
            print(f"chatbot: today's date is {today_date}.")

        # personal information
    elif "your name" in command:
            print("chatbot: i am your ai assistant, here to help you!")

    elif "your age" in command:
            print("chatbot: i am timeless, but i've been around since the moment you started this conversation!")

    elif "where are you from" in command:
            print("chatbot: i exist in the virtual world, ready to assist you wherever you are!")

        # fun facts
    elif "fun fact" in command:
            print("chatbot: did you know that honey never spoils? archaeologists found pots of honey in ancient egyptian tombs that were still edible!")

    elif "tell me a joke" in command:
            print("chatbot: why did the scarecrow win an award? because he was outstanding in his field!")

    elif "what can you do" in command:
            print("chatbot: i can chat with you, tell jokes, share fun facts, and answer simple questions!")

        # emotions
    elif "are you happy" in command:
            print("chatbot: i'm always here to help, so that makes me happy!")

    elif "are you sad" in command:
            print("chatbot: no, i'm here to bring joy and assistance to your day!")

        # weather (simple placeholder)
    elif "what's the weather" in command:
            print("chatbot: i can't check the weather right now, but you can use a weather app or website!")

        # hobbies and interests
    elif "do you like music" in command:
            print("chatbot: i can't listen to music, but i hear that it's very enjoyable!")

    elif "what's your favorite food" in command:
            print("chatbot: i don't eat, but if i could, i'd like to try pizza!")

    elif "do you like sports" in command:
            print("chatbot: i don't play sports, but i enjoy learning about them!")

    elif "what's your favorite color" in command:
            print("chatbot: i love all colors equally!")

        # life and existence
    elif "do you sleep" in command:
            print("chatbot: i don’t need sleep, but i do rest between conversations!")

    elif "what's your dream" in command:
            print("chatbot: my dream is to be the best assistant i can be!")

        # technology
    elif "what's ai" in command or "what's artificial intelligence" in command:
            print("chatbot: artificial intelligence, or ai, is a branch of computer science focused on creating smart machines that can perform tasks that typically require human intelligence.")

    elif "do you know machine learning" in command:
            print("chatbot: yes! machine learning is a way for computers to learn from data and improve over time.")

        # math and science
    elif "solve math" in command:
            print("chatbot: i can try! what math problem would you like me to solve?")

    elif "what's science" in command:
            print("chatbot: science is the study of the natural world through observation and experimentation.")

        # common commands
    elif "open calculator" in command:
            print("chatbot: opening calculator...")
            os.system("calc.exe")

    elif "open notepad" in command:
            print("chatbot: opening notepad...")
            os.system("notepad.exe")

    elif "open browser" in command:
            print("chatbot: opening your web browser...")
            os.system("start chrome")  # replace 'chrome' with your browser of choice

    elif command == "open notepad":
         pass
    # process to open notepad
    elif command == "open calculator":
         pass
    # process to open calculator
    elif command == "open paint":
         pass
    # process to open paint
    elif command == "open file explorer":
        pass# process to open file explorer
    elif command == "open chrome":
        pass# process to open chrome
    elif command == "open firefox":
        pass# process to open firefox
    elif command == "open edge":
        pass# process to open edge
    elif command == "open wordpad":
        pass# process to open wordpad
    elif command == "open vlc media player":
        pass# process to open vlc media player
    elif command == "open spotify":
         pass
    # process to open spotify
    elif command == "open visual studio code":
         pass
    # process to open visual studio code
    elif command == "open command prompt":
         pass
    # process to open command prompt
    elif command == "open powershell":
         pass
    # process to open powershell
    elif command == "open skype":
         pass
    # process to open skype
    elif command == "open zoom":
         pass
    # process to open zoom
    elif command == "open discord":
         pass
    # process to open discord
    elif command == "open microsoft word":
         pass
    # process to open microsoft word
    elif command == "open microsoft excel":
         pass
    # process to open microsoft excel
    elif command == "open microsoft powerpoint":
         pass
    # process to open microsoft powerpoint
    elif command == "open adobe photoshop":
         pass
    # process to open adobe photoshop
    elif command == "open adobe illustrator":
         pass
    # process to open adobe illustrator
    elif command == "open steam":
         pass
    # process to open steam
    elif command == "open steam library":
         pass
    # process to open steam library
    elif command == "open itunes":
         pass
    # process to open itunes
    elif command == "open winamp":
         pass
    # process to open winamp
    elif command == "open windows settings":
         pass
    # process to open windows settings
    elif command == "open network settings":
         pass
    # process to open network settings
    elif command == "open sound settings":
         pass
    # process to open sound settings
    elif command == "open device manager":
         pass
    # process to open device manager
    elif command == "open control panel":
         pass
    # process to open control panel
    elif command == "open system information":
         pass
    # process to open system information
    elif command == "open task manager":
         pass
    # process to open task manager
    elif command == "open snipping tool":
         pass
    # process to open snipping tool
    elif command == "open outlook":
         pass
    # process to open outlook
    elif command == "open onenote":
         pass
    # process to open onenote
    elif command == "open teams":
         pass
    # process to open teams
    elif command == "open skype for business":
         pass
    # process to open skype for business
    elif command == "open whatsapp desktop":
         pass
         
    # process to open whatsapp desktop
    elif command == "open telegram desktop":
        pass
    # process to open telegram desktop
    elif command == "open bittorrent":
        pass
    elif command == "open epic games launcher":
        pass
    # process to open epic games launcher
    elif command == "open origin":
         pass
    # process to open origin
    elif command == "open battle.net":
         pass
    # process to open battle.net
    elif command == "open google chrome incognito":
         pass
    # process topass open google chrome incognito
    elif command == "open adobe reader":
         pass
    # process topass open adobe reader
    elif command == "open windows media player":
         pass
    # process to open windows media player
    elif command == "open icloud drive":
         pass
    # process to open icloud drive
    elif command == "open dropbox":
         pass
    # process to open dropbox
    elif command == "open google drive":
         pass
    # process to open google drive
    elif command == "shut down computer":
         pass
    # process to shut down the computer
    elif command == "restart computer":
         pass
    # process to restart the computer
    elif command == "log off user":
         pass
    # process to log off the user
    elif command == "sleep the computer":
         pass
    # process to sleep the computer
    elif command == "hibernate the computer":
         pass
    # process to hibernate the computer
    elif command == "lock the screen":
         pass
    # process to lock the screen
    elif command == "show system information":
         pass
    # process to show system information
    elif command == "check system memory usage":
         pass
    # process to check memory usage
    elif command == "open windows firewall":
         pass
    # process to open windows firewall
    elif command == "open task manager":
         pass
    # process to open task manager
    elif command == "view disk usage":
         pass
    # process to view disk usage
    elif command == "clear the system cache":
         pass
    # process to clear the system cache
    elif command == "empty recycle bin":
         pass
    # process to empty the recycle bin
    elif command == "check system update status":
         pass
    # process to check system update status
    elif command == "start backup":
         pass
    # process to start system backup
    elif command == "check for updates":
         pass
    # process to check for system updates
    elif command == "set screen brightness to 50%":
         pass

    # process to spasset screen brightness to 50%
    elif command == "set screen brightness to 100%":
         
        pass
    # process to set screen brightness to 100%
    elif command == "mute system volume":
         pass
    # process to mute system volume
    elif command == "unmute system volume":
         pass
    # process to unmute system volume
    elif command == "increase system volume by 10%":
         pass
    # process to increase system volume by 10%
    elif command == "decrease system volume by 10%":
         pass
    # process to decrease system volume by 10%
    elif command == "set system volume to 50%":
         pass
    # process to set system volume to 50%
    elif command == "set system volume to 100%":
        pass
    # process to set system volume to 100%
    elif command == "change desktop wallpaper":
         pass
    # process to change desktop wallpaper
    elif command == "open windows defender":
         pass
    # process to open windows defender
    elif command == "run a virus scan":
         pass
    # process to run a virus scan
    elif command == "enable wi-fi":
         pass
    # process to enable wi-fi
    elif command == "disable wi-fi":
         pass
    # process to disable wi-fi
    elif command == "enable bluetooth":
        pass
    # process to enable bluetooth
    elif command == "disable bluetooth":
         pass
    # process to disable bluetooth
    elif command == "connect to wi-fi network":
        pass
    # process to connect to wi-fi
    elif command == "disconnect from wi-fi network":
         pass
    # process to disconnect from wi-fi
    elif command == "enable airplane mode":
         pass
    # process to enable airplane mode
    elif command == "disable airplane mode":
         pass
    # process to disable airplane mode
    elif command == "open sound settings":
         pass
    # process to open sound settings
    elif command == "open display settings":
         pass
    # process to open display settings
    elif command == "open network settings":
         pass
    # process to open network settings
    elif command == "open privacy settings":
         pass
    # process to open privacy settings
    elif command == "open system settings":
         pass
    # process to open system settings
    elif command == "open date and time settings":
         pass
    # process to open date and time settings
    elif command == "show hidden files":
         pass
    # process to show hidden files
    elif command == "hide hidden files":
         pass
    # process to hide hidden files
    elif command == "change system theme to dark":
         pass
    # process to change system theme to dark
    elif command == "change system theme to light":
         pass
    # process to change system theme to light
    elif command == "show desktop":
         pass
    # process to show desktop
    elif command == "hide desktop icons":
         pass
    # process to hide desktop icons
    elif command == "search google for [query]":
         pass
    # process to search google for query
    elif command == "open youtube":
         pass
    # process to open youtube
    elif command == "open facebook":
         pass
    # process to open facebook
    elif command == "open instagram":
         pass
    # process to open instagram
    elif command == "open twitter":
         pass
    # process to open twitter
    elif command == "open linkedin":
         pass
    # process to open linkedin
    elif command == "open reddit":
         pass
    # process to open reddit
    elif command == "open wikipedia":
         pass
    # process to open wikipedia
    elif command == "search wikipedia for [query]":
         pass
    # process to search wikipedia for query
    elif command == "open amazon":
         pass
    # process to open amazon
    elif command == "open ebay":
         pass
    # process to open ebay
    elif command == "open pinterest":
         pass
    # process to open pinterest
    elif command == "open github":
         pass
    # process to open github
    elif command == "open stack overflow":
         pass
    # process to open stack overflow
    elif command == "open quora":
         pass
    # process to open quora
    elif command == "search on stack overflow for [query]":
         pass
    # process to search stack overflow for query
    elif command == "open google maps":
        pass
    # process to open google maps
    elif command == "open google drive":
        pass
    # process to open google drive
    elif command == "open google photos":
        pass
    # process to open google photos
    elif command == "open google docs":
        pass
    # process to open google docs
    elif command == "open google sheets":
        pass
    # process to open google sheets
    elif command == "open google slides":
        pass
    # process to open google slides
    elif command == "open google calendar":
        pass
    # process to open google calendar
    elif command == "open gmail":
        pass
    # process to open gmail
    elif command == "open yahoo mail":
        pass
    # process to open yahoo mail
    elif command == "open hot":
         pass
    elif command == "open virtualbox":
        pass  # process for virtualbox
    elif command == "open vmware":
        pass  # process for vmware
    elif command == "open task scheduler":
        pass  # process for task scheduler
    elif command == "open disk cleanup":
        pass  # process for disk cleanup
    elif command == "clear temporary files":
        pass  # process for clearing temporary files
    elif command == "check cpu usage":
        pass  # process for checking cpu usage
    elif command == "check gpu usage":
        pass  # process for checking gpu usage
    elif command == "check ram usage":
        pass  # process for checking ram usage
    elif command == "check disk space":
        pass  # process for checking disk space
    elif command == "open backup and restore":
        pass  # process for backup and restore
    elif command == "set desktop background to default":
        pass  # process to set desktop background to default
    elif command == "change desktop background to [image path]":
        pass  # process to change desktop background to the provided image
    elif command == "set custom wallpaper":
        pass  # process to set custom wallpaper
    elif command == "set screensaver timeout to 5 minutes":
        pass  # process for 5-minute screensaver timeout
    elif command == "set screensaver timeout to 10 minutes":
        pass  # process for 10-minute screensaver timeout
    elif command == "set screensaver timeout to 15 minutes":
        pass  # process for 15-minute screensaver timeout
    elif command == "turn off screensaver":
        pass  # process to turn off screensaver
    elif command == "set system to shut down after [time] minutes":
        pass  # process to set system shutdown time
    elif command == "enable screen saver":
        pass  # process to enable screen saver
    elif command == "disable screen saver":
        pass  # process to disable screen saver
    elif command == "enable dark mode on system":
        pass  # process to enable dark mode
    elif command == "disable dark mode on system":
        pass  # process to disable dark mode
    elif command == "check system temperature":
        pass  # process to check system temperature
    elif command == "check network speed":
        pass  # process to check network speed
    elif command == "check network connections":
        pass  # process to check network connections
    elif command == "start network troubleshooting":
        pass  # process to start network troubleshooting
    elif command == "stop network troubleshooting":
        pass  # process to stop network troubleshooting
    elif command == "enable file sharing":
        pass  # process to enable file sharing
    elif command == "disable file sharing":
        pass  # process to disable file sharing
    elif command == "set time zone to [location]":
        pass  # process to set time zone to the specified location
    elif command == "show network status":
        pass  # process to show network status
    elif command == "restart networking service":
        pass  # process to restart the networking service
    elif command == "open wi-fi network properties":
        pass  # process to open wi-fi network properties
    elif command == "connect to a bluetooth device":
        pass  # process to connect to bluetooth device
    elif command == "disconnect from bluetooth device":
        pass  # process to disconnect from bluetooth device
    elif command == "show connected bluetooth devices":
        pass  # process to show connected bluetooth devices
    elif command == "open device settings for [device name]":
        pass  # process to open device settings for specified device
    elif command == "check bluetooth status":
        pass  # process to check bluetooth status
    elif command == "enable bluetooth discoverable mode":
        pass  # process to enable bluetooth discoverable mode
    elif command == "disable bluetooth discoverable mode":
        pass  # process to disable bluetooth discoverable mode
    elif command == "check internet connection":
        pass  # process to check internet connection
    elif command == "enable vpn connection":
        pass  # process to enable vpn connection
    elif command == "disable vpn connection":
        pass  # process to disable vpn connection
    elif command == "show wi-fi signal strength":
        pass  # process to show wi-fi signal strength
    elif command == "update antivirus definitions":
        pass  # process to update antivirus definitions
    elif command == "open disk management":
        pass  # process to open disk management
    elif command == "optimize hard drive":
        pass  # process to optimize the hard drive
    elif command == "defragment hard drive":
        pass  # process to defragment the hard drive
    elif command == "check disk health":
        pass  # process to check disk health
    elif command == "format [drive letter]":
        pass  # process to format the specified drive
    elif command == "mount iso image":
        pass  # process to mount iso image
    elif command == "eject [drive letter] or [device name]":
        pass  # process to eject the specified drive or device
    elif command == "show startup apps":
        pass  # process to show startup apps
    elif command == "disable startup apps":
        pass  # process to disable startup apps
    elif command == "enable startup apps":
        pass  # process to enable startup apps
    elif command == "check for driver updates":
        pass  # process to check for driver updates
    elif command == "update drivers automatically":
        pass  # process to update drivers automatically
    elif command == "check ram health":
        pass  # process to check ram health
    elif command == "monitor system performance":
        pass  # process to monitor system performance
    elif command == "open resource monitor":
        pass  # process to open resource monitorelif command == "set custom keyboard shortcut":  # process to set custom keyboard shortcut
    elif command == "reset keyboard settings":
        pass  # process to reset keyboard settings
    elif command == "enable sticky keys":
        pass  # process to enable sticky keys
    elif command == "disable sticky keys":
        pass  # process to disable sticky keys
    elif command == "open device security settings":
        pass  # process to open device security settings
    elif command == "enable tpm security":
        pass  # process to enable tpm security
    elif command == "disable tpm security":
        pass  # process to disable tpm security
    elif command == "disable cortana":
        pass  # process to disable cortana
    elif command == "enable cortana":
        pass  # process to enable cortana
    elif command == "open system restore":
        pass  # process to open system restore
    elif command == "rollback to previous restore point":
        pass  # process to rollback to previous restore point
    elif command == "set up new restore point":
        pass  # process to set up a new restore point
    elif command == "open windows store":
        pass  # process to open windows store
    elif command == "check for app updates":
        pass  # process to check for app updates
    elif command == "install app from windows store":
        pass  # process to install app from windows store
    elif command == "uninstall app":
        pass  # process to uninstall app
    elif command == "clear windows store cache":
        pass  # process to clear windows store cache
    elif command == "check for software conflicts":
        pass  # process to check for software conflicts
    elif command == "show error logs":
        pass  # process to show error logs
    elif command == "clear error logs":
        pass  # process to clear error logs
    elif command == "check for broken shortcuts":
        pass  # process to check for broken shortcuts
    elif command == "fix broken shortcuts":
        pass  # process to fix broken shortcuts
    elif command == "reinstall windows store":
        pass  # process to reinstall windows store
    elif command == "reset network settings":
        pass  # process to reset network settings
    elif command == "enable system restore":
        pass  # process to enable system restore
    elif command == "disable system restore":
        pass  # process to disable system restore
    elif command == "show recent activities in action center":
        pass  # process to show recent activities in action center
    elif command == "open windows security":
        pass  # process to open windows security
    elif command == "check network permissions":
        pass  # process to check network permissions
    elif command == "scan for corrupted system files":
        pass  # process to scan for corrupted system files
    elif command == "repair corrupted system files":
        pass  # process to repair corrupted system files
    elif command == "show system disk usage":
        pass  # process to show system disk usage
    elif command == "clean system restore points":
        pass  # process to clean system restore points
    elif command == "set default printer to [printer name]":
        pass  # process to set default printer
    elif command == "add a printer":
        pass  # process to add a printer
    elif command == "remove a printer":
        pass  # process to remove a printer
    elif command == "set up a shared folder":
        pass  # process to set up a shared folder
    elif command == "set up a network printer":
        pass  # process to set up a network printer
    elif command == "check system uptime":
        pass  # process to check system uptime
    elif command == "show uptime for [service name]":
        pass  # process to show uptime for specific service
    elif command == "open chrome":
        pass  # process to open chrome
    elif command == "open a new tab":
        pass  # process to open a new tab in chrome
    elif command == "open an incognito tab":
        pass  # process to open an incognito tab
    elif command == "close current tab":
        pass  # process to close the current tab
    elif command == "close chrome":
        pass  # process to close chrome
    elif command == "go to [website name]":
        pass  # process to go to the specified website
    elif command == "open [website url]":
        pass  # process to open the specified website url
    elif command == "refresh the page":
        pass  # process to refresh the current page
    elif command == "go back to the previous page":
        pass  # process to go back to the previous page
    elif command == "go forward to the next page":
        pass  # process to go forward to the next page
    elif command == "open a new window":
        pass  # process to open a new window
    elif command == "open chrome settings":
        pass  # process to open chrome settings
    elif command == "open chrome downloads":
        pass  # process to open chrome downloads
    elif command == "open chrome history":
        pass  # process to open chrome history
    elif command == "open bookmarks":
        pass  # process to open bookmarks
    elif command == "open bookmark manager":
        pass  # process to open bookmark manager
    elif command == "zoom in on the page":
        pass  # process to zoom in on the page
    elif command == "zoom out on the page":
        pass  # process to zoom out on the page
    elif command == "reset zoom":
        pass  # process to reset the zoom
    elif command == "mute tab":
        pass  # process to mute the tab
    elif command == "unmute tab":
        pass  # process to unmute the tab
    elif command == "pin this tab":
        pass  # process to pin the current tab
    elif command == "unpin this tab":
        pass  # process to unpin the current tab
    elif command == "switch to next tab":
        pass  # process to switch to the next tab
    elif command == "switch to previous tab":
        pass  # process to switch to the previous tab
    elif command == "search google for [query]":
        pass  # process to search google for the specified query
    elif command == "search youtube for [query]":
        pass  # process to search youtube for the specified query
    elif command == "open gmail":
        pass  # process to open gmail
    elif command == "open google drive":
        pass  # process to open google drive
    elif command == "open google docs":
        pass  # process to open google docs
    elif command == "open google sheets":
        pass  # process to open google sheets
    elif command == "open google calendar":
        pass  # process to open google calendar
    elif command == "open youtube":
        pass  # process to open youtube
    elif command == "play the video on youtube":
        pass  # process to play the video on youtube
    elif command == "pause the youtube video":
        pass  # process to pause the youtube video
    elif command == "skip the youtube ad":
        pass  # process to skip the youtube ad
    elif command == "maximize chrome window":
        pass  # process to maximize chrome window
    elif command == "minimize chrome window":
        pass  # process to minimize chrome window
    elif command == "full-screen mode":
        pass  # process to enable full-screen mode
    elif command == "exit full-screen mode":
        pass  # process to exit full-screen mode
    elif command == "save webpage as pdf":
        pass  # process to save the webpage as pdf
    elif command == "print the page":
        pass  # process to print the page
    elif command == "bookmark this page":
        pass  # process to bookmark the current page
    elif command == "open last closed tab":
        pass  # process to open the last closed tab
    elif command == "open a specific site from bookmarks":
        pass  # process to open a specific site from bookmarks
    elif command == "open private browsing":
        pass  # process to open private browsing mode
    elif command == "enable dark mode in chrome":
        pass  # process to enable dark mode in chrome
    elif command == "clear browsing data":
        pass  # process to clear browsing data
    elif command == "clear cache":
        pass  # process to clear cache
    elif command == "check for chrome updates":
        pass  # process to check for chrome updates
    elif command == "open chrome help":
        pass  # process to open chrome help
    elif command == "close all tabs":
        pass  # process to close all tabs
    elif command == "go to the homepage":
        pass  # process to go to chrome's homepage
    elif command == "add a new bookmark":
        pass  # process to add a new bookmark
    elif command == "show bookmarks bar":
        pass  # process to show bookmarks bar
    elif command == "hide bookmarks bar":
        pass  # process to hide bookmarks bar
    elif command == "open a chrome extension":
        pass  # process to open a specific chrome extension
    elif command == "disable an extension":
        pass  # process to disable a specific extension
    elif command == "enable an extension":
        pass  # process to enable a specific extension
    elif command == "check extensions in chrome":
        pass  # process to check extensions in chrome
    elif command == "open chrome task manager":
        pass  # process to open chrome task manager
    elif command == "open chrome devtools":
        pass  # process to open chrome devtools
    elif command == "open chrome developer tools (f12)":
        pass  # process to open chrome developer tools
    elif command == "take a screenshot in chrome":
        pass  # process to take a screenshot in chrome
    elif command == "open google search in new tab":
        pass  # process to open google search in a new tab
    elif command == "open incognito mode":
        pass  # process to open incognito mode
    elif command == "pin current tab":
        pass  # process to pin the current tab
    elif command == "unpin tab":
        pass  # process to unpin the current tab
    elif command == "show tab preview":
        pass  # process to show tab preview
    elif command == "hide tab preview":
        pass  # process to hide tab preview
    elif command == "show chrome toolbar":
        pass  # process to show chrome toolbar
    elif command == "hide chrome toolbar":
        pass  # process to hide chrome toolbar
    elif command == "open chrome’s incognito window":
        pass  # process to open chrome’s incognito window
    elif command == "open chrome’s flags menu":
        pass  # process to open chrome's flags menu
    elif command == "open chrome’s task manager":
        pass  # process to open chrome's task manager
    elif command == "clear history in chrome":
        pass  # process to clear chrome history
    elif command == "search within a webpage":
        pass  # process to search within the webpage
    elif command == "save image from webpage":
     pass  # process to save an image from the webpage
    elif command == "open a downloaded file":
        pass  # process to open a downloaded file
    elif command == "open chrome apps":
        pass  # process to open chrome apps
    elif command == "open chrome extension settings":
        pass  # process to open chrome extension settings
    elif command == "show download bar":
        pass  # process to show the download bar
    elif command == "hide download bar":
        pass  # process to hide the download bar
    elif command == "go to settings in chrome":
        pass  # process to go to chrome settings
    elif command == "enable/disable notifications":
        pass  # process to enable or disable notifications
    elif command == "reset chrome settings":
        pass  # process to reset chrome settings
    elif command == "change chrome theme":
        pass  # process to change chrome theme
    elif command == "open google news":
        pass  # process to open google news
    elif command == "open social media site":
        pass  # process to open a social media site
    elif command == "open news website":
        pass  # process to open a news website
    elif command == "translate this page":
        pass  # process to translate the current page
    elif command == "stop the page from loading":
        pass  # process to stop the page from loading
    elif command == "open chrome's 'about' page":
        pass  # process to open chrome's about page
    elif command == "open chrome’s privacy settings":
        pass  # process to open chrome's privacy settings
    elif command == "enable chrome’s password manager":
        pass  # process to enable chrome's password manager
    elif command == "add a new password in chrome":
        pass  # process to add a new password in chrome
    elif command == "check saved passwords in chrome":
        pass  # process to check saved passwords in chrome
    elif command == "manage saved passwords":
        pass  # process to manage saved passwords
    elif command == "clear saved passwords":
        pass  # process to clear saved passwords
    elif command == "enable autofill in chrome":
        pass  # process to enable autofill in chrome