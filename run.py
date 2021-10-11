from salt import *
from application import *

def main():
    create_salt()
    while True:
        asyncio.run(login())
    return
        
if __name__ == '__main__':
    main()
