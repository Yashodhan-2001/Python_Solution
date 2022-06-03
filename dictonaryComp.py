# lis=[1,2,3,4,5,6,6,7,8]
# dic={var:var*2 for var in lis if var%2!=0}
# print(dic)


# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
  
# dict_using_comp = {key:value for (key, value) in zip(state, capital)}
  
# print("Output Dictionary using dictionary comprehensions:", 
#                                            dict_using_comp)


# lis=[1,2,3,4,5,6,7,8,9]
# dic_cube={var:var*var*var for var in lis if var%2==0}
# print(dic_cube)

lis=[1,2,3,5,6,7,8,9]
dic={var:var for var in lis if var%2==0}
print(dic)

lia=[1,2,3,4,5,6,7,8,9]
lim=[9,8,7,6,5,4,3,2,1]
dic={key :value for (key,value)in zip(lia,lim)}
print(dic)