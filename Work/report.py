# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint
from collections import Counter
def read_portfolio(filename):
    '''
    Read stock from a CSV file of name,price data
    '''
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
        headers = next(rows)
        # print (headers)

        
        portfolio = [] #empty list        
        for rowNum, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row)) #zip allows you to read data without hardcoding a fixed file format
            #print(record)
            try:
                stock = {} # Initial empty dict
                stock['name'] = record['name']
                stock['shares'] = int(record['shares'])
                stock['price'] = float(record['price'])
                portfolio.append(stock)
            except ValueError:
                print(f'Row {rowNum}: Bad row: {row}')         
        return portfolio

def print_report(report):
    headers = ('Name', 'Shares', 'Price')
    print('%10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f' % (row['name'], row['shares'], row['price']))

report = read_portfolio('Data/portfolio.csv')
print(report)
print_report(report)



# portfolio = read_portfolio('Data/portfolio.csv')
# portfolio2 = read_portfolio('Data/portfolio2.csv')

#list 
# cost = sum([s['shares'] * s['price'] for s in portfolio]) 
# more100 = [ s for s in portfolio if s['shares'] > 100 ]
# msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
# print(cost)
# print(more100)
# print(msftibm)

# #set 
# names = { s['name'] for s in portfolio }
# stock = { s['price'] for s in portfolio}
# # print(names)

# #dictionary 
# holdings = Counter()
# for s in portfolio:
#     holdings[s['name']] += s['shares']

# holdings2 = Counter()
# for s in portfolio2:
#     holdings2[s['name']] += s['shares']

# #print(holdings)
# #print(holdings['MSFT'])
# print(holdings.most_common(3))

# combined = holdings + holdings2
# print(combined)
# #holdings = { name: 0 for name in names }
# #holdings.items()