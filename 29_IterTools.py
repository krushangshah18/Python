"""
itertools provides fast, memory-efficient tools for working with iterators
Many of these functions return generators, meaning:
    ✔ Lazy (don’t load full list into memory)
    ✔ Efficient even with large or infinite sequences
"""

######## Combinatoric Iterators
from itertools import permutations,combinations,combinations_with_replacement,product
# 1. permutations(iterable, r)
print(list(permutations("ABC",2)))

# 2. combinations(iterable, r)
print(list(combinations("ABC",2)))

# 3. combinations_with_replacement
print(list(combinations_with_replacement("ABC",2)))

# 4. product (Cartesian Product)
print(list(product("ABC","12")))

########## Infinite Iterators

#itertools includes infinite generators, so use caution and break loops manually

from itertools import count, cycle, repeat

#count(start=0, step=1) — infinite counter
for i in count(10,2):
    print(i, end=" ")
    if i > 20:
        break
print()

#cycle(iterable) — repeat forever
colors = cycle(["R","G","B"])
for _ in range(5):
    print(next(colors))

#repeat(item, times=None)
print(list(repeat("A",5)))

########## Useful Itertools for Data Processing
from itertools import accumulate,chain,groupby
import operator
#accumulate — running totals
print(list(accumulate([1,2,3,4])))
print(list(accumulate([1,2,3,4], operator.mul )))

#chain — combine iterables
print(list(chain([1,2],[3,4],[5])))
print(list(chain.from_iterable([[1,2],[3,4]])))

#groupby — group sorted data
data = "AAAABBBCCCDDDACCDD"
for k,g in groupby(data):
    print(k,len(list(g)))
    # print(g) #<itertools._grouper object at 0x7b8d89834ca0>

    