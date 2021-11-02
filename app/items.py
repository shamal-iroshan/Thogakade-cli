import os
import json

__item_db_location__ = "db/items"
__current_session_location__ = "db/session/current_session.db"

def addItem(params):
    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]

        if userRole == "admin":
            if len(params) == 3:
                if not os.path.isdir(__item_db_location__):
                    os.makedirs(__item_db_location__)
                else:
                    if os.path.isfile(f"{__item_db_location__}/{params[0]}.db"):
                        print("item already exsists")
                    else:
                        _data_ = {
                            "name": params[0],
                            "butingPrice": params[1],
                            "sellingPrice": params[2]
                        }
                        with open(f"{__item_db_location__}/{params[0]}.db", "w") as item_file:
                            json.dump(_data_, item_file)
            else:
                print("check your command")
        else:
            print("You don't have permission")

    else:
        print("No current session, please login")
