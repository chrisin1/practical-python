# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint
def read_portfolio(filename):
    # tuple version
    # with open(filename, 'rt') as f:
    #     # data = f.read() #all data on one line
    #     # skip headers
    #     rows = csv.reader(f)
    #     headers = next(f)
    #     # print (headers)
    #     portfolio = [] #empty list
    #     for row in rows:
    #         #print(row)
    #         holding = (row[0], int(row[1]), float(row[2]))  #tuple container
    #         portfolio.append(holding)
    #     return portfolio

    # dict version
    with open(filename, 'rt') as f:
        # data = f.read() #all data on one line
        # skip headers
        rows = csv.reader(f)
        headers = next(f)
        # print (headers)
        portfolio = [] #empty list        
        for row in rows:
            #print(row)
            prices = {} # Initial empty dict
            prices['name'] = row[0]
            prices['shares'] = int(row[1])
            prices['price'] = float(row[2])
            portfolio.append(prices)
        return portfolio

total = read_portfolio('Data/portfolio.csv')
pprint(total)

