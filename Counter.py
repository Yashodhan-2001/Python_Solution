from collections import Counter
import collections
from typing import OrderedDict
# print(Counter([1,2,2,3,3,3,4,5,6,7,2,3,4,5,6,7,8,]))

# print(Counter({'A','A','A','B','B','B','B','B','C','C','C','D','D','D','E','E','E','E','E','E','E','E','E','E'}))

# yash=collections.Counter([1,2,3,4,5,6,7,3,2,4,5,6,7,8,9,1,2,3,4,5,5,6,6,7,8,9,7,5,5])
# print(yash)
# yash=collections.Counter(('a','a','a','b','b','c','d','d','d','e','e','e','f'))
# print(yash)

shri=collections.Counter(['yash','yash','laddu','laddu','suraj','suraj','suraj','suraj','suraj','yash','amit,'])
print(shri)

# example of subtraction

# python=collections.Counter()
# java=collections.Counter()
# python.update(A=10,B=30,C=40)
# java.update(A=20,B=40,C=90)
# print(java-python)



#  use of elements function

# count=Counter([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,6,7,7])
# yash=Counter(A=10,B=30,C=90)
# print(count)
# print(list(count.elements()))
# print(list(yash.elements()))

# most_Common function use

# count=Counter({"A":200,"B":300,"C":700,"D":500})
# for keys,values in count.most_common(3):
#      print('%s: %d' % (keys, values))
    
dc=OrderedDict()
print("Before dict")
dc['a']=10
dc['b']=20
dc['c']=30
dc['d']=40
for key,values in dc.items():
    print(key,values)
dc.pop("b")
dc["b"]=40
print("after dict")
for key,values in dc.items():
    print(key,values)    