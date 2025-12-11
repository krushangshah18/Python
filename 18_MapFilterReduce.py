l = [1,2,3,4,5]
print(l)

#map
NewL = list(map(lambda x : x*x*x,l))
print(NewL)

#filter
NewNewL = list(filter(lambda x:x%2==0,NewL))
print(NewNewL)

#reduce
from functools import reduce
Finalsum = reduce(lambda x,y : x+y,NewNewL)
print(Finalsum)