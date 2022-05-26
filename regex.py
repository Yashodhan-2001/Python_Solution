# import re
# txt="This is Me"
# x=re.search("^This .*Me$",txt)
# if x:
#     print("YEs! it is present")
# else:
#     print("Not present")    

# import re
# match =re.search(r'Yashodhan','''is a good boy Yashodhan''')
# print(match)
# print(match.group())
# print(match.start())
# print(match.end())


import re
matches="Yes this computer is very expensive and tis computer have lotrs of fetures and apps also this computer is solid for playing any type of games"
result=re.findall(r'[Cc]omputer',matches)
print(result)