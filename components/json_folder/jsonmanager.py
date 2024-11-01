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

    def _write_data(self, data):
        # Custom write to ensure formatting and spacing
        with open(self.file_path, 'w') as f:
            json_str = json.dumps(data, indent=4, separators=(',', ': '))
            f.write(json_str + '\n')  # Add a newline at the end

