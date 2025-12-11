"""
Instance Variable : are the variables which belongs to the instances/objects means they are different for each object

Static variables : these are class variables means for any object this variable is common each object DOSEN'T have its copy

"""

class Atm:
    #Static/class var
    __counter=0

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.srNum = Atm.__counter
        Atm.__counter = Atm.__counter + 1

    @staticmethod
    def get_counter(): #Static methods belong to class so they dont need self therefore add @staticmethod anotation at top of it
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("NOT ALLOWED")

one = Atm()
two= Atm()
print(one.srNum)
print(two.srNum)

print(Atm.get_counter())
