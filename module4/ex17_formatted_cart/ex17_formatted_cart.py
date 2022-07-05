class Cart:
    pass


class Item:
    pass


if __name__ == '__main__':
    cart = Cart()
    cart.add(Item(1.5, 'kg', 'tomatoes', 5))
    cart.add(Item(2, 'kg', 'cucumbers', 4))
    cart.add(Item(1, 'tube', 'toothpaste', 2))
    cart.add(Item(1, 'box', 'tissues', 4))
    print(f'Your cart contains: {cart:short}')
    print(f'Your cart: {cart:long}')
