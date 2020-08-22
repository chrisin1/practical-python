class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def sell(self, amt):
        self.shares -= amt
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'