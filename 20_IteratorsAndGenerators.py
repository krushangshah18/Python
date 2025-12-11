import sys

L = [x for x in range(1,100000)] #Stores complete list in memory
print(sys.getsizeof(L)/1024, "KB OR",sys.getsizeof(L), "Bytes") 

X = range(1,10000000000000) #Uses range object which is an iterator, does not store all values in memory
print(sys.getsizeof(X)/1024, "KB OR",sys.getsizeof(X), "Bytes")


#Understanding Iterators
L = [1,2,3,4]
iterOfL = iter(L) #Creating an iterator from the list it has __iter__ and __next__ methods

print(next(iterOfL)) #1
print(next(iterOfL)) #2
print(next(iterOfL)) #3   
print(next(iterOfL)) #4
# print(next(iterOfL)) #StopIteration Error

#Creatin our ouwn for loop using iterators
def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

a = ["apple", "banana", "cherry"]
b = (1,2,3,4)
c={'name':'alice', 'age':25}
d={1,2,3,4}
my_for_loop(d)


#Making our own range function
class MyRange: #this is iterable class
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangIterator(self)

class MyRangIterator: #thiss is iterator class
    def __init__(self,iterableObj):
        self.iterable = iterableObj

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start += 1
        return current

for i in MyRange(1,10):
    print(i)
    
r = MyRange(11,15)
print(r)
for i in r: #This will get executed
    print(i)
for i in r: #This will not get executed as the iterator is exhausted
    print(i)


#Gen Demo
print()
print()
print()
def genDemo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3
    print("StopIteration ERROR Will be raised now if called using next incase using loop it will handle it automatically")

g = genDemo() #Creating generator object here we next is not called yet

# print(next(g)) #Start 1
# print(next(g)) #Middle 2
# print(next(g)) #End 3
# print(next(g)) #StopIteration

#OR

for i in g: #next is called automatically until StopIteration is raised
    print(i)

print()

#yield vs return
"""
yield can be called multiple times and returns a generator object
return can be called only once and returns a value

yield is used to produce a series of values over time, pausing after each one until the next value is requested
return is used to produce a single value and exit the function immediately

yield generates a sequence of values and maintains the function's state between calls
return sends a single value back to the caller and terminates the function
"""

"""
Normal function vs Generator function
Normal Function:
it executes the entire function and returns a single value using return statement in one go

Generator Function:
it uses yield statement to produce a series of values over time, pausing after each yield and 
maintaining state between calls

when its paused at yield, all local variables and the execution state are saved, allowing it to resume later
"""

#Generator function 
def squares(n):
    for i in range(n):
        yield i*i

gen = squares(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
print()

#Range using generator function
def my_range(start,end):
    for i in range(start,end):
        yield i

gen = my_range(10,15)
for i in gen:
    print(i)

#Generator comprehension

#Syntax:
"""
Just for refrence this is how list comprehension looks like
[expression for item in iterable if condition]
[x*x for x in range(10)]

gen = (x*x for x in range(10)) #Note the round brackets
"""
gen = (x*x for x in range(10))
print(gen) #This will print generator object
for i in gen:
    print(i)


#Generator for ML Batch Loader

def batch_loader(data, batch_size):
    batch=[]
    for item in data:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

gen = batch_loader(range(1,23),4)
for batch in gen:
    print(batch)