"""A module is a file that contains Python code 
functions, classes, or variables
 that can be reused in other programs."""

#Basic
import math
print(math.sqrt(25))   # Output: 5.0

#Using alias
import math as m
print(m.pi)

#Importing specific functions
from math import factorial as fact, pow
print(fact(5))  # Output: 120
print(pow(2, 3))     # Output: 8.0


#user-defined module
import myModule # generally better for bigger projects and avoiding conflicts
print(myModule.greeting("Krushang"))

from myModule import greeting # good for short scripts or when importing only 1–2 functions
print(greeting("Bob"))
"""
Both of these will work the same way 
- performance perspective, the difference is very small and usually not important
- import myModule is Slightly cheaper
"""


#Some commonly used built-in modules
import random
print(random.randint(1, 100))

import datetime
today = datetime.date.today()
print(today)

import os
print(os.getcwd())   # Current directory
