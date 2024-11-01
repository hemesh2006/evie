from components.functions import *
from components.json_folder.jsonmanager import *
from components.speak import *
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
def load_screen():
    gif.write(["loadinggif.gif",[850,350]])
while True:
    #stabilization
    #
    #text=input(speak("command",150,1))
    time.sleep(0.3)
    #speak("opening youtube",100,1)
    #search_youtube("tamil song")
    gif.write(["skull.gif",[850,350]])
    text.write([str(mouse_position()),[400,200],20,"yellow"])
    text.append(["hello",[700,200],20,"yellow"])
    time.sleep(5)
    gif.remove_element("skull.gif")
    text.remove_element("hello")
    text.write(["ht",[400,200],20,"yellow"])
    time.sleep(3)

    
    