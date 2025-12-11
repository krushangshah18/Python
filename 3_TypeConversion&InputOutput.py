"""Type Conversion"""

#implicit type conversion : Python automatically converts types when safe

x = 5           # int
y = 2.0         # float
z = x + y       # x is converted to float
print(z)        # 7.0
print(type(z))  # <class 'float'>

#explicit type conversion : Manually converting types using functions
"""
| Function  | Converts To     |
| --------- | --------------- |
| `int()`   | Integer         |
| `float()` | Floating number |
| `str()`   | String          |
| `bool()`  | Boolean         |
| `list()`  | List            |
| `tuple()` | Tuple           |
| `set()`   | Set             |
"""

#Some Examples:
a = "123"
b = int(a)          # Convert string to integer
print(b)            # 123
print(type(b))      # <class 'int'>         

#List → Dict
pairs = [["name", "John"], ["age", 25], ["city", "NY"]]
data = dict(pairs)
print(data)  # {'name': 'John', 'age': 25, 'city': 'NY'}

#Dict → List
info = {"name": "Alice", "age": 22}
keys_list = list(info.keys())
values_list = list(info.values())
print(keys_list)   # ['name', 'age']
print(values_list) # ['Alice', 22]

#Dict → Tuple
info = {"name": "Alice", "age": 22}
info_Tuple = tuple(info.items())
print(info_Tuple)


#Input and Output in Python
#Taking input from user

#Important: input() always returns a string, so convert if needed
name = input("Enter your name: ")
print("Hello", name)
age = int(input("Enter your age: "))  # Converting input string to integer
print("You are", age, "years old.")


#Output 
#Basic
print("Hello World")

#Printing multiple values
print("Name:", name, "Age:", age)

#Formatted Strings (f-strings)
print(f"{name} is {age} years old.")

#Using Format Method
print("{} is {} years Old.".format(name,str(age)))

#Separator (sep) and end (end) options
# sep : Used to specify what should separate multiple values inside print().
print(1,2,3,4, sep='-')

#end : Used to specify what should be printed at the end of the output. **Default is newline**.
print("Hello", end=' ')
print("World")

a="World"
print("Hello", a) #different parameters passed Using comma (,) adds space by default: Hello World
print("Hello"+a) # String concatenation HelloWorld