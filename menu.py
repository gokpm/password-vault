def login_menu() -> str:
    choice = None
    while choice not in ['l', 'e']:
        choice = (input('l -> login, e -> exit\n')).lower()
    return choice

def main_menu() -> str:
    choice = None
    while choice not in ['s', 'u', 'r', 'l', 'e']:
        choice = (input('s -> store, u -> update, r -> retrieve, l -> logout, e -> exit\n')).lower()
    return choice

def new_user() -> str:
    choice = None
    while choice not in ['y', 'n', 'e']:
        choice = (input('Create new user?\ny -> yes, n -> no, e -> exit\n')).lower()
    return choice

def navigation() -> str:
    choice = None
    while choice not in ['c', 'a', 'e']:
        choice = (input('c -> continue, a -> abort, e -> exit\n')).lower()
    return choice

def update_menu():
    choice = None
    print('App already present, use update')
    while choice not in ['u', 'b', 'l', 'e']:
        choice = (input('u -> update, b -> back, l -> logout, e -> exit\n'))
    return choice

def final_menu():
    choice = None
    while choice not in ['u', 'p', 'b', 'l', 'e']:
        choice = (input('u -> username, p -> password, b -> back, l -> logout, e -> exit\n'))
    return choice
    


