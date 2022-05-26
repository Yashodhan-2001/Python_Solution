# strv="Yashodhan"
# ite=iter(strv)
# print(ite.__next__())#Y
# print(ite.__next__())#a
# print(ite.__next__())#s
# print(ite.__next__())#h
# print(ite.__next__())#o
# print(ite.__next__())#d
# print(ite.__next__())#h
# print(ite.__next__())#a
# print(ite.__next__())#n


def sq(n):
    for i in range(n):
        yield i*i
ans=sq(6)
print(next(ans))    
print(next(ans))   
print(next(ans))  
print(next(ans))   
print(next(ans))   

