from components.json_folder.jsonmanager import *
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
def sign_in():
    pass
def sign_up():
    path="output.json"
    
    input.write(["username",[780, 300],[1100, 400],[255, 0, 0],38,1])
    file=open(path,"r")
    data=json.load(file)
    username=data["single_line"]
    time.sleep(20)
    input.write(["password",[780, 300],[1100, 400],[255, 0, 0],38,1])
    file=open(path,"r")
    data=json.load(file)
    password=data["single_line"]
button_reset("arrow")

while(1):
    text.clear()
    image.clear()
    gif.clear()
    button.clear()
    input.clear()
    init_screen()
    screen_show()
    sign_up()
    time.sleep(10)
    