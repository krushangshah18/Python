""" 
3 Ways to perform Polymorphism

- method overriding
- method overloading
- operator overloading
"""

##############method overloading

#By syntax its not possible to perform overloading but there is a workaroung to it

#This Way its not possible in Python as we used to do in java
class Geometry:
    def area(self, radius): 
        return 3.14* radius * radius
    
    def area(self,l,b):
        return l*b 
    
# obj = Geometry()
# print(obj.area(4)) #ERORRRRRRR


###Can perform This way
class Geometry:
    def area(self, a,b=0): 
        if b==0:
            print("Circle :", 3.14* a * a)
        else:
            print("Rectangle :",a*b) 
obj = Geometry()

obj.area(4)
obj.area(4,6)



###############operator overloading

a = "First Part"
b = "Second Part"
print(a+b) #here it performs concatenation

a=5
b=7
print(a+b) #here it performs addition