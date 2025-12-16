"""
A decorator is a function that:
    - Takes another function
    - Adds extra behavior
    - Returns a new function
    - Without changing the original function’s code
"""


import time
#implementing Cache using Decorators
def cache(func):

    cacheValues={}
    def wrapper(*args):
        print(f"Arguments are : {args} and method is {func.__name__}") 

        if args in cacheValues:
            return cacheValues[args] 
        result = func(*args)
        cacheValues[args] = result
        return result
    
    return wrapper

@cache #equivalent to temp = cache(longRunningFunc(a,b))
def longRunningFunc(a,b):
    time.sleep(2)
    return a + b

print(longRunningFunc(3,4))
print(longRunningFunc(5,4))
print(longRunningFunc(3,4)) 


#Chaining Decorators (ORDER MATTERS)
def deco1(func):
    def wrapper():
        print("deco1")
        return func()
    return wrapper

def deco2(func):
    def wrapper():
        print("deco2")
        return func()
    return wrapper

@deco1
@deco2 # func = deco1(deco2(f)) : Bottom one runs first.
def f():
    print("Function")

f()

print()
print()

def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before")
        result = func(*args,**kwargs)
        print("After")
        return result

    return wrapper

@decorator
def sayHi():
    print("HI")

# sayHi = decorator(sayHi) # if @decorator is not mentioned over the sayhi function
# sayHi()

sayHi()
"""
Step 1: Understand This Line (MOST IMPORTANT)
    @decorator
    def say_hi():
        print("Hi")
    
    say_hi()

Python does NOT execute this magically.

It rewrites it as:

    def say_hi():
        print("Hi")

    say_hi = decorator(say_hi)
"""
#
"""
Step 2: What Does decorator(say_hi) Return?

From your code:

    def decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper


So:
    decorator(say_hi)   →   wrapper

That means:
    say_hi = wrapper


⚠️ IMPORTANT
    The name say_hi now points to wrapper, NOT the original function
"""
#
"""
Step 3: Where Is wrapper() Actually Called?

Now look at this line:
    say_hi()

But remember:
    say_hi = wrapper

So this is really:
    wrapper()

That’s it.
That’s how wrapper gets executed.
"""


###########Decorator with PARAMETERS (Decorator Factory)
from functools import wraps
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(n):
                print(f"Before {i}")
                result = func(*args,**kwargs)
                print(f"After {i}")
        return wrapper
    return decorator

@repeat(5)
def helloBolo(nm):
    print(f"Hello {nm}!!!")


helloBolo("KS")

print(helloBolo.__name__) #This outputs wrapper therefore loss of metadata so use @wraps(func)
#functools.wraps preserves the original function’s metadata when using decorators

##########some important Built-in Decorators
"""
| Decorator       | Purpose               |
| --------------- | --------------------- |
| `@staticmethod` | Method without `self` |
| `@classmethod`  | Method with `cls`     |
| `@property`     | Attribute-like access |
| `@lru_cache`    | Memoization           |
| `@dataclass`    | Auto boilerplate      |
"""


"""
Decorator vs Decorator Factory
This is about how many layers of functions you have

- A decorator is a function that Takes a function and Returns a function
- A decorator factory is a function that returns a decorator, allowing decorators to accept arguments.

def repeat(n):                # 1️⃣ factory
    def decorator(func):      # 2️⃣ decorator
        def wrapper(*args, **kwargs):  # 3️⃣ wrapper
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
"""