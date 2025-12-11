"""
static variable in Java ≈ class variable in Python
and if we want to update class variables we use classmethod

So we have :
- class variable 
- class method (Need it to access or modify class variables)
- static method (Needed When the function doesn’t depend on class or instance at all)
"""

"""
| Feature                     | `@classmethod`                         | `@staticmethod`            |
| --------------------------- | -------------------------------------- | -------------------------- |
| First argument              | `cls` (class itself)                   | **no auto first argument** |
| Can modify class variables? | ✔ Yes                                  | ❌ No                      |
| Used for                    | Factory constructors, version upgrades | Utility/helper functions   |
"""

#Class Method :
class Optimizer:
    optimizers_created = 0  # class variable

    def __init__(self, lr):
        self.lr = lr
        Optimizer.optimizers_created += 1

    @classmethod
    def count(cls):
        return cls.optimizers_created

a = Optimizer(1)
b = Optimizer(1)
print(Optimizer.optimizers_created)
print(Optimizer.optimizers_created)



#####Static method

class Math:
    @staticmethod
    def relu(x):
        return max(0, x)

print(Math.relu(-5))


print()
print()
print()
print()
print()
"""
Static Method :

A @staticmethod cannot know which class called it.
It acts like a normal function inside a class — nothing special.
"""
class M:
    total = 0
    
    @staticmethod
    def increment():
        M.total += 1   # must HARDCODE class name ❌
        ###### M.total → so it always updates the parent class variable

class Child(M): pass
Child.increment()
print(Child.total)   
print(M.total)       # updated instead this should be 0



"""
Class Method :
The method gets a reference to the class that called it → cls.
When calling Child.increment(), cls = Child
"""
class M:
    total = 0

    @classmethod
    def increment(cls):
        cls.total += 1

class Child(M): pass
Child.increment()

print(Child.total)  # ✔ 1
print(M.total)      # ✔ 0

"""
| Feature                              | `@staticmethod`           | `@classmethod`                     |
| ------------------------------------ | ------------------------- | ---------------------------------- |
| Receives calling class?              | ❌ No                      | ✔ Yes (`cls`)                     |
| Can update class-specific variables? | ❌ No (only by hardcoding) | ✔ Yes                             |
| Inheritance aware?                   | ❌ Never                   | ✔ Always                          |
| Best for                             | Helper/utility functions  | Factory methods, class-level state |

"""