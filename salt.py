import os
from base64 import b64encode
from base64 import b32encode
from base64 import b16encode
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
                value0_record = old_encrypted_database_dictionary[key_record][0]
                value1_record = old_encrypted_database_dictionary[key_record][1]
                new_key_record = (key.encrypt(old_key.decrypt(key_record.encode()))).decode()
                new_value0_record = (key.encrypt(old_key.decrypt(value0_record.encode()))).decode()
                new_value1_record = (key.encrypt(old_key.decrypt(value1_record.encode()))).decode() 
                new_encrypted_database_dictionary.update({new_key_record: [new_value0_record, new_value1_record]})        
    write(r'database.json', new_encrypted_database_dictionary)
    return key

def get_key(filepath: str) -> bytes:
    salt = read(filepath).encode()
    key = Fernet(salt)
    return key

def generate_key(password):
    salt = b64encode(os.urandom(4096))
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt,
                     iterations=1000000)
    password = urlsafe_b64encode(kdf.derive(password.encode()))
    key = Fernet(password)
    return key

def lock(message, key) -> str:
    message = message.encode()
    encrypted_message = key.encrypt(message)
    encrypted_message = encrypted_message.decode()
    return encrypted_message

def unlock(message, key) -> str:
    message = message.encode()
    decrypted_message = key.decrypt(message)
    decrypted_message = decrypted_message.decode()
    return decrypted_message
    
    
