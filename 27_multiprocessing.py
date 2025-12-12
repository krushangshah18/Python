"""
Python’s GIL (Global Interpreter Lock) allows only one thread to execute Python bytecode at a time.

So threads cannot run CPU-bound code in parallel.

Multiprocessing overcomes the GIL by creating separate Python processes, each with its own interpreter + its own GIL.

its good when tasks are CPU bound and not I/O bound
"""


from multiprocessing import Process
import os

def work():
    print(f"Work getting executed by {os.getpid()}")

p = Process(target=work)
p.start()
p.join()



############# Proper Example for multiprocessing

from multiprocessing import process

def compute():
    s=0
    print(f"Work getting executed by {os.getpid()}")
    for i in range(10_000_000):
        s+=i

    print(f"Lop completed for {os.getpid()}")
        

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
    results = pool.map(square,range(10))

print(results)