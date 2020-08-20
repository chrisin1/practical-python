# pcost.py
#
# Exercise 1.27
import sys
import csv
import report
def portfolio_cost(filename):

    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % argv[0])
    cost = portfolio_cost(argv[1])
    print(cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)