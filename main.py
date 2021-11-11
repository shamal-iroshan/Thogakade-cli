import click
from app.user import User
from app.items import Items
from app.cart import Cart
from app.orders import Orders
from app.util import Util

util = Util()
cart = Cart()
items = Items()
orders = Orders()
user = User()

@click.command()
@click.option('--type', default='init', help='command type')
@click.argument('operation')
@click.argument('params', nargs=-1, required=False)
def hello(type, operation, params): 
    if type == "user":
        if operation == "register":
            user.register(params)
        elif operation == "login":
            user.login(params)
        elif operation == "current":
            user.current()
    elif type == "item":
        if operation == "add":
            items.addItem(params)
        elif operation == "view-all":
            items.viewAll()
        elif operation == "view":
            items.viewSingleItem(params)
        elif operation == "delete":
            items.deleteItem(params)
    elif type == "order":
        if operation == "add-cart":
            cart.addToCart(params)
        elif operation == "view-cart":
            cart.viewCart()
        elif operation == "clear-cart":
            cart.emptyCart()
        elif operation == "place-order":
            orders.placeOrder()
        elif operation == "view-single-order":
            orders.viewSingleOrder(params)
        elif operation == "view-all-orders":
            orders.viewAllOrders(params)
        elif operation == "mark-complete":
            orders.markComplete(params)
    elif type == "init": 
        util.init()
    else:
        print("Error")

if __name__ == '__main__':
    hello()