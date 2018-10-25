# coding: utf-8


class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight + self.price



if __name__ == '__main__':
    item1 = LineItem('aaa', 10, 10)
    item2 = LineItem('bbb', 20, 20)
    item3 = LineItem('ccc', 30, 30)

    items = [item1, item2, item3]
    
    keys = ['description', 'weight', 'price']
    for i in range(3):
        print('ITEM #{}'.format(i+1))
        for key in keys:
            print(getattr(items[i], key))
    print(item1.weight, item2.price)
