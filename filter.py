# def even(num):
#     varibles=[1,2,3,4,5,6,7,8,9]
#     if num in varibles:
#         if num%2==0:
#             return True
#     else:
#         return False
# lis=[1,2,3,4,5,6,7,8,9]
# result=filter(even,lis)
# print(list(result))


lis=[1,2,3,4,5,6,7,8,9]
result=filter(lambda x:x%2==0,lis)
print(list(result))

