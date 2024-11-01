from components.functions import *
from components.json_folder.jsonmanager import *
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
def startup():
    pass
while True:
    time.sleep(0.3)
    gif.clear()
    
    a,b=mouse_position()
    text.write([str(a)+","+str(b),[1550,100],40,"yellow"])
    text.append(["ram: "+str(ram_usage()),[1550,300],30,"blue"])
    gif.write(["skull.gif",[740,200]])
    
    
