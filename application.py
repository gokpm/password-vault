import sys
import asyncio
from menu import *
from salt import *
from database_operations import *
from authenticator import *

async def login() -> None:
    key = get_key(r'application_key.json')
    choice = login_menu()
    if choice == 'l':
        username = input('Username: ')
        database = read(r'database.json')
        flag = False
        for key_record in database:
            decrypted_key_record = unlock(key_record, key)
            if username == decrypted_key_record:
                user_key = unlock(database[key_record][0], key)
                vault_key = unlock(database[key_record][1], key)
                user_salt = unlock(database[key_record][2], key)
                flag = True
                break
        if flag:
            tasks = []
            tasks.append(asyncio.create_task(get_totp(user_key)))
            tasks.append(asyncio.create_task(input_otp()))
            await asyncio.wait(tasks)
            flag = tasks[1].result()
            if flag:
                secret = Fernet(user_salt.encode())
                user_database = read(vault_key)
                while True:
                    choice = main_menu()
                    if choice == 's':
                        app = lock(input('App: '), secret)
                        username = lock(input('Username: '), secret)
                        password = lock(input('Password: '), secret)
                        user_database.update({app: [username, password]})
                        write(vault_key, user_database)
                        continue
                    if choice == 'u':
                        continue
                    if choice == 'r':
                        app = input('App: ')
                        for key_record in user_database:
                            decrypted_app = unlock(key_record, secret)
                            if app == decrypted_app:
                                decrypted_username = unlock(user_database[key_record][0], secret)
                                decrypted_password = unlock(user_database[key_record][1], secret)
                                print(decrypted_username)
                                print(decrypted_password)
                        continue
                    if choice == 'l':
                        return
                    if choice == 'e':
                        sys.exit()
            else:
                return
        else:
            choice = new_user()
            if choice == 'y':
                user_key = b32encode(os.urandom(16)).decode()
                print('Scan the following QR Code with Google Authenticator')
                get_qr(username, user_key)
                choice = navigation()
                if choice == 'c':
                    user_salt = urlsafe_b64encode(os.urandom(32)).decode()
                    vault_key = b32encode(os.urandom(16))
                    vault_name = r'{0}.json'.format(vault_key.decode())
                    create(vault_name, {})
                    username = lock(username, key)
                    user_key = lock(user_key, key)
                    vault_name = lock(vault_name, key)
                    user_salt = lock(user_salt, key)
                    database.update({username:[user_key, vault_name, user_salt]})
                    write(r'database.json', database)
                if choice == 'a':
                    return
                if choice == 'e':
                    sys.exit()
            if choice == 'n':
                return
            if choice == 'e':
                sys.exit()
    if choice == 'e':
        sys.exit()
    return
        
    
    
