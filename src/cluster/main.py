from database import *

def main():
    client = getConnection(True)
    print(client)

if __name__ == '__main__':
    main()