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
"""
Operator overloading lets objects of your custom classes behave like built-in types 
when you use operators such as +, -, *, ==, <, [], etc.

In Python, this is achieved by defining special (magic / dunder) methods like __add__, __eq__, __lt__, etc.
"""
"""
Without operator overloading:
    p1.add(p2)

With operator overloading:
    p1 + p2
"""


"""
Arithmetic Operators
| Operator | Method         |
| -------- | -------------- |
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |
| `%`      | `__mod__`      |
| `**`     | `__pow__`      |
"""
"""
Comparison Operators
| Operator | Method   |
| -------- | -------- |
| `==`     | `__eq__` |
| `!=`     | `__ne__` |
| `<`      | `__lt__` |
| `<=`     | `__le__` |
| `>`      | `__gt__` |
| `>=`     | `__ge__` |
"""
"""
Unary Operators
| Operator   | Method    |
| ---------- | --------- |
| `-obj`     | `__neg__` |
| `+obj`     | `__pos__` |
| `abs(obj)` | `__abs__` |

Augmented Assignment
| Operator | Method     |
| -------- | ---------- |
| `+=`     | `__iadd__` |
| `-=`     | `__isub__` |

"""
a = "First Part"
b = "Second Part"
print(a+b) #here it performs concatenation

a=5
b=7
print(a+b) #here it performs addition


"""
Reverse Operators (__radd__, __rsub__, …)

The Core Question

When Python sees:
    a + b

Which object’s code should run?
    👉 Python always tries LEFT operand first.

So it tries:
    a.__add__(b)

2. What If a Does NOT Know How to Add b?
Example:
    10 + my_object

    - 10 is an int
    - int does not know how to add your custom object
    So:
        int.__add__(my_object)   # ❌ Not supported

Now what?
    👉 Python gives RIGHT operand a chance

It calls:
    my_object.__radd__(10)
    This is called a reverse operator.

3. Rule (MEMORIZE THIS)
    For: a + b

Python tries in this exact order:
    - a.__add__(b)
    - If that fails or returns NotImplemented → b.__radd__(a)
    - If both fail → TypeError

    
Type Checking & NotImplemented (IMPORTANT)
Never assume other is the same type.

def __add__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return Point(self.x + other.x, self.y + other.y)
"""