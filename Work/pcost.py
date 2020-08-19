# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):

    with open(filename, 'rt') as f:
        # data = f.read() #all data on one line
        # skip headers
        rows = csv.reader(f)
        headers = next(rows)
        # print (headers)
        total = 0.0
        for rowNum, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row)) #zip allows you to read data without hardcoding a fixed file format
            try:
                count = int(record['shares']) #converts first column to ints
                price = float(record['price']) #takes second column, removes \n, and converts to float
                # price = price
                total += (count * price)
            except ValueError:
                print(f'Row {rowNum}: Bad row: {row}')            
        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'
cost = portfolio_cost(filename)
print(cost)