
#With is a context manager
with open("sample.txt", "w") as file:
    file.write("Hiii")

#######Creating our own with

class File:

    def __init__(self,fileName,mode):
        self.file = open(fileName,mode)

    def __enter__(self):
        print("ENTER")
        return self.file
    
    def __exit__(self, type, value, traceback):
        #If no exception occurs → all three are None
        #If exception occurs inside the block → Python passes exception details
        """
        If __exit__ returns:
            True → suppress exception
            False → re-raise exception
        """
        # type : provides type of error
        print("EXIT")
        self.file.close()

with File("sample.txt","w") as file:
    file.write("HELLLLLLOOOOOOOO!!!!!")



###### another approach to create context manager

from contextlib import contextmanager

@contextmanager
def file(filename,method):
    """ 
    Everything before yield = __enter__
    Everything after yield = __exit__
    The value after yield becomes the value of as
    """
    file = open(filename,method)
    yield file 
    file.close()

with File("sample.txt","w") as file:
    file.write("HELLLLLLOOOOOOOO using generator!!!!!")

