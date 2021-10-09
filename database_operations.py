import os
import json

def create(filepath: str) -> bool:
    flag = False
    if not os.path.isfile(filepath):
        write(filepath, None)
        flag = True
    return flag

def read(filepath: str) -> str or dict:
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def write(filepath: str, data: str or dict) -> bool:
    flag = False
    with open(filepath, 'w') as file:
        json.dump(data, file, indent = 4)
        flag = True
    return flag
