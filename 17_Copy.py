"""Shallow and deep copy"""

"""When working with mutable objects (like lists, dictionaries, sets, custom objects), 
sometimes we need to create copies instead of referencing the same object."""

"""
NOTE: Assignment does NOT copy it references the same object

a = [1, 2, 3]
b = a     # Just reference
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
"""

"""
Two main types of copies
| Type             | What it copies                        | When to use                          |
| ---------------- | ------------------------------------- | ------------------------------------ |
| **Shallow Copy** | Copies only top-level container       | When nested objects are not changed  |
| **Deep Copy**    | Recursively copies all nested objects | When you need full independent clone |
"""

import copy

# Shallow Copy Example
ogList = [1, 2, [3, 4], 5]
# shallowCopiedList = copy.copy(ogList) #OR
shallowCopiedList = ogList.copy()

shallowCopiedList[2].append(99)
ogList[2].append(77)

print("Original List after shallow copy modification:", ogList)  # [1, 2, [3, 4, 99], 5]
print("Shallow Copied List:", shallowCopiedList)  # [1, 2, [3, 4, 99], 5]


# Deep Copy Example
ogList2 = [1, 2, [3, 4], 5]
deepCopiedList = copy.deepcopy(ogList2)

deepCopiedList[2].append(99)
ogList2[2].append(77)

print("Original List after deep copy modification:", ogList2)  # [1, 2, [3, 4], 5]
print("Deep Copied List:", deepCopiedList)  # [1, 2, [3, 4, 99], 5]