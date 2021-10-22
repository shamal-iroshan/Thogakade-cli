import sys
from app.user import register, login, current

if __name__ == '__main__':
    arguments = sys.argv[1:]

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "register":
            register(params)
        elif command == "login":
            login(params)
        elif command == "current":
            current()