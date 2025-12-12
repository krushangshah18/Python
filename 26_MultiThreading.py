"""
Threading = running multiple tasks concurrently within the same process


"""

import threading,time

def dynamicTimeWork(sec):
    print(f"Task with time: {sec} Seconds Started")
    time.sleep(sec)
    print(f"Task with time: {sec} Seconds Ended")

t1 = threading.Thread(target=dynamicTimeWork, args=[5])
t2 = threading.Thread(target=dynamicTimeWork, args=[3])
t3 = threading.Thread(target=dynamicTimeWork, args=[1])

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

print("ALL Completed")

"""
Daemon Threads
Daemon threads automatically close when the main program exits.

t= threading.Thread(target=task, daemon=True)
Use-case:
    Background logging
    Monitoring
    Timers
"""


############Race Condition: 

import threading

counter = 0

def increment():
    #Do NOT create a new local variable named counter Use the variable counter from the module
    global counter
    for _ in range(10000):
        counter +=1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final Count: ",counter)



#Fix Race Conditions with Locks

counter = 0
lock = threading.Lock()

def longCount():
    global counter
    for _ in range (10000):
        with lock:
            counter +=1 

t1 = threading.Thread(target=longCount)
t2 = threading.Thread(target=longCount)

t1.start()
t2.start()

t1.join()
t2.join()
print("Final Count: ",counter)
