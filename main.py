import click
from app.user import register, login, current
from app.items import addItem, viewAll, viewSingleItem, deleteItem
from app.cart import addToCart, viewCart, emptyCart

@click.command()
@click.option('--type', default='init', help='command type')
@click.argument('operation')
@click.argument('params', nargs=-1, required=False)
def hello(type, operation, params): 
    if type == "user":
        if operation == "register":
            register(params)
        elif operation == "login":
            login(params)
        elif operation == "current":
            current()
    elif type == "item":
        if operation == "add":
            addItem(params)
        elif operation == "view-all":
            viewAll()
        elif operation == "view":
            viewSingleItem(params)
        elif operation == "delete":
            deleteItem(params)
    elif type == "order":
        if operation == "add-cart":
            addToCart(params)
        elif operation == "view-cart":
            viewCart()
        elif operation == "clear-cart":
            emptyCart()
    else:
        print("Error")

if __name__ == '__main__':
    hello()