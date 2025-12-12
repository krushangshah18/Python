"""  
Reference Counting & Garbage Collector
"""
"""
Two major components:

- Reference Counting → primary, immediate cleanup
- Garbage Collector → handles cycles that ref counting cannot free
"""

"""
Every Python object stores a counter: how many references point to it
When reference count hits 0, memory is freed immediately
"""
import sys
import gc 

a = [1,2,3,4]
print(sys.getrefcount(a))
b = a 
print(sys.getrefcount(a))
c = a 
print(sys.getrefcount(a))
del c
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))
print()
print()
print()
print()

x = [1,2,3]      # reference count = 2
print(sys.getrefcount(x))
y = x            # refcount = 3
print(sys.getrefcount(x))
lst = [x, x]     # refcount = 5 (two references in list)
print(sys.getrefcount(x))

print(gc.get_count())
print(gc.get_stats())


del y            # -1
print(sys.getrefcount(x))
lst.pop()        # -1
print(sys.getrefcount(x))
x = None         # -1
print(sys.getrefcount(x))

"""
Reference counting cannot free cyclic references.

For that Garbage collection is used


Python’s GC is in the gc module.

GC is used for breaking reference cycles when:
    - Objects refer to each other
    - No external reference exists

CPython uses generational garbage collection:

    Generation 0 → youngest
    Generation 1
    Generation 2 → oldest

Younger generations are checked more frequently.


GC checks:

    1. Build a graph of objects
    2. If a group of objects reference each other
    3. And no object is referenced from outside the group
    4. → They are unreachable → safe to delete
"""


gc.collect() #Triggering GC manually
print(gc.get_stats()) #Checking GC stats 
print(gc.get_count()) #how many allocations happened since the last GC run
#Output of get_count() new objects have been allocated in Generation 0
#objects survived previous sweeps and moved to Generation 1
#objects in Generation 2 have not yet triggered a sweep

print("Thereshold :",gc.get_threshold())
"""
They tell GC when to run next:
    - If Gen 0 counter hits its threshold, Python runs light GC.
    - If Gen 1 counter hits its threshold, Python runs medium GC.
    - If Gen 2 counter hits its threshold, Python runs full GC (slowest).
"""

gc.disable() # only reference counting will work
gc.enable()
"""
Why disable GC?

    - In high-performance workloads
    - When many short-lived objects get created
    - For predictable latency (games, trading systems)
Reference counting alone is very fast → GC introduced overhead.
"""


"""Weak References
Sometimes you want references that do NOT increase reference count
"""
print()
print()
print()
import weakref

class A:
    pass

obj = A()
print(sys.getrefcount(obj))
p = obj 
print(sys.getrefcount(obj))
r = weakref.ref(obj)
print(sys.getrefcount(obj))
"""
Now:
    r() returns the object
    Does NOT increase refcount
    If obj is deleted → r() returns None

Useful for:
    caches
    observers
    avoiding cycles
"""

"""Memory Leaks in Python

Cyclic references + objects defining __del__
If an object in a cycle has a __del__ method, GC will NOT free it.
"""

class A:
    def __del__(self):
        print("deleted")

a = A()
b = A()
a.other = b
b.other = a
