import os

__order_db_location__ = "db/orders"
__util_location__ = "db/util"
__cart_db_location__ = "db/orders/cart"
__item_db_location__ = "db/items"
__user_db_location__ = "db/users"
__current_session_location__ = "db/session"


def init():
    if not os.path.exists('db/'):
        os.makedirs(__order_db_location__)
        os.makedirs(__util_location__)
        os.makedirs(__cart_db_location__)
        os.makedirs(__item_db_location__)
        os.makedirs(__user_db_location__)
        os.makedirs(__current_session_location__)
        print("Database initialized.!")
    else:
        print('Database already initialized')