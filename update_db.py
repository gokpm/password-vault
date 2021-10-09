import os
import json
import base64

vault_filepath = r'vault.json'

def build_vault() -> bool:
    if not os.path.isfile(vault_filepath):
        write_into_vault({})
        return True
    return False
    
def read_from_vault() -> dict:
    try:
        with open(vault_filepath, 'r') as vault:
            read_data = json.load(vault)
    except json.decoder.JSONDecodeError:
        read_data = {}
    return read_data

def write_into_vault(data_to_write) -> None:
    with open(vault_filepath, 'w') as vault:
        json.dump(data_to_write, vault, indent = 4)
    return

public_key_filepath = r'public_key.json'

def build_key() -> bool:
    if not os.path.isfile(public_key_filepath):
        salt = base64.b64encode(os.urandom(4096)).decode('utf-8')
        write_into_key(salt)
        return True
    return False

def write_into_key(data_to_write) -> None:
    with open(public_key_filepath, 'w') as key:
        json.dump(data_to_write, key, indent = 4)
    return

def read_from_key():
    try:
        with open(public_key_filepath, 'r') as key:
            read_data = json.load(key)
    except json.decoder.JSONDecodeError:
        salt = base64.b64encode(os.urandom(4096)).decode('utf-8')
        write_into_key(salt)
        read_data = read_from_key()
    return read_data
    
