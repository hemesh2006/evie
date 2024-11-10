from components.json_folder.jsonmanager import *
from components.speak import *
from components.functions import *
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
    #spk("thankks for using me evie me s evie iam making for you "
    gif.append(["loadh.gif",[840,700]])
    command=mic()
    gif.remove_element("loadh.gif")
    
    
    
    