import json
import os

class JSON:
    def __init__(self, file_path):
        self.file_path = file_path
        self._initialize_file()

    def _initialize_file(self):
        # Check if the file exists; if not, create it with an empty list
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)  # Start with an empty list

    def read(self):
        # Read and return the current contents of the JSON file
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def append(self, new_data):
        # Load existing data
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # Ensure we're working with a top-level list
        if not isinstance(data, list):
            data = []  # Reset if the format is incorrect

        # Extend the list directly with new_data items, assuming new_data is a list of items
        data.extend([new_data])  # Add items without creating additional nesting
        self._write_data(data)

    def clear(self):
        # Clear all data by writing an empty list
        self._write_data([])  # Write an empty list

    def write(self, element):
        # Replace all data with the given element inside a top-level list
        self._write_data([element])  # Wrap element in a list

    def remove_element(self, element_name):
        # Load existing data
        data = self.read()
        
        # Iterate through each element to find a match
        for item in data:
            if item[0] == element_name:
                data.remove(item)  # Remove the first match
                self._write_data(data)  # Update the file after removal
                print(f"Removed: {item}")
                return data  # Return updated data list after removal
        
        print("Element not found.")
        return data  # Return unmodified data if no match is found

    def _write_data(self, data):
        # Custom write to ensure formatting and spacing
        with open(self.file_path, 'w') as f:
            json_str = json.dumps(data, indent=4, separators=(',', ': '))
            f.write(json_str + '\n')  # Add a newline at the end



'''sample gif json:
[
    ["skull.gif",[740,200]]
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

'''sample input 
[
    [
        "Enter your name",       
        [100, 100],               
        [400, 150],              
        [255, 0, 0],             
        14,                       
        1                       
    ],
    [
        "Enter your message",     
        [100, 200],              
        [400, 350],             
        [0, 0, 255],           
        12,                      
        0                        
    ]
]
'''