#Demo for baasic class, object, self and constructor concepts in Python OOP
import time
class Car:
    # Constructor to initialize the car objects
    def __init__(self, company, name, year):
        self.company = company
        self.name = name
        self.year = year
        self.state = 'stopped'
    
    def display_info(self):
        return f"Car: {self.company} {self.name}, Year: {self.year}"
    
    def age(self):
        current_year = time.localtime().tm_year
        return current_year - self.year
    
    def startCar(self):
        self.state = 'running'
        return f"{self.name} is now {self.state}"
    
    def stopCar(self):
        self.state = 'stopped'
        return f"{self.name} is now {self.state}"

    """
    Magic/Dunder Method : 
        These are the methods which a not called by the object but triggered at certaing conditions 
        Eg : __init__, __str__, __add__, __sub__, __mul__, __truediv__ .....

        https://www.tutorialsteacher.com/python/magic-methods-in-python
    """

    def __str__(self): #This is triggered when we pass our object in print()
        #always returns String
        return f"{self.company} {self.name} ({self.year}) - Age: {self.age()} years"
    

    
# Creating objects of the Car class
car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2018)

print(car1.display_info()) #self is passed automatically even if its not mentioned during the call
print(car2)

"""
About Self :
- In Python, 'self' refers to the instance of the class. (self in nothing but object of the class itself)
- It is used to access variables and methods associated with the current object. 
- When you define methods in a class, you must include 'self' as the first parameter to allow access to instance 
attributes and other methods within the class. 
- When you call a method on an object, Python automatically passes the object as the first argument to the method, 
which is why you don't need to provide it explicitly during the call.
"""

"""
Why do we Need To have self as first argument in every method of the class? :

A class can have Data and Methods and these two can only be accessed by the objects of the class So to call 
a method within same class also we need it to call as self.methodName 

therefore self is also the object itself
"""

