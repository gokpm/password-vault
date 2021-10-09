def login_menu() -> str:
    choice = (input('l -> login, e -> exit\n')).lower()
    return choice

def main_menu() -> str:
    choice = (input('s -> store, u -> update, r -> retrieve, l -> logout, e -> exit\n')).lower()
    return choice

def new_user() -> str:
    choice = (input('Create new user? (y/n)\n')).lower()
    return choice
