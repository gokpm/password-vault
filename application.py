import sys
from menu import *
from salt import *
from database_operations import *

def login():
    key = get_key(r'application_key.json')
    choice = login_menu()
    if choice == 'l':
        input_username = input('Username: ')
        database = read(r'database.json')
        flag = False
        for key_record in database_dictionary:
            decrypted_key_record == (key.decrypt(key_record.encode())).decode()
            if input_username == decrypted_key_record:
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
                vault_key = b64encode(os.urandom(16))
                vault_name = r'{0}.json'.format(vault_key.decode())
                else:
                    sys.exit()
            if choice == 'n':
                sys.exit()                      
    if choice == 'e':
        sys.exit()
        
    
    
