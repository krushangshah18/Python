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

@cache
def longRunningFunc(a,b):
    time.sleep(2)
    return a + b

print(longRunningFunc(3,4))
print(longRunningFunc(5,4))
print(longRunningFunc(3,4)) 


#Chaining Decorators
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
@deco2
def f():
    print("Function")

f()

