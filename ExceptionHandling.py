


# def div(n):
#     h=n/0
#     print(b)
# try:
#     div(3)  
#     div(5)
# except ZeroDivisionError:
#     print("ZeroDivisiorError Occured and handled")  
# except NameError:    
 #      print("Name error occured and handled")
# try:
#     k=5//0
# except ZeroDivisionError:
#     print("Zero Division Error and handled")
# finally:
#     print("This has to be execute")   
    
    
# x=-1
# if x<0:
#     raise Exception("no beloW 0")   

# try:
#     y=int(input("enter the value of y  "))

#     if y<2999:
#         raise ValueError("Money needs to be added")   
#     else:
#         print("fine")
# except ValueError as e:
#     print(e)
            
            
def even(n):
    try:
        if n%2==0:
            print("No is even")
            
        else:
            print("Everthing looks fine but unfortuneately got odd no")
    except Exception as e:
        print(e)
even(13)        
                            