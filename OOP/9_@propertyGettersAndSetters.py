"""
We can use functions return value as objects property
"""
"""
Use _name as the backing store to avoid recursion when implementing the property 
(calling self.name inside name would call the property again).
"""
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age=age

    @property
    def age(self): 
        return self._age
    
    @age.setter 
    def age(self,new):
        self._age = new

    @age.deleter 
    def age(self):
        del self._age 

obj = Person("KS",21)

print(obj.age)
obj.age = 22
print(obj.age)
del obj.age
# print(obj.age) #AttributeError: 'Person' object has no attribute '_age'. Did you mean: 'age'?



############Computed property example
from functools import cached_property
import time


class Rectangle:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    @property
    def area(self):
        return self._w * self._h
    
    @cached_property
    def cacheAarea(self): #once computed then wont be computed again until we delete the cache (deleteing this property or attribute)
        print("In Cached Fultion Expensive task being calculated")
        time.sleep(3)

        return self._w * self._h

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, v):
        if v <= 0: 
            raise ValueError("width>0 required")
        print("Updating Width")
        self._w = v

Robj = Rectangle(5,10)

# print(Robj.area)
# print(Robj.width)
print()
print()
print()
print()
print("CachedArea:",Robj.cacheAarea)
print("CachedArea:",Robj.cacheAarea)
print("area:",Robj.area)
Robj.width = 10
print("area:",Robj.area)
print("CachedArea:",Robj.cacheAarea)

del Robj.cacheAarea
print("CachedArea:",Robj.cacheAarea)
