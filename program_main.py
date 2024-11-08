from components.json_folder.jsonmanager import *
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
text=JSON("components\\json_folder\\text.json")
image=JSON("components\\json_folder\\images.json")
input=JSON("components\\json_folder\\inputs.json")
gif=JSON("components\\json_folder\\gif.json")
def init_screen():
    text.clear()
    image.clear()
    input.clear()
    gif.clear()
    text.write(["evie",[860,380],70,"green"])


init_screen()
