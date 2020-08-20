# writing a function
# import math
# def sum(num):
#     total = 0
#     for i in range(num + 1):
#         total += i
#     return total

# a = sum(100)
# print(a) 
# 
# 
# reading a file
import os
import sys
# import urllib.request
# os.getcwd()
# with open('Data/portfolio.csv', 'rt') as f:
#     # data = f.read() #all data on one line
#     # skip headers
#     # headers = next(f)
#     # print (headers)
#     for line in f:
#         print(line, end = '') # one line at a time

# fetching internet data
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()


# working with sequences and iteration
# iteration
# points = [
#   (1, 4, 1),(10, 40, 1),(23, 14, 2),(5, 6, 3),(7, 8, 4)
# ]
# for x, y in enumerate(points, start = 1):
#     print ('Coord ' + str(x) + ": ", end =""),
#     print(y, end = '')
#     print("hi")  


# a = [0,1,2,3,4,5,6,7,8]
# b = a[2:5]
# b[0] = 500
# print(a)
# print(b)

# #zip function
# columns = ['column1', 'column2', 'column3']
# rows = ["row1", 'row2', 'row3']
# pairs = zip(columns, rows)
# for column, row in pairs:
#     print(column + ' ' + row)
# def go_do_something(num):
#     num + 1
# try:
#     go_do_something('ye')
# except Exception as e:
#     print('Computer says no. Reason :', e)
#     raise
print(sys.path)
