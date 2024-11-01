from components.functions import *
from components.json_folder.jsonmanager import *
from components.speak import *
import webbrowser
'''
battery_info()
screen_shot()
take_photo()
set_volume()
play_music("hi")
pause_music()
resume_music()
stop_music()
open_application(path)
google_search(query)
search_youtube(query)
click()
scroll_down(amount)
scroll_up(amount)
close_tab()
close_current_window()
search_wikipedia(query)
shutdown()
sleep()
hybrid_sleep()
deep_sleep()
wifi_on()
wifi_off()
minimize_current_window()
type_keyboard(text)
maximize_current_window()
execute_command(command)
get_disk_space(disk)
ram_usage()
'''

text=JSON(r"C:\Users\HP\Desktop\evie\components\json_folder\text.json")
image=JSON(r"C:\Users\HP\Desktop\evie\components\json_folder\images.json")
gif=JSON(r"C:\Users\HP\Desktop\evie\components\json_folder\gif.json")
import time


def automatic_show():
    ram_text=ram_usage()
    text.write(["ram:"+str(ram_text)+"%",[1700,200],20,"yellow"])
while 1:
    
    #stabilization
    #
    #text.write([str(mouse_position()),[400,200],20,"yellow"])
    #but_screen()
    
    #text=input(speak("command",150,1))
    #time.sleep(0.3)
    #speak("opening youtube",100,1)
    #search_youtube("tamil song")
    #gif.write(["skull.gif",[850,350]])
    text.write([str(mouse_position()),[400,200],20,"yellow"])
    #text.append(["hello",[700,200],20,"yellow"])
    #time.sleep(5)
    #gif.remove_element("skull.gif")
    #text.remove_element("hello")
    #text.write(["ht",[400,200],20,"yellow"])
    #time.sleep(3)
    #command=input("Enter a  Command")
    command=input("COMMAND> :")
    command=command.replace("evie","")
    if "open youtube" in command:
        command=command.replace("open youtube","")
        search_youtube(command)
    elif "open google" in command:
        command=command.replace("open google","")
        google_search(command)
    elif "open whatsapp" in command:
        open_application(command)
    elif "open notepad" in command:
        open_application(r"C:\Program Files\Notepad++\notepad++.exe")
    elif command=="make full screen":
        maximize_current_window()
    elif command=="maximize the screen":
        maximize_current_window()
    elif command=="minimize the screen":
        minimize_current_window()
    elif command=="minimize screen":
        minimize_current_window()
    elif command=="minimize":
        minimize_current_window()
    elif command=="show network detail":
        pass
    elif command=="show network":
        pass
    elif command=="connect wifi":
        pass
    elif command=="connect wifi <name>":
        pass
    elif command=="connect bluetooth":
        pass
    elif command=="turn on bluetooth":
        pass
    elif command=="turn on wifi":
        pass
    elif command=="take a selfie":
        take_photo()
    elif command=="take selfie":
        take_photo()
    elif command=="take a photo":
        take_photo()
    elif command=="take photo":
        take_photo()
    elif command=="take screenshot":
        screen_shot()
    elif command=="disable wifi":
        pass
    elif command=="enable wifi":
        pass
    elif command=="search on google":
        pass
    elif command=="explain <something>":
        pass
    elif command=="sleep mode enable":
        sleep()
    elif command=="enable sleep mode":
        sleep()
    elif command=="enable sleep":
        sleep()
    elif command=="enable hybretrete":
        pass
    elif command=="shutdown":
        pass
    elif command=="shutdown the computer":
        pass
    elif command=="shutdown it":
        pass
    elif command=="play music":
        pass
    elif command=="play song":
        pass
    elif command=="play tamil song":
        pass
    elif command=="song please":
        pass
    elif command =="reduce volume":
        pass
    elif command=="increase volume":
        pass
    elif command=="full volume":
        set_volume(100)
    elif command=="increase brightness":
        pass
    elif command=="keyboard light":
        pass
    elif command=="backlight on":
        pass
    elif command=="backlight off":
        pass
    elif command=="open calculator":
        pass
    elif command=="open chatgpt":
        webbrowser.open("https:/chatgpt.com")
    elif command=="open email":
        webbrowser.open("https://mail.google.com")
    elif command=="lock the cursor":
        pass
    elif command=="lock cursor":
        pass
    elif command=="activate user":
        pass
    elif command=="show battery percentage":
        pass
    elif command=="show battery":
        pass
    elif command=="close it":
        time.sleep(4)
        pyautogui.hotkey("alt","f4")
    elif command=="close app":
        time.sleep(4)
        pyautogui.hotkey("alt","f4")
    elif command=="close tab":
        time.sleep(4)
        close_tab()
    elif "ram usage" in command:
        print(ram_usage())
    elif command=="battery info":
        battery=battery_info()
        print(battery[0])
    elif command=="click mouse":
        click()
    elif command=="open setting":
        pass
    elif command=="activate image detection":
        pass
    elif command=="activate image detect":
        pass
    elif command=="image detect":
        pass
    elif command=="detect image":
        pass
    elif command=="restart it":
        pass
    elif command=="connect jionet":
        pass
    elif command=="connect wifi hotspot":
        pass
    elif command=="copy the content":
        pass
    elif command=="paste it":
        pass
    elif "type" in command:
        command=command.replace("type","")
        type_keyboard(command)
    elif command=="enable safe mode":
        pass
    elif command=="disable evie":
        pass
    elif command=="evie stop it":
        pass
    elif command=="shut your mouth":
        pass
    elif command=="do not speak":
        pass
    elif command=="do you have any feeling":
        pass
    elif command=="do you have feeling":
        pass
    elif command=="close all apps":
        pass
    elif command=="close apps":
        pass
    elif command=="evie what happen":
        pass
    elif command=="open new tab":
        pass
    elif command=="disable image detection":
        pass
    elif command=="disable detection":
        pass
    elif command=="detection":
        pass
    elif command=="press and hold it":
        pass
    elif command=="hold it":
        pass
    elif command=="scroll down":
        pass
    elif command=="scroll up":
        pass 
    elif command=="move cursor":
        pass
    elif command=="send a  selfie":
        pass
    elif command=="send a photo":
        pass
    elif command=="send screenshot":
        pass
    elif command=="good morning":
        pass
    elif command=="good afternoon":
        pass
    elif command=="open vscode":
        open_application(r"D:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    elif command=="code deploy":
        pass
    elif command=="start coding":
        pass
    elif command=="clone the repository":
        pass
    elif command=="open new window in vscode":
        pass
    elif command=="new window vscode":
        pass
    elif command=="compile it":
        pass
    elif command=="compile":
        pass
    elif command=="compile the code":
        pass
    elif command=="activate conda <name>":
        pass #
    elif command=="conda":
        pass
    elif command=="open project":
        pass ##from git clone
    elif command=="open vscode":
        pass
    elif command=="vscode":
        pass
    elif command=="code":
        pass
    elif command=="show battery":
        pass
    elif command=="show battery info":
        pass
    elif command=="half volume":
        set_volume(50)
    elif command=="mute it":
        pass
    elif command=="mute":
        pass
    elif command=="git pull":
        pass
    elif command=="git commit":
        pass
    elif command=="git add":
        pass
    elif command=="git push":
        pass
    elif command=="chatgpt":
        pass
    elif command=="chatgpt open":
        pass
    elif command=="open github":
        pass
    elif command=="activate gitbash":
        pass
    elif command=="activate git":
        pass
    elif command=="activate github":
        pass
    elif command=="search youtube":
        pass
    elif command=="windows button":
        pass
    elif command=="windows update":
        pass
    elif command=="open whatsapp beta":
        pass
    elif command=="whatsapp beta":
        pass
    elif command=="admin cmd":
        pass
    elif command=="cmd":
        pass
    elif command=="command prompt":
        pass
    elif command=="open new project":
        pass
    elif command=="close project":
        pass
    elif  command=="gpu usage":
        pass
    elif command=="gpu":
        pass
    elif command=="open chrome":
        pass
    elif command=="open file explorer":
        pass
    elif command=="chrome":
        pass
    elif command=="anaconda":
        pass
    elif command=="desktop":
        pass
    elif command=="open task manager":
        pass
    elif command=="task manager":
        pass
    elif command=="recycle bin":
        pass
    elif command=="stop detection":
        pass
    elif command=="clone git <repname>":
        pass
    elif command=="open vscode":
        pass
    elif command=="new project":
        pass
    elif command=="project":
        pass
    elif command=="new window on vscode":
        pass
    elif command=="open project":
        pass
    elif command=="vscode":
        pass
    elif command=="execute the code":
        pass
    elif command=="compile":
        pass
    elif command=="recognize detection":
        pass
    elif command=="check charge":
        pass
    elif command=="charge":
        pass
    elif command=="dt project":
        pass
    elif command=="what is your name":
       print("my name is evie i was  a  ai intelligent")
    elif command=="clear the overlay":
        text.clear()
        gif.clear()
        image.clear()
    elif command=="clear the screen":
        text.clear()
        gif.clear()
        image.clear()
    elif command=="clear screen":
        text.clear()
        gif.clear()
        image.clear()
    elif command=="what is your name":
        print("my name is evie i was  a  ai intelligent")
    elif command=="name please":
        print("my name is evie i was  a  ai intelligent")
    elif command=="what name":
        print("my name is evie i was  a  ai intelligent")
    elif command=="your name":
        print("my name is evie i was  a  ai intelligent")
    elif command=="your name please":
        print("my name is evie i was  a  ai intelligent")
    elif "search youtube" in command:
        command=command.replace("search youtube","")
        search_youtube(command)
