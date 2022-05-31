# open file for reading
# f=open("reading.txt",'r')
# print(f.read())
# f.close()

# open file for Writing

# f=open("Writing.txt","w")
# f.write("Suno yash ek bhut hi bdiya banda hai aur amart bhi hai")
# f.close

# open a file in append mode

# f=open("append.txt","a")
# f.write("Yash ek bhut hi bdiya bnda hai ")
# f.close

# open file in W+ mode

f=open("WriteRead.txt","w+")
f.write("YAsh is a very talented guy")
content=f.read()
print(content)
f.close()