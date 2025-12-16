import math 
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance(self,other):
        return round(math.sqrt(((other.x - self.x)**2)+((other.y - self.y)**2)),2)
    
    def midPoint(self,other):
        newX = (self.x + other.x)/2
        newY = (self.y + other.y)/2
        return  Point(newX,newY)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        

A = Point(3,5)
D = Point(3,5)
B = Point(7,9)
C = Point(3,2)

print(A,B,C)
print(A.distance(B))
print(A.midPoint(C))
print(A==C)
print(A==D)