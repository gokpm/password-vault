import os
import base64
from tkinter import Tk
from time import sleep
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from update_db import *

def copy(text_to_copy):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text_to_copy)
    r.update()
    sleep(10)
    print('constructed')
    r.clipboard_clear()
    r.clipboard_append('')
    r.update()
    r.destroy()
    print('destructed')
    return

def store():
    app = input('app:\n')
    vault_dictionary = read_from_vault()
    i = 0
    for key in vault_dictionary:
        if app == decryption(key):
            i += 1
    if i == 0:
        app = encryption(app)
        username = encryption(input('username:\n'))
        password = encryption(input('password:\n'))
        vault_dictionary.update({app: {'username':username, 'password':password}})
        write_into_vault(vault_dictionary)
    else:
        print('update')
    vault_dictionary = None
    return

def retrieve():
    app = input('app:\n')
    vault_dictionary = read_from_vault()
    i = 0
    for key in vault_dictionary:
        if app == decryption(key):
            app = key
            i += 1
    if i > 0:
        choice = input('\nu -> username\np -> password\n\n')
        if choice == 'u':
            username = decryption(vault_dictionary[app]['username'])
            copy(username)
            choice = input('\np -> password\ne -> exit\n\n')
            if choice == 'p':
                password = decryption(vault_dictionary[app]['password'])
                copy(password)
            elif choice == 'e':
                exit()  
        elif choice == 'p':
            password = decryption(vault_dictionary[app]['password'])
            copy(password)
            choice = input('\nu -> username\ne -> exit\n\n')
            if choice == 'p':
                username = decryption(vault_dictionary[app]['username'])
                copy(username)
            elif choice == 'e':
                exit()
    vault_dictionary = None
    return

def update():
    app = input('app:\n')
    vault_dictionary = read_from_vault()
    i = 0
    for key in vault_dictionary:
        if app == decryption(key):
            app = key
            i += 1
    if i > 0:
        choice = input('\nu -> username\np -> password\nb -> both\n\n')
        if choice == 'u':
            username = encryption(input('username:\n'))
        elif choice == 'p':
            password = encryption(input('password:\n'))
        elif choice == 'b':
            username = encryption(input('username:\n'))
            password = encryption(input('password:\n'))
        vault_dictionary.update({app: {'username':username, 'password':password}})
        write_into_vault(vault_dictionary)
    else:
        print('store')
    vault_dictionary = None
    return

def login(password):
    global tunnel
    build_key()
    build_vault()
    salt = read_from_key().encode('utf-8')
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt,
                     iterations=1000000)
    password = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    tunnel = Fernet(password)
    return

def encryption(message_to_encrypt) -> str:
    encrypted_message = tunnel.encrypt(message_to_encrypt.encode())
    encrypted_message = encrypted_message.decode()
    return encrypted_message

def decryption(message_to_decrypt) -> str:
    decrypted_message = tunnel.decrypt(message_to_decrypt.encode())
    decrypted_message = decrypted_message.decode()
    return decrypted_message
    
def options():
    choice = input('s -> store\nu -> update\nr -> retrieve\n\n')
    if choice == 's':
        store()
    elif choice == 'u':
        update()
    elif choice == 'r':
        retrieve()
    elif choice == 'e':
        exit()
    return
        
        
    
