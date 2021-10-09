import os
from base64 import b64encode
from database_operations import *

def create_salt() -> bytes:
    salt = b64encode(os.urandom(4096))
    flag = create(r'application_key.json', salt.decode('utf-8'))
    return salt

print(create_salt())
