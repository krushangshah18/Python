#Tuples are Immutable
"""
t = (10, 20, 30)
# t[1] = 100  ❌ Error: TypeError: 'tuple' object does not support item assignment
"""

t = (1, 2, 3)
print(2 in t)      # True
print(5 not in t)  # True

t = (1, 2, 3, 2, 4)
print(t.count(2)) #2
print(t.index(2)) #1

"""Tuple Packing & Unpacking"""
t = 1, 2, 3    # Packing (without parentheses also works)
print(t)
a, b, c = t    # Unpacking
print(a, b, c)  # 1 2 3

#With extra values using *:
t = (10, 20, 30, 40)
a, *b = t
print(a)  # 10
print(b)  # [20, 30, 40]

"""nested Tuples"""
t = (1, 2, (3, 4), 5)
print(t[2][1])  # 4

"""Tuples with different data types"""
student = ("Sam", 21, ["Math", "Science"])
print(student)

#Note : Even though tuples are immutable, mutable elements inside them can change
student[2].append("English")
print(student)   # ('Sam', 21, ['Math', 'Science', 'English'])


"""Concatenation & Repetition"""
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)
print(t1 * 3)    # (1, 2, 1, 2, 1, 2)
