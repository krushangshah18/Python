"""
Descriptor Class : used to define common behaviour for a propert or attribute
"""

"""
Use Case Example : can create a descriptor class when the getters and setters needs to be same for more than one attribute

ex: we have price and qty and both needs =ve numbers so we can use common descriptor for them 
"""

#######This is Descriptor class
class PositivNumber:
    def __init__(self):
        self.name = None 

    def __set_name__(self,owner,name): #links the instance of PositiveNumber with attribute its assigned to
        #The owner will be the class name here its Product and name will be the attribue price/quantity 
        self.name = name

    def __get__(self,instance,owner):
        #instance of the product class AND owner is the class
        print(f"I AM CALLED GET")
        return instance.__dict__.get(self.name,0) #Its Dictionary so if key not found default is 0
    
    def __set__(self,instance,value):
        print(f"I AM CALLED SET")
        if value < 0:
            raise ValueError(f"{self.name} Must be Positive")
        instance.__dict__[self.name] = value


class Product:
    price = PositivNumber() #This will trigger dunder method __set_name__
    quantity = PositivNumber()

    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity


p = Product(99,50)

print(p.price)
print(p.quantity)

# p.price = -10 #ValueError: price Must be Positive