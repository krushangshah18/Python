"""
def func(lst=[]):
    lst.append(1)
    print(lst)

func()
func()

Output :
[1]
[1,1]

Why? : When a function is defined, default arguments are evaluated only once, not every time the function is called.
"""

"""
DataClass Goal : goal is: Remove boilerplate, keep class readable
"""

class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return(f"Point(x={self.x}), y={self.y})")
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

p1 = Point(1, 2)
p2 = Point(2, 1)
print(p1, p2)
print(p1==p2)


### Whole above code can be reduced to 

from dataclasses import dataclass

@dataclass
class Point:
    x: int  #PY reads these fields and then creates 3 by default methods 
    y: int  # __init__, __repr__, __eq__ These can be modified based on your requirements

p1 = Point(1, 2)
p2 = Point(2, 1)
print(p1, p2)
print(p1==p2)

"""
https://docs.python.org/3/library/dataclasses.html#class-variables
"""

from dataclasses import dataclass,field

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    # sizes: list[str] = [] #WRONG Reason is demonstrated at beginning of the file So use "field"
    sizes :list[str] = field(default_factory=list) #we provide function which needs to be called on every instance creation 
    #list is mutable — using subjects=[] would share the same list across objects

    sizes :list[str] = field(default=("Something here"), init=False ) 
    #We can use default instead of default_factory if the value is immutable 
    # also we can decide if this fields should be included in some function or not here in __init__ its false so not included       
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
"""
How Dataclass will generate the __init__ for above code

def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
"""



####How include classVariable in the class 
from typing import ClassVar

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    thisWillBeClassVariable: ClassVar[int] = 200


#######Inheritance in data class

class Rectangle: #Base class is not data class
    def __init__(self, height, width):
        self.height = height
        self.width = width

@dataclass
class Square(Rectangle): #Child class is a dataclass
    side: float

    def __post_init__(self): #as parent is not data class so it wont tigger parents constructor
        super().__init__(self.side, self.side)


########Example where both of them are dataclass

@dataclass
class Rectangle: #Base class is a dataclass
    width: int
    height: int

@dataclass
class ColoredRectangle(Rectangle): #Child class is a dataclass
    color: str  #So both the constructors are called

rect = ColoredRectangle(10,20,"Green")

print(rect)


#######If you want to make classes immutable 

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    
p = Point(1, 2)
p.x = 10    # ❌ dataclasses.FrozenInstanceError
