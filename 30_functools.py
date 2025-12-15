"""
lru_cache caches function results → memoization.
"""

from functools import lru_cache

# @lru_cache(maxsize=None) # Unlimited Cache size
# @lru_cache() #default = 128
@lru_cache(maxsize=3)
def compute(x):
    print(f"Computing: {x}")
    return x*x 


print(compute(5))
print(compute(3))
print(compute(2))
print(compute(3))
print(compute(5))
print(compute(2))
print(compute(1))
print(compute(5))
print(compute(4))
print(compute.cache_info())
print(compute.cache_clear())

print()
print()
print()
print()

####### partial function

"""
partial allows pre-filling parameters → powerful for functional programming
"""

from functools import partial

def power(base,exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
# cube = partial(power, 3) # incase the first parameter needs to be set this is the syntax


print(square(5))
print(cube(3))


######## reduce in functools

from functools import reduce
import operator
print()
print()
print()
print(reduce(operator.add,[1,2,3,4]))
print(reduce(operator.mul,[1,2,3,4]))
print(reduce(operator.sub,[1,2,3,4]))
print(reduce(operator.eq,[5,7]))