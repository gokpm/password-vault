import sys
from menu import *
from salt import *
from database_operations import *

def login():
    key = get_key(r'application_key.json')
    choice = login_menu()
    if choice == 'l':
        username = input('Username: ')
        database = read(r'database.json')
        flag = False
        for key_record in database:
            decrypted_key_record == (key.decrypt(key_record.encode())).decode()
            if username == decrypted_key_record:
                flag = True
                break
        if flag:
            pass
        else:
            choice = new_user()
            if choice == 'y':
                user_key = b64encode(os.urandom(16))
                print('Setup the following key in the Google Authenticator app')
                print('key: {0}'.format(user_key.decode()))
                choice = navigation()
                if choice()
                vault_key = b64encode(os.urandom(16))
                vault_name = r'{0}.json'.format(vault_key.decode())
                username = lock(username, key)
                user_key = lock(user_key, key)
                vault_name = lock(vault_name, key)
                database.update({username:[user_key, vault_name]})
                write(r'database.json', database)
            if choice == 'n':
                break
            if choice == 'e':
                sys.exit()
    if choice == 'e':
        sys.exit()
        
    
    
