# x =10/0   # This will raise a ZeroDivisionError

"""Most genric way to handle errors"""
# try: 
#     # x = 10 / 0
#     pass
# except:
#     print("ERROR")

"""Handling specific error"""
# try: 
#     pass
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result is:", result)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")
# else:
#     print("No errors occurred. EXECUTED ONLY IF NO EXCEPTION")
# finally:
#     print("Execution completed. ALWAYS EXECUTED")

"""Exception Object & Accessing Error Message"""
# try:
#     x = 10/0
# except ZeroDivisionError as e:
#     print("Error occurred:", e)

"""Raising Exceptions"""
# age = -5
# if age<0:
#     raise ValueError("Age cannot be negative")

"""Custom Exceptions"""
class NegativeAgeError(Exception):
#(Exception) — this means AgeError inherits from Python’s built-in 
# Exception class
    def __init__(self, message="Age cannot be negative"):
        super().__init__(message)
try:
    age = -10
    if age < 0:
        raise NegativeAgeError()
except NegativeAgeError as e:
    print("Custom Exception:", e)

"""Using assert Statement"""
#assert is a debugging tool used to test assumptions in code.
#If the condition is True, the program continues normally.
#If the condition is False, Python raises an AssertionError.

#SYNTAX : assert condition, optional_message

age = -5
assert age >= 0, "Age cannot be negative"
print("Valid age")