# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def parse_csv(lines, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')
    
    rows = csv.reader(lines, delimiter = delimiter)
    # Read the file headers
    records = []
    headers = next(rows) if has_headers else []
    if select:
        indices = [headers.index(column) for column in select]
        headers = select
    else:
        indices = []
    for rowNum, row in enumerate(rows, start = 1):
        if not row:    # Skip rows with no data
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try: 
                row = [func(val) for func, val in zip(types, row)]
                if headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError:
                if not silence_errors:
                    print(f'Row {rowNum}: Couldn\'t convert {row} ')
            

    return records

#badPortfolio1 = parse_csv('Data/portfolio.csv', select = ['name', 'shares'], has_headers=False)
# portfolio2 = parse_csv('Data/portfolio.csv', types = [str, int, float])
# portfolio3 = parse_csv('Data/prices.csv', types = [str, float], has_headers = False)
# portfolio4 = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
# badPortfolio2 = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors = True)
# print(badPortfolio2)

