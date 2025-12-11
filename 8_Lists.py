my_list = [1, 2, 3, 4, 5]

print(my_list)
print(my_list[0])  # 1 (indexing starts at 0)
print(my_list[-1])  # 5 (negative indexing for reverse order)
print(my_list[1:4])  # [2, 3, 4] (from index 1 to 3, exclusive of 4)
print(my_list[:3])   # [1, 2, 3] (from start to index 2)
print(my_list[2:])   # [3, 4, 5] (from index 2 to end)

"""add elements to the list"""
my_list.append(6)  # Add 6 at the end
my_list.insert(2, "new")  # Insert "new" at index 2
print(my_list)  # [1, 2, "new", 3, 4, 5, 6]

"""remove elements from the list"""
my_list.remove(3)  # Removes first occurrence of 3
print(my_list)  # [1, 2, "new", 4, 5, 6]
print(my_list.pop(2))  # Remove element at index 2 (Returns the removed item)
print(my_list)  # [1, 2, 4, 5, 6]

"""modify elements in the list"""
my_list[0] = 100  # Change the first element to 100
print(my_list)  # [100, 2, 4, 5, 6]

"""getting length of the list"""
print(len(my_list))  # Returns the number of items in the list

"""concatenation, repetition"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2  # Concatenates lists
list4 = list1 * 2  # Repeats the list
print(list3)  # [1, 2, 3, 4, 5, 6]
print(list4)  # [1, 2, 3, 1, 2, 3]

"""List Comprehensions"""
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
print(squares)

evens = [x for x in range(1, 20) if x % 2 == 0]
print(evens)


"""Common Methods"""
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)   # [1, 2, 3, 4, 5]

numbers.clear()
print(numbers)   # []

nums = [10, 20, 30, 20]
print(nums.index(20))  # 1 (returns first occurrence)

nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3

"""Sorting :"""
data = [5, 3, 1, 4, 2]
data.sort()
print(data)  # [1, 2, 3, 4, 5]   (changes original list)

data.sort(reverse=True)
print(data)  # [5, 4, 3, 2, 1]

"""Using sorted() (returns new list):"""
marks = [50, 20, 80]
new_marks = sorted(marks)
print(marks)  # [50, 20, 80]
print(new_marks)  # [20, 50, 80]

"""reverse() — Reverse original list"""
a = [1, 2, 3, 4]
a.reverse()
print(a)  # [4, 3, 2, 1]

"""Copying Lists"""
x = [1, 2, 3]
y = x.copy() # creates duplicate object
z=x # refrences the same object as x
x[1] = 99
print(x)  # [1, 99, 3]
print(y)  # [1, 2, 3]
print(z)  # [1, 99, 3]

"""Nested Lists"""
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0][1])  # 2

"""zip() with lists"""

names = ["A", "B", "C"]
scores = [80, 90, 85]

combined = list(zip(names, scores))
print(combined)

