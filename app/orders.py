import os
import json
from prettytable import PrettyTable

__order_db_location__ = "db/orders"
__current_session_location__ = "db/session/current_session.db"
__order_last_id__ = "db/util/order_last_id.db"
__cart_db_location__ = "db/orders/cart/cart.db"

table = PrettyTable(['ID', 'Name', 'Price', 'QTY'])

def placeOrder():
    last_id = getLastID()
    new_id = last_id + 1

    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]   
        if userRole == "customer":
            if os.path.getsize(__cart_db_location__) != 0:
                if os.path.exists(__cart_db_location__):
                    with open(__cart_db_location__, "r") as cart_file:
                        _cart_ = json.load(cart_file)
                        items = _cart_['items']
                        order = {
                            "id": new_id,
                            "items": items,
                            "user": _data_
                        }
                        user = _data_["username"]
                        if os.path.isdir(f"{__order_db_location__}/{user}"):
                            print(f"{__order_db_location__}/{user}/{new_id}.db")
                            with open(f"{__order_db_location__}/{user}/{new_id}.db", "w") as order_file:
                                json.dump(order, order_file)
                                updateLastID(new_id)
                        else:
                            os.makedirs(f"{__order_db_location__}/{user}")
                            with open(f"{__order_db_location__}/{user}/{new_id}.db", "w") as order_file:
                                json.dump(order, order_file)
                                updateLastID(new_id)



def viewSingleOrder(params):
    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]   
        if userRole == "customer":
            customerName = _data_["username"]
            with open(f"{__order_db_location__}/{customerName}/{params[0]}.db", "r") as order_file:
                order = json.load(order_file)
                items = order["items"]
                for item in items:
                    item_arr = [item["id"], item["name"], item["sellingPrice"], item["qty"]]
                    table.add_row(item_arr)
                print("Order ID: ", order["id"])
                print("Customer Name: ", customerName)
                print(table)
        elif userRole == "admin":
            customerName = params[0]
            with open(f"{__order_db_location__}/{customerName}/{params[1]}.db", "r") as order_file:
                order = json.load(order_file)
                items = order["items"]
                for item in items:
                    item_arr = [item["id"], item["name"], item["sellingPrice"], item["qty"]]
                    table.add_row(item_arr)
                print("Order ID: ", order["id"])
                print("Customer Name: ", customerName)
                print(table)

def viewAllOrders(params):
    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]   
        if userRole == "customer":
            customerName = _data_["username"]
            order_files = os.listdir(f"{__order_db_location__}/{customerName}")
            for order in order_files:
                allTable = PrettyTable(['ID', 'Name', 'Price', 'QTY'])
                with open(f"{__order_db_location__}/{customerName}/{order}", "r") as order_file:
                    order = json.load(order_file)
                    items = order["items"]
                    for item in items:
                        item_arr = [item["id"], item["name"], item["sellingPrice"], item["qty"]]
                        allTable.add_row(item_arr)
                    print("Order ID: ", order["id"])
                    print("Customer Name: ", customerName)
                    print(allTable)
        elif userRole == "admin":
            customerName = params[0]
            order_files = os.listdir(f"{__order_db_location__}/{customerName}")
            for order in order_files:
                allTable = PrettyTable(['ID', 'Name', 'Price', 'QTY'])
                with open(f"{__order_db_location__}/{customerName}/{order}", "r") as order_file:
                    order = json.load(order_file)
                    items = order["items"]
                    for item in items:
                        item_arr = [item["id"], item["name"], item["sellingPrice"], item["qty"]]
                        table.add_row(item_arr)
                    print("Order ID: ", order["id"])
                    print("Customer Name: ", customerName)
                    print(table)

def markComplete(params):
    if os.path.isfile(__current_session_location__):
        userRole = ""
        with open(__current_session_location__, "r") as item_file:
            _data_ = json.load(item_file)
            userRole = _data_["role"]
        if userRole == "admin":
            customerName = params[0]
            with open(f"{__order_db_location__}/{customerName}/{params[1]}.db", "r") as order_file:
                order = json.load(order_file)
                order["status"] = "completed"
                with open(f"{__order_db_location__}/{customerName}/{params[1]}.db", "w") as updated_order_file:
                    json.dump(order, updated_order_file)
                    print("Order status updated")       

# utility functions

def getLastID():
    if os.path.exists(__order_last_id__):
        with open(__order_last_id__, "r") as last_id_file:
            return int(last_id_file.readline())
    else:
        return 0

def updateLastID(id):
    with open(__order_last_id__, "w") as last_id_file:
        last_id_file.write(str(id))