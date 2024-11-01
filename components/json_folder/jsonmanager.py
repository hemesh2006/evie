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
                json.dump([], f)

    def read(self):
        # Read and return the current contents of the JSON file
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def append(self, new_data):
        # Load existing data, append the new data, and write back with custom formatting
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        data.append(new_data)
        self._write_data(data)

    def clear(self):
        # Clear all data by writing an empty list
        self._write_data([])

    def write(self, elements):
        # Replace all data with the given list of elements
        self._write_data(elements)

    def _write_data(self, data):
        # Custom write to ensure each list item appears on a single line
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=1, separators=(',', ': '))
            f.write('\n')  # Add a newline at the end of the file

# Example usage
manager = JSON('data.json')

# Append a new element
manager.append(["asset\\src_gif\\new_image.gif", [150, 250]])

# Clear all elements in the file
manager.clear()

# Write multiple elements at once
manager.write([
    ["asset\\src_gif\\skull.gif", [100, 200]],
    ["asset\\src_gif\\circle.gif", [300, 400]],
    ["asset\\src_gif\\ui.gif", [700, 500]]
])

# Read the file contents to verify
print(manager.read())
