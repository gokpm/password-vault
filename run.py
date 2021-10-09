from manager import *

def main():
    password = input('password:\n')
    while True:
        login(password)
        options()

if __name__ == '__main__':
    main()
