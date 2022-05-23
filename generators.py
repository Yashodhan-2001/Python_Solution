
def gen(n):
    for i in range(n):
        yield i
g=gen(5)
print(g.__next__())   #0    
print(g.__next__())     #1
print(g.__next__())     #2
print(g.__next__())     #3
print(g.__next__())     #4
     