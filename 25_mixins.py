"""
A Mixin is a class that provides reusable methods but is not meant to stand alone.
Mixins add functionality to other classes.
They are not complete objects by themselves (no standalone purpose).
They rely on multiple inheritance.
"""


"""
When to Use Mixins (Perfect Use Cases)

Mixins are ideal when:
    ✔ You want to add extra capabilities to many unrelated classes
    Example: Logging, serialization, comparison, hashing, validation, timestamps.

    ✔ You don't want to create a deep class hierarchy
    Mixins let you add features horizontally.

    ✔ You want reusable building blocks
    Each Mixin provides one specific feature.
"""
class ThisIsMixin:
    def toJSON(self):
        import json
        return json.dumps(self.__dict__)

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

class Student(Person,ThisIsMixin):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

    def __repr__(self):
        return f"Name: {self.name}, age: {self.age}, department: {self.department}"
    

s = Student("Krushang",21,"CE")
print(s)
print(s.toJSON)

"""
Mixin : mixin is a class with the single purpose to add functionality to other classes

multiple inheritance is used to achieve mixins in python
"""