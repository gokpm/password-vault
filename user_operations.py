import sys
from tkinter import Tk
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
    app = input('App: ')
    for key in database:
        key = unlock(key, secret)
        if app == key:
            match = True
            break
        else:
            match = False
    if match:
        flag = False
        choice = update_menu()
        if choice == 'b':
            choice = None
            return
        if choice == 'u':
            choice = None
    else:
        app = lock(app, secret)
        username = lock(input('Username: '), secret)
        password = lock(input('Password: '), secret)
        database.update({app: [username, password]})
        write(vault, database)
        flag = True
    return flag, choice

def retrieve(database, secret):
    app = input('App: ')
    for key in database:
        if app == unlock(key, secret):
            match = True
            break
        else:
            match = False
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
        print('No apps found')
    return choice
