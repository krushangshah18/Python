#Arithmetic operators
"""
| Operator | Name                | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | `15`   |
| `-`      | Subtraction         | `10 - 5`  | `5`    |
| `*`      | Multiplication      | `10 * 5`  | `50`   |
| `/`      | Division            | `10 / 5`  | `2.0`  |
| `//`     | Floor division      | `10 // 3` | `3`    |
| `%`      | Modulus (remainder) | `10 % 3`  | `1`    |
| `**`     | Exponent (power)    | `2 ** 3`  | `8`    |
"""
a = 10
b = 3
print(a + b, a // b, a % b, a ** b)


#Comparison Operators
"""
| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `a == b` |
| `!=`     | Not equal to     | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |
"""
print(a == b, a != b, a > b, a < b, a >= b, a <= b)


#Logical Operators
"""
| Operator | Meaning                 | Example              |
| -------- | ----------------------- | -------------------- |
| `and`    | True if both are true   | `(x > 3 and y < 10)` |
| `or`     | True if any one is true | `(x > 10 or y < 10)` |
| `not`    | Reverses result         | `not(x > 3)`         |
"""
print(True and False)  # False
print(True or False)   # True
print(not True)        # False


#Identity Operators
"""
| Operator | Meaning                           |
| -------- | --------------------------------- |
| `is`     | True if both refer to same object |
| `is not` | True if not the same object       |
"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True (same object)
print(a is c)      # False (same values but different objects)
print(b is not c)  # True


#Membership Operators
"""
| Operator | Meaning                      |
| -------- | ---------------------------- |
| `in`     | True if value exists         |
| `not in` | True if value does not exist |
"""
my_list = [1, 2, 3, 4]
print(2 in my_list)      # True
print(5 not in my_list)  # True 