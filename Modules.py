# MATH MODULE
# from math import*
# import math 
# # import sys
# print(sqrt(8))
# print(factorial(4))
# # print(dir(math))
# print(int(pow(2,5)))
# print(math.pi)
# print(math.sin(2))

# DIR Function
# import random
# print(dir(random))

#  DATETIME MODULE

from datetime import date
mydate=date(2001,2,21)
print("My birthday date is ",mydate)

# CURRENT DATE FUNCTION

from datetime import *
my_date=date.today()
print("Toaday date is ",my_date)
print("Toady year ",my_date.year)
print("Toady month ",my_date.month)
print("Toady date ",my_date.day)

str=date.isoformat(my_date)
print(my_date)
print(type(str))