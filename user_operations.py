import sys
from tkinter import Tk
from getpass import getpass
from time import sleep
from menu import *
from salt import *

def copy(text_to_copy):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text_to_copy)
    r.update()
    print('you have 5 seconds to paste it')
    sleep(5)
    r.clipboard_clear()
    r.clipboard_append('')
    r.update()
    r.destroy()
    print('destroyed')
    return

def store(vault, database, secret):
    app = getpass('App: ')
    match = check_database(app, database, secret)
    if match:
        flag = False
        choice = update_menu()
        if choice == 'u':
            username = lock(getpass('Username: '), secret)
            password = lock(getpass('Password: '), secret)
            database.update({app: [username, password]})
            write(vault, database)
            choice = None
            flag = True
        if choice == 'b':
            choice = None
            return flag, choice
    else:
        app = lock(app, secret)
        username = lock(getpass('Username: '), secret)
        password = lock(getpass('Password: '), secret)
        database.update({app: [username, password]})
        write(vault, database)
        choice = None
        flag = True
    return flag, choice

def retrieve(database, secret):
    app = getpass('App: ')
    match = check_database(app, database, secret)
    if match:
        while True:
            choice = final_menu()
            if choice == 'u':
                decrypted_username = unlock(database[key][0], secret)
                copy(decrypted_username)
                choice = None
                continue
            if choice == 'p':
                decrypted_password = unlock(database[key][1], secret)
                copy(decrypted_password)
                choice = None
                continue
            return choice
    else:
        choice = None
        print('No apps found')
    return choice

def update(vault, database, secret):
    app = getpass('App: ')
    match = check_database(app, database, secret)
    flag = False
    if match:
        username = lock(getpass('Username: '), secret)
        password = lock(getpass('Password: '), secret)
        database.update({app: [username, password]})
        write(vault, database)
        choice = None
        flag = True
    else:
        choice = store_menu()
        if choice == 's':
            username = lock(getpass('Username: '), secret)
            password = lock(getpass('Password: '), secret)
            database.update({app: [username, password]})
            write(vault, database)
            choice = None
            flag = True
        if choice == 'b':
            choice = None
            return flag, choice
    return flag, choice

def check_database(app, database, secret):
    match = False
    for key in database:
        key = unlock(key, secret)
        if app == key:
            match = True
            break
        else:
            pass
    return match
    
