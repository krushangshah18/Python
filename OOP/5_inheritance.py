""" Inheritance : is-a relationship """
"""
When Class B inherits from class A it inherits the following things :

- Data members
- methods
- constructor

NOTE : Private members are not inherited
"""

#################Basic Inheritance :
class User:
    def login(self):
        print("Login")
    def register(self):
        print("Register")
    
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

u = Student()
#u = User()
u.enroll()
u.review()
u.login()
u.register()


#####################Inheritance where Partent constructor called and private var
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self._brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s=SmartPhone (20000, "Apple", 13)

# print(s.__brand) #CAMMOT ACCESS ERROR


############################Polymorphism : Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone (20000, "Apple", 13)
s.buy()



###################Note: If child constructor is present then parent constructor WONT be called
class Parent:
    def __init__(self,num): #This wont be called therefor num variable is not created
        self.__num=num
    
    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
    
son = Child(100,10)
# print("Parent: Num:",son.get_num())


#################Super Keyword :

class Phone:
    def __init__ (self, price, brand, camera):
        print ("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        super().buy() #Super can be used to invoke parents method or constructors 
        

s=SmartPhone(20000, "Apple", 13)
s.buy()

# s.super().buy() #super keyword dosnt works outside the class this is WRONG


##################Another Example for Super :

class Phone:
    def __init__ (self, price, brand, camera):
        print ("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print ("Inside smartphone constructor at Start")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor at End")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)
print(s.os)
print(s.brand)



"""
Type of inheritance :

- Single Level : father -> child
- multi-Level : GrandFather -> father -> child
- hierarchical : One Parent two siblings
- multiple : Diamond - B,c->D //D inherits both B and C

"""

##########################multiple inheritance examples :

class Phone: 
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone (Phone, Product): 
    """
    SmartPhone Dosent have Constructor so phone's constructor is called as its precedence is first while inheriting
    and if phone also dosent have the constructor then products constructo is called
    """
    pass

s=SmartPhone(20000, "Apple", 12)
s.buy()
s.review()


#### EG-2

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

class SmartPhone (Product, Phone):
    """
    MRO : Method Resolution order

    in case of conflict eg buy method is called it would start from left to right inherited classes and 
    find the buy method first product then phone 

    in this case it will execut product's buy method first
    """
    pass

s=SmartPhone(20000, "Apple", 12)
s.buy()