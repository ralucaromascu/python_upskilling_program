class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __format__(self, format_spec):
        if format_spec == 'short':
            new_list = sorted([item.name for item in self.items])
            return ', '.join(new_list)
        elif format_spec == 'long':
            return '\n'.join(str(item) for item in sorted(self.items, key=lambda x: x.name))
        else:
            raise TypeError('unsupported format string passed to Cart.__format__')


class Item:
    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        try:
            self.price = float(price)
        except ValueError as e:
            print(e)

    def __str__(self):
        return f'{self.quantity:5} {self.measure:5} {self.name:10} @ ${self.price}...$' \
               f'{self.quantity*self.price}'


if __name__ == '__main__':
    cart = Cart()
    cart.add(Item(1.5, 'kg', 'tomatoes', 5))
    cart.add(Item(2, 'kg', 'cucumbers', 4))
    cart.add(Item(1, 'tube', 'toothpaste', 2))
    cart.add(Item(1, 'box', 'tissues', 4))
    print(f'Your cart contains: {cart:short}')
    print(f'Your cart:\n{cart:long}')
