# Instructions

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

## Cart

### Add item to cart
```
--type order add-cart <itemID> <qty>
```

### Clear item from cart
```
--type order clear-item <itemID>
```

### Clear cart
```
--type order clear-cart
```

### View cart
```
--type order view-cart
```