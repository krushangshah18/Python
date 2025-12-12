"""
What is Profiling?
    Profiling = measuring where your program spends time.

Why profiling matters:
    - Slow programs are rarely slow everywhere — usually 5% of the code causes 80% of the slowdown.
    - Guessing is wrong; measuring is right.
    - Without profiling, you waste time optimizing things that don’t matter.

Python gives two types of profiling:
| Tool         | Best For                                        |
| ------------ | ----------------------------------------------- |
| **cProfile** | Entire scripts, functions, bottleneck discovery |
| **timeit**   | Micro-benchmarks (tiny pieces of code)          |

"""

#####################cProfile
import cProfile
import time

def slow():
    total = 0
    # time.sleep(3)
    for i in range(10_000_000):
        total += i
    return total

# cProfile.run("slow()")
cProfile.run("slow()", sort="tottime")

########### timeit — MICRO-BENCHMARKING
"""
Used to compare two small pieces of code.

Why not use time.time()?

    - Inaccurate at microsecond scale
    - OS scheduling noise
    - Doesn't run enough iterations

timeit solves this.
"""
import timeit

def A():
    [x*x for x in range(1000)]

def B():
    res =[]
    for i in range(1000):
        res.append(i*i)

 
print(timeit.timeit(A,number=10000))
print(timeit.timeit(B,number=10000))



"""Optimization Strategies"""

"""
Strategy 1 — Avoid Unnecessary Python Loops
    Pure Python loops are slow
    Better use:
        - List comprehensions   
        - Built-ins like sum, min, max, sorted
        - Vectorized operations (NumPy)

Strategy 2 — Reduce Function Calls (huge overhead in Python)

Strategy 3 — Use Local Variables
    Local variable access is much faster than:
        - global lookup (LOAD_GLOBAL)
        - attribute access (LOAD_ATTR)

    # slow
    for i in range(n):
        total += obj.value

    # fast
    val = obj.value
    for i in range(n):
        total += val


Strategy 4 — Use Built-ins Over Python Code
    Python built-ins are written in C → faster.

    Examples:
        sum(list) → C loop
        sorted(list) → C Timsort
        min, max, any, all

Strategy 5 — Use lru_cache for expensive repeated computations

Strategy 6 — Profile again after optimizing
    Never optimize blindly.

    Procedure:
        - Run cProfile
        - Identify slow function
        - Fix it
        Re-run cProfile
        Compare results
"""