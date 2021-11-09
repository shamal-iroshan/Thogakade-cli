import os
import json
from prettytable import PrettyTable

__order_db_location__ = "db/orders"
__current_session_location__ = "db/session/current_session.db"
__order_last_id__ = "db/util/order_last_id.db"
__cart_db_location__ = "db/orders/cart/cart.db"
__item_db_location__ = "db/items"

table = PrettyTable(['ID', 'Name', 'Price', 'qty'])

def addToCart(params):
    if os.path.exists(__cart_db_location__):
        item = get_item_by_path(f"{__item_db_location__}/{params[0]}.db")
        item["qty"] = params[1]
        _data_ = {
            "items": [item]
        }
        if os.path.getsize(__cart_db_location__) == 0:
            with open(__cart_db_location__, "w") as cart_file:
                json.dump(_data_, cart_file)
            print("Item added to the cart")
        else:  
            with open(__cart_db_location__, "r") as cart_file:
                _cart_ = json.load(cart_file)
                item_arr = _cart_["items"]
                item_arr.append(item)
                _updated_data_ = {
                    "items": item_arr
                }
                with open(__cart_db_location__, "w") as cart_file:
                    json.dump(_updated_data_, cart_file)
                print("Item added to the cart")
    else:
        item = get_item_by_path(f"{__item_db_location__}/{params[0]}.db")
        item["qty"] = params[1]
        _data_ = {
            "items": [item]
        }
        with open(__cart_db_location__, "w") as cart_file:
            json.dump(_data_, cart_file)
        print("Item added to the cart")

def viewCart():
    if os.path.exists(__cart_db_location__):
        with open(__cart_db_location__, "r") as cart_file:
            _cart_ = json.load(cart_file)
            items = _cart_['items']   
        for i in items:
            table.add_row([i['id'], i['name'], i['sellingPrice'], i['qty']])
        print(table)

def emptyCart():
    open(__cart_db_location__, 'w').close()
    print("Cart cleared")

# utility functions

def getLastID():
    if os.path.exists(__order_last_id__):
        with open(__order_last_id__, "r") as last_id_file:
            return int(last_id_file.readline())
    else:
        return 0

def get_item_by_path(path):
    with open(path, "r") as item_file:
        _data_ = json.load(item_file)
        return _data_