import os
import json
from prettytable import PrettyTable

__item_db_location__ = "db/items"
__current_session_location__ = "db/session/current_session.db"
__item_last_id__ = "db/util/last_id.db"

table = PrettyTable(['ID', 'Name', 'Buying price', 'Selling price'])

def addItem(params):
    last_id = getLastID()
    new_id = last_id + 1

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
                    if os.path.isfile(f"{__item_db_location__}/{new_id}.db"):
                        print("item already exsists")
                    else:
                        _data_ = {
                            "id": new_id,
                            "name": params[0],
                            "buyingPrice": params[1],
                            "sellingPrice": params[2]
                        }
                        with open(f"{__item_db_location__}/{new_id}.db", "w") as item_file:
                            json.dump(_data_, item_file)
                        updateLastID(new_id)
            else:
                print("check your command")
        else:
            print("You don't have permission")

    else:
        print("No current session, please login")

def viewAll():
    item_files = os.listdir(__item_db_location__)
    for item_file_name in item_files:
        item_arr = get_item_by_path(f"{__item_db_location__}/{item_file_name}")
        table.add_row(item_arr)
    print(table)

def viewSingleItem(params):
    item_arr = get_item_by_path(f"{__item_db_location__}/{params[0]}.db")
    table.add_row(item_arr)
    print(table)

def deleteItem(params):
    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]

        if userRole == "admin":
            if len(params) == 1:
                file_path = f"{__item_db_location__}/{params[0]}.db"
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print("Item deleted")
                else:
                    print("Item does not exist")
            else:
                print("check your command")
        else:
            print("You don't have permission")

    else:
        print("No current session, please login")


# utility functions

def getLastID():
    if os.path.exists(__item_last_id__):
        with open(__item_last_id__, "r") as last_id_file:
            return int(last_id_file.readline())
    else:
        return 0

def updateLastID(id):
    with open(__item_last_id__, "w") as last_id_file:
        last_id_file.write(str(id))

def get_item_by_path(path):
    with open(path, "r") as item_file:
        _data_ = json.load(item_file)
        return [_data_["id"], _data_["name"], _data_["buyingPrice"], _data_["sellingPrice"]]
