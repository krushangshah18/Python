l = [1,2,3,4,5]
print(l)

#map
NewL = list(map(lambda x : x*x*x,l)) #map(func,iterable)
print(NewL) #[1,8,27,64,125]

#filter
NewNewL = list(filter(lambda x:x%2!=0,NewL))
print(NewNewL) #[1,27,125]

#reduce
from functools import reduce
Finalsum = reduce(lambda x,y : x+y,NewNewL)
print(Finalsum) #153