#A set is an unordered collection of unique elements.

s = set([1,4,3,4,2,3,4,7,5,6,8,5,7,8,8,7,9,9,2,3])
print(s)
s = {1, 2, 3, 2, 4, 2, 3, 4}
print(s)

"""
| Feature         | Description                                |
| --------------- | ------------------------------------------ |
| Unique elements | Duplicate values are automatically removed |
| Unordered       | No indexing or slicing                     |
| Mutable         | You can add or remove elements             |
"""

s.add(10) # add single element
print(s)

s.update([11,12,13]) # add multiple elements
print(s)

s.remove(12) # remove specific element (error if not found)
print(s)

s.discard(12) # remove specific element (no error if not found)
print(s)

print(s.pop()) #Removes and returns random item
print(s)

s.clear() #Removes all items
print(s)

"""Set Operations"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a.union(b)) # {1, 2, 3, 4, 5, 6}

print(a & b)  
print(a.intersection(b))   # {3, 4}

print(a - b)
print(a.difference(b))     # {1, 2}

print(a ^ b)
print(a.symmetric_difference(b))  # {1, 2, 5, 6

"""Set Membership"""
print(2 in a)     # True
print(10 not in a)  # True
