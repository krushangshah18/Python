"""
Abstraction means hidden

abstract method is a method in which we dont have any code
"""
"""
| Concept           | Meaning                         |
| ----------------- | ------------------------------- |
| **Abstraction**   | *What* operations are available |
| **Encapsulation** | *How* data is protected         |
"""

#abstract base classes module
from abc import ABC, abstractmethod

#To make a class abstract class we need 2 things 
"""
1. The class should inherit ABC
2. There should be atleast one method decorated with @abstractmethod decorator
"""

class BankApp(ABC):
    def database(self):
        print("Connected")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):
    def loginMethod(self):
        print("Login Successful")
    def security(self):
        print("Fully Secured")

mo = MobileApp()
mo.security()
mo.loginMethod()
mo.database()


# bk = BankApp() #Can't instantiate abstract class BankApp without an implementation for abstract method 'security'