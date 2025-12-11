"""
Encapsulation :

We restrict our variables to get accessed directly

Why? : 
so if the variables are being accessed directly then variables can be update directly from outside of the object 

we make variables and methids private by prefixing the name by "__" eg : __IamPrivateVar OR __PrivateMethod()


when we make variable private as __MyVar during interpretation its converted to _ClassName_MyVar
"""
#Nothing in python is truly private

class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance=10

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print(f"PIN Updated {self.__pin}")
        else:
            print("NOT ALLOWED")

    def __str__(self):
        return "Pin for the account is {} and balance is {}".format(self.__pin,self.__balance)
#here sbi is reference variable as it stores reference to the objects location in the memory
sbi = Atm()

sbi.balance=60 #This will not actually change the balance variable but is adds another variable to the object 

print(sbi.balance)
print(sbi._Atm__balance) #this is how py stores private variables but DO NOT USE them
print(sbi)

sbi.set_pin("1234")
print(sbi.get_pin())
sbi.set_pin(342234)
print(sbi.get_pin())
