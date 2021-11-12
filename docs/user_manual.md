# Instructions

## Initialize Database
```
init
```

## User

### Register
```
--type user register <username> <password> <role>
```

### Login
```
--type user login <username> <password>
```

### View Current User
```
--type user current
```

## Item

### Add
```
--type item add <name> <buyingPrice> <sellingPrice>
```
### View All
```
--type item view-all
```
### View Single Item
```
--type item view <id>
```
### Delete Item
```
--type item delete <id>
```

## Cart

### Add item to cart
```
--type order add-cart <itemID> <qty>
```
### Clear cart
```
--type order clear-cart
```

### View cart
```
--type order view-cart
```

## Order

### Add Order
```
--type order place-order
```

### View Single Order As a customer
```
--type order view-single-order <id>
```

### View Single Order As a admin
```
--type order view-single-order <customer name> <order id>
```

### View All Orders As a customer
```
--type order view-all-orders
```

### View All Orders As a admin
```
--type order view-all-orders <customer name>
```

### Mark order as complete(only admin can do)
```
--type order mark-complete <customer name> <order id>
```