#Defining and calling a function
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

#different ways to pass arguments

# 1. Positional Arguments
def add(a,b):
    return a+b
print(add(2,3))  # 5

# 2. Keyword Arguments
def person(name ,age):
    print(f"{name} is {age} years old")

person("Bob",25)
person(age=30, name="Sam")
person(name="John", age=22)

# 3. Default Arguments
def multiply(a, b=2):
    return a * b
print(multiply(3))
print(multiply(3, 4))


"""Variable-Length Arguments in Functions"""
"""
1. *args — Multiple Positional Arguments
- Used when you want to pass any number of positional (non-keyword) arguments.
- Inside the function, args becomes a tuple.
"""
def total(*args):
    print(args) 
    print(type(args)) #tuple
    return sum(args) #10

print(total(1,2,3,4))

"""
2. **kwargs — Multiple Keyword Arguments
- Used when you want to pass any number of keyword (name=value) arguments.
- Inside the function, kwargs becomes a dictionary.
"""
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
info(name="Alice", age=30, city="NY")


"""Recursion"""
def factorial(n):
    if n==1:
        return 1
    
    return n*factorial(n-1)

print(factorial(5))

"""Built-in Functions"""
"""
| Function                    | Description                   |
| --------------------------- | ----------------------------- |
| `print()`                   | Display output                |
| `input()`                   | Take user input               |
| `len()`                     | Returns length of a sequence  |
| `type()`                    | Shows type of a variable      |
| `sum()`                     | Adds items in iterable        |
| `max()`, `min()`            | Maximum / Minimum values      |
| `range()`                   | Generates sequence of numbers |
| `sorted()`                  | Returns sorted list           |
| `int()`, `float()`, `str()` | Type conversion               |
| `abs()`                     | Absolute value                |
| `round()`                   | Rounds number                 |
"""

"""Some commonly used Built-in functions"""
#zip() : Combines two or more iterables element-wise into tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

#enumerate() : Adds a counter to an iterable and returns it as an enumerate object
fruits = ['apple', 'banana', 'cherry']
for i,fruit in enumerate(fruits):
    print(i, fruit)
for i,fruit in enumerate(fruits,start=5):
    print(i, fruit)

#sorted()
nums = [5, 2, 9, 1]
print(sorted(nums))           # [1, 2, 5, 9]
print(sorted(nums, reverse=True))  # [9, 5, 2, 1]

#Custom key sorting
students = [("A", 21), ("B", 18), ("C", 25)]
print(sorted(students, key=lambda x: x[1]))

#any() and all() : Returns True if ANY element is true / ALL elements are true
values = [0, False, 3, ""]
print(any(values))   # True  (because 3 is truthy)

marks = [80, 75, 90, 60]
print(all(marks))  # True

values = [1, 2, 0]
print(all(values)) # False (0 is false)


"""Lambda Functions : has Only one expression and its an anonymous (nameless) function"""
f = lambda x,y : x+y 
print(f(2,3))


"""Docstring"""
def add(a, b):
    """This function adds two numbers."""
    return a + b
print(add.__doc__)


############## Nested Functions

def outer():
    def inner():
        print("I am here")
    inner()

outer()

#Returning the inner function
def outer():
    def inner():
        print("I am here")
    return inner

f = outer()
f()


################# Closure
"""
A closure is a function that remembers variables from its enclosing scope, even after that scope has finished execution
"""

def outer():
    x = 10

    def inner():
        print(f"Value of x = {x}") #Closure

    return inner

f = outer()
f()

#Modifying Enclosed Variables
def outer():
    x = 10
    def inner():
        nonlocal x # in using nonlocal : 
        #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
        x += 1
        print("Inner X : ",x)
    
    print("outer before calling inner X : ",x)
    inner()
    print("outer After calling inner X : ",x)

outer()


#########IMP : Closures capture variable, not value
funcs = []
for i in range(3):
    def f():
        print(i)
    funcs.append(f)

for f in funcs:
    f()

"""
2
2
2
"""