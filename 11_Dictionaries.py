#A dictionary is a collection of key–value pairs.

student = {"name": "Sam", "age": 21, "marks": 88}
print(student)
print(student.items())
print(student.keys())
print(student.values())

"""Accessing Elements"""
print(student["name"])     # Sam
print(student.get("age"))  # 21
print(student.get("grade"))  # None
print(student.get("grade", "Not Found"))  # Using get() avoids an error if key missing

"""Modifying Elements"""
student["age"] = 22      # update
student["city"] = "Delhi"  # add
print(student)

"""Removing Elements"""
student.pop("age")      # removes key & returns value
print(student)
student.popitem()       # removes last inserted pair
print(student)
del student["marks"]     # delete key
print(student)
student.clear()         # remove all
print(student)

"""Looping through a Dictionary"""
info = {"a": 1, "b": 2, "c": 3}
for key in info:
    print(key, info[key])

"""Dictionary Comprehensions"""
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

evens = {x: x*x for x in range(10) if x % 2 == 0}
print(evens)

"""Nested Dictionaries"""
students = {
    1: {"name": "A", "marks": 85},
    2: {"name": "B", "marks": 90}
}

print(students[1]["marks"])   # 85


"""fromkeys() — Create dict from keys"""
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

"""setdefault() Used to insert a key if not present and returns the value. new or the current one"""
d = {"name": "John"}
print(d.setdefault("age", 25)) #25
print(d)  # {'name': 'John', 'age': 25}

"""Sorting dictionary : Sorting doesn’t modify the dictionary—it returns a new sorted view."""
data = {"b": 3, "a": 1, "c": 2}

print(sorted(data))                     # ['a', 'b', 'c'] (keys only)
print(sorted(data.items()))             # [('a', 1), ('b', 3), ('c', 2)]
print(sorted(data.items(), key=lambda x: x[1]))  # sort by value

