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
        choice = (input('c -> continue, a -> abort, e -> exit')).lower()
    return choice
