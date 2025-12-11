"""Conditional Statements"""

#if elif else
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

#Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

#match Statement
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")


"""Loops in Python"""

#Range function
StoredRange = range(5)  # 0 to 4
print(StoredRange)

#While Loop
i=0
while i < 5:
    print(i)
    i += 1

#For Loop
for j in range(5):
    print(j)

#Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Looping through a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

#Looping through a string
for char in "hello":
    print(char)

#looping through custom range
for k in range(2, 10, 2):  # from 2 to 9, step 2
    print(k)

for n in range(5, 0, -1):  # from 5 to 1, step -1
    print(n)

for p in range(1,6): # 1 to 5
    print(p)

#Nested Loops
for x in range(3):
    for y in range(2):
        print(f"x: {x}, y: {y}")

#Using else with loops
for q in range(3):
    print(q)
else:
    print("Loop completed")

#Using break and continue
for r in range(5):
    if r == 3:
        break  # Exit loop when r is 3
    print(r)    

for s in range(5):
    if s == 2:
        continue  # Skip when s is 2
    print(s)

#Using pass in loops
for t in range(5):
    pass  # Placeholder for future code

