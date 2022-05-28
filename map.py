# hello=[1,2,3,4,5,6,7,8,9]
# result=map(lambda x:x%2==0,hello)
# print(list(result))

# def even(number):
#     if number%2==0:
#         return number
#     else :
#         return "odd"
# number=(1,2,3,4,5,6)   
# result=map(even,number) 
# print(list(result))

number1=(1,2,3,4,5,6,7,8,9)
number2=(9,8,7,6,5,4,3,2,1)
result=map(lambda x,y:x*y,number1,number2)
print(list(result))