```python
import os
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(data, file_path):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def normalize_data(data):
    """
    Normalize data using Min-Max scaling.
    """
    data_min = np.min(data)
    data_max = np.max(data)
    return (data - data_min) / (data_max - data_min)

def encode_labels(labels):
    """
    Encode labels using LabelEncoder.
    """
    encoder = LabelEncoder()
    encoder.fit(labels)
    return encoder.transform(labels), encoder

def decode_labels(encoded_labels, encoder):
    """
    Decode labels using LabelEncoder.
    """
    return encoder.inverse_transform(encoded_labels)

def get_environment_variable(var_name):
    """
    Get the value of an environment variable.
    """
    return os.getenv(var_name)

def set_environment_variable(var_name, var_value):
    """
    Set the value of an environment variable.
    """
    os.environ[var_name] = var_value
```