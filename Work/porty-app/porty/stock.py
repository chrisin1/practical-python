from .typedproperty import String, Integer, Float
class Stock:
    
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def sell(self, amt):
        self.shares -= amt
        return self.shares * self.price
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        return self.shares * self.price  