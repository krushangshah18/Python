"""

- Role of __init__.py
    __init__.py tells Python that the folder should be treated as a package.

- Before Python 3.3
    Without __init__.py, Python wouldn’t treat the folder as a package
    Importing modules inside it would fail

- After Python 3.3

    Implicit namespace packages allow imports even without __init__.py

    But still helpful for:

        Package initialization code

        Defining what is visible on import

        Setting version, metadata

        Import shortcuts
"""

#What __all__ Does

"""
Without __all__
# utils/math_ops.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

    
# main.py
from utils.math_ops import *

print(add(10, 5))    # Works
print(sub(10, 5))    # Works
"""

"""
With __all__
# utils/math_ops.py
__all__ = ["add"]   # Only allow add

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

    
# main.py
from utils.math_ops import *

print(add(10, 5))   # Works
print(sub(10, 5))   # ❌ Error: Name 'sub' is not defined
"""


#__all__ is mentioned in both __init__.py and module

"""
NOTE: 
__all__ only affects 'from module import *' imports.

If __all__ is mentioned in both places the module and __init__ then :

Case 1: Importing from the package:
    from mypkg import *
    Only modules/functions in mypkg/__init__.py __all__ are imported.

Case 2: Importing from a specific module:
    from mypkg.module1 import *
    __init__.py is not involved here.    
    Only functions/classes in mypkg/module1.py __all__ are imported.
"""