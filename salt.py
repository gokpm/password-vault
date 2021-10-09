import os
from base64 import urlsafe_b64encode
from database_operations import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def create_salt():
    new_encrypted_database_dictionary = {}
    salt = urlsafe_b64encode(os.urandom(32))
    key = Fernet(salt)
    flag_key = create(r'application_key.json', salt.decode())
    if flag_key:
        write(r'database.json', {})
    else:
        flag_database = create(r'database.json', {})
        old_salt = read(r'application_key.json').encode()
        old_key = Fernet(old_salt)
        write(r'application_key.json', salt.decode())
        if flag_database:
            pass
        else:
            old_encrypted_database_dictionary = read(r'database.json')
            for key_record in old_encrypted_database_dictionary:
                value_record = old_encrypted_database_dictionary[key_record]
                new_key_record = (key.encrypt(old_key.decrypt(key_record.encode()))).decode()
                new_value_record = (key.encrypt(old_key.decrypt(value_record.encode()))).decode()                          
                new_encrypted_database_dictionary.update({new_key_record:new_value_record})        
    write(r'database.json', new_encrypted_database_dictionary)
    return key
