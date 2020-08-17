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
# import urllib.request
os.getcwd()
with open('Data/portfolio.csv', 'rt') as f:
    # data = f.read() #all data on one line
    # skip headers
    # headers = next(f)
    # print (headers)
    for line in f:
        print(line, end = '') # one line at a time

# fetching internet data
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()
  