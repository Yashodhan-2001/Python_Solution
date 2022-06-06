# class yash:
#     def __init__(self,name,company):
#         self.name=name
#         self.company=company
# vats=yash("Yashodhan","TCS") 
# print(vats.name) 
# print(vats.company)    


# class Parent:
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname  
#         self.lastname=lastname
#     def print(self):
#         print(self.firstname,self.lastname)
# cd=Parent("Yashodhan","Vats")
# cd.print() 
# class Child(Parent):
#     pass
# md=Parent("Yash","Sharma")
# # md.print()           
        
# class even:
#     def __init__(self,n):
#        self.n=n
#     def print(self):
#         if self.n%2==0:
#             print("True")
#         else:
#             print("False")    
# class evenchild(even):
#     def Wish(self):
#         print("Happy Birthday")
    
    
# md=even(3) # parent class object
# md.print()             
# cd=evenchild(40) # child class object
# cd.print()
# cd.Wish()           

# MULPIPLE INHERITANCE
# class Grandfather:
#     def __init__(self):
#         self.str1="Rajkumar Sharma"
#         print("Base 1")
# class Father:
#     def __init__(self):
#         self.str2="AMit Kumar Sharma"
#         print("Base 2")   
# class Me(Grandfather,Father):
#     def __init__(self):
#         Grandfather.__init__(self)
#         Father.__init__(self)
#         print("Derived class")
            
#     def Info(self):
#         print(self.str1,self.str2)  
# hi=Me()
# hi.Info() 
# MULTILEVEL INHERITANCE

class Grandfather:
    def __init__(self ,name):
        self.name=name
    def getName(self):
        return self.name    
    print("Base 1..............")
        
class Father(Grandfather):
    def __init__(self,name,age):
        Grandfather.__init__(self,name)
        self.age=age
    def getAge(self):
        return self.age    
    print("Basee 2...............")    
class Son(Father):
    def __init__(self,name ,age,address):
        Father.__init__(self,name,age) 
        self.address=address
    def getAddress(self):
        return self.address
    print("Base 3..............")
give=Son("Rajkumar Sharma   ", 45 ,"  South Rampuri MZN h no 354647") 
print(give.getName(),give.getAge(),give.getAddress())                   
                    

