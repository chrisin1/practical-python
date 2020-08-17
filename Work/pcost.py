# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename):

    with open(filename, 'rt') as f:
        # data = f.read() #all data on one line
        # skip headers
        headers = next(f)
        # print (headers)
        total = 0.0
        for line in f:
            row = line.split(',')
            count = int(row[1]) #converts first column to ints
            price = float(row[2]) #takes second column, removes \n, and converts to float
            # price = price
            total += (count * price)
        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(cost)