```python
import json
import os
import random

def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_path, data):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def preprocess_data(data):
    """
    Preprocess the data.
    """
    # Implement your preprocessing logic here
    return data

def split_data(data, test_size=0.2):
    """
    Split the data into training and testing sets.
    """
    data_length = len(data)
    test_length = int(data_length * test_size)
    
    random.shuffle(data)
    
    return data[test_length:], data[:test_length]

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def get_file_path(directory_path, file_name):
    """
    Get the full file path.
    """
    return os.path.join(directory_path, file_name)
```