import functools
num1=[1,2,3,4,5,6,7,8,9]
result=functools.reduce(lambda x,y: x*y,num1)
print(result)
