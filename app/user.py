import os
import json

__user_db_location__ = "db/users"
__current_session_location__ = "db/session"

def register(params):
    if len(params) == 2:
        if not os.path.isdir(__user_db_location__):
            os.makedirs(__user_db_location__)
        else:
            if os.path.isfile(f"{__user_db_location__}/{params[0]}.db"):
                print("user name already exsists")
            else:
                _data_ = {
                    "username": params[0],
                    "password": params[1]
                }
                with open(f"{__user_db_location__}/{params[0]}.db", "w") as user_file:
                    json.dump(_data_, user_file)
    else:
        print("check your command")
            
    



def login(params):
    if len(params) == 2:
        if os.path.isfile(f"{__user_db_location__}/{params[0]}.db"):
            with open(f"{__user_db_location__}/{params[0]}.db") as user_file:
                _data_ = json.load(user_file)
                if params[1] == _data_["password"]:
                    if not os.path.isdir(__current_session_location__):
                        os.makedirs(__current_session_location__)
                        _session_ = {
                            "username": _data_["username"]
                        }
                        with open(f"{__current_session_location__}/current_session.db", "w") as session_file:
                            json.dump(_session_, session_file)
                    else:
                        _session_ = {
                            "username": _data_["username"]
                        }
                        with open(f"{__current_session_location__}/current_session.db", "w") as session_file:
                            json.dump(_session_, session_file)
                    print("Login successfull")
                else:
                    print("Check your password")
        else:
            print("No user found")
    else:
        print("check your command")
    

def current():
    if os.path.isfile(f"{__current_session_location__}/current_session.db"):
        with open(f"{__current_session_location__}/current_session.db", "r") as session_file:
            _data_ = json.load(session_file)
            print(_data_["username"])
    else:
        print("No current session")
