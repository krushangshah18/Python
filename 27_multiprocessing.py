"""
Python’s GIL (Global Interpreter Lock) allows only one thread to execute Python bytecode at a time.
    Exists in CPython and Not in PyPy, Jython, IronPython
    So threads cannot run CPU-bound code in parallel.
Why Does Python Have the GIL : Uses reference counting for memory management Reference counting is not thread-safe
GIL simplifies memory safety

What the GIL ACTUALLY Blocks :
| Scenario             | GIL Impact      |
| -------------------- | ----------------|
| CPU-bound threading  | ❌ Blocked      |
| I/O-bound threading  | ✅ Works        |
| Multiprocessing      | ✅ No GIL issue |
| NumPy / C extensions | ✅ GIL released |


Multiprocessing overcomes the GIL by creating separate Python processes, each with its own interpreter + its own GIL.
Multiprocessing runs multiple processes.
    - Separate memory space
    - Uses multiple CPU cores
    - True parallelism

its good when tasks are CPU bound and not I/O bound
"""
"""
Python Scope Rule
Python follows LEGB:

| Scope | Meaning                              |
| ----- | ------------------------------------ |
| **L** | Local (inside current function)      |
| **E** | Enclosing (outer function, closures) |
| **G** | Global (module-level)                |
| **B** | Built-in                             |

- global tells Python to use the module-level variable, not create a local one
- nonlocal refers to the nearest enclosing function variable (NOT global). (Only works inside nested functions)
"""

from multiprocessing import Process
import os

def work():
    print(f"Work getting executed by {os.getpid()}")

p = Process(target=work)
p.start()
p.join()



############# Proper Example for multiprocessing

def compute():
    s=0
    print(f"Work getting executed by {os.getpid()}")
    for i in range(10_000_000):
        s+=i

    print(f"Loop completed for {os.getpid()} s={s}")
        

processes = []

for _ in range(4):
    p = Process(target=compute)
    processes.append(p)
    print(f"Proecess {p} started")
    p.start()

for p in processes:
    p.join()

print("All Process Work completed")


##############Sharing Data Between Processes
"""
Each process has its own memory — globals are not shared, unlike threading

To share data, use:
    - multiprocessing.Value
    - multiprocessing.Array
    - multiprocessing.Manager
"""

from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    for _ in range(10000):
        with lock:
            counter.value +=1

counter = Value('i',0)
lock = Lock()

procs = [Process(target=increment, args=(counter,lock)) for _ in range(4)]

for p in procs:
    p.start()

for p in procs:
    p.join()

print(counter.value)








############Process Pools
"""
many tasks, manually creating processes is annoying.
Python gives high-level process pools.
"""

from multiprocessing import Pool

def square(x):
    return x*x

with Pool(processes=4) as pool:
    results = pool.map(square,range(10)) #pool.map(function, iterable)
    """
    - Apply function to each element of iterable
    - Distribute work across the process pool
    - Collect results in input order
    """

print(results)

"""
Worker 1 → square(0)
Worker 2 → square(1)
Worker 3 → square(2)
Worker 4 → square(3)

Worker 1 → square(4)
Worker 2 → square(5)
Worker 3 → square(6)
Worker 4 → square(7)

Worker 1 → square(8)
Worker 2 → square(9)

"""