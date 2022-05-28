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

# Character metadat uses
# import re
# matches="Yes this computer is very expensive and tis computer have lotrs of fetures and apps also this computer is solid for playing any type of games"
# result=re.findall(r'[Cc]omputer',matches)
# print(result)

# import re 
# text="It is me and here It my hood no one Will be there"

# result=re.findall(r'there$',text)
# if result:
#     print("YEs i am here")
# else:
#     print("Acha chlta hu duio mai yaad rkhna")    

# import re

# text ="Yash is a programmer"
# result=re.findall(r'Y...h',text)
# print(result)

# import re
# txt=" helo hello yash"
# result=re.findall(r'he.+o',txt)
# print(result)

# import re
# txt=" ho"
# result=re.findall(r'h.+o',txt)
# print(result)

# import re
# txt="Yash hello"
# result=re.findall(r"he.?o",txt)
# print(result)

# import re
# text="hello yash"
# result=re.findall(r"he.{2}o",text)
# print(result)

# import re
# txt="This is yash from up uttar pradesh"
# result=re.findall(r"mzn|yash",txt)
# print(result)
# if result:
#     print("Yes got 1 string from the container")
# else:
#     print("No bad luch please next time")    

# import re 
# txt="This is my bike"
# result=re.split(r"\s",txt,2)
# print(result)

# import re
# txt="This is my car"
# result=re.sub(r"\s","4",txt)
# print(result)

# import re
# txt="this is may car"
# result=re.sub("\s","4",txt,1)
# print(result)

import re
txt="the rain in my heart are u able to see that beauty"
result=re.sub("\s","10",txt,4)
print(result)
