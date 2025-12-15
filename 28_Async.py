"""
Async Programming
"""

import asyncio


#coroutine function
#async function
async def someFunc():
    print("This is a async Function")


asyncio.run(someFunc())
print()
print()
print()
"""
asyncio.run() : starts event loop and we need to pass a coroutine object to this
the async function we are calling in its parameres return a coroutine object

this handles the awaiting of the coroutine object
"""


####### Async Function vs normal function

# someFunc() #coroutine 'someFunc' was never awaited someFunc()
#This generates coroutine object and it need to be awaited to get its result of execution


##### Await keyword
"""
await can be used only inside an async function 
"""

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data... ") 
    await asyncio.sleep(delay)
    # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "Some data"}
    # Return some data

# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2) #Here the function has not started executing yet
    print("coroutine obj created but not stared to execute yet")
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task 
    print(f"Received result: {result}")
    print("End of main coroutine")


# Run the main coroutine
print("Before calling main coroutine")
asyncio.run(main())
print("After calling main coroutine")







##### Another example on await : 
# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data

# Define another coroutine that calls the first coroutine
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)
    
    result1 = await task1
    print(f"Received result: {result1}")
    result2 = await task2
    print(f"Received result: {result2}")
    #Here wwe are not getting any performance benefit as both of them needs to be awaited 
    #so for now the execution takes 4sec instead of 2 
    #thesefore we use tasks performed below

#Run the main coroutine
asyncio.run(main())
print()
print()
print()
print()

######## Tasks 
"""
way to run co-routine schedule ASAP 
and allws us to run multiple cvoroutine simultaneously
"""

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    print(f"Coroutine {id} Waiting OVER")
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create tasks for running coroutines concurrently
    print("------------Starting task 1---------------------")
    task1 = asyncio.create_task(fetch_data(1,2))
    print("------------Starting task 2---------------------")
    task2 = asyncio.create_task(fetch_data(2, 3))
    result1 = await task1
    print("------------Starting task 3---------------------")
    task3 = asyncio.create_task(fetch_data(3, 1))
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)
asyncio.run(main())
print()
print()
print()
print()
"""
Earlier we were waiting for a coroutine to finish before moving on to next

with task we dont have that issue here when the coroutine is sleeping or waiting for something which is not in control
of our program we move on and start executing another task

NOTE : we are not using multiple CPU Cores

Goal : is to optimizre our efficiency
"""


############Gather Function 

async def fetch_data(id,sleep_time):
    print(f"coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    # if id == 2:
    #     raise Exception
    print(f"{id} my execution is over")
    return {f"Data fetched from coroutine id : {id}"}

async def main():
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))
    #gather is not good at error handling
    #it wont cancel other coroutines if one of the would fail
    #this could lead your application to some unknown state if not handled properly
    for result in results:
        print(f"Result: {result}")

asyncio.run(main())
print()
print()
print()
print()


###### Task group better than gather function and preffered over it  
"""
Provides built-in error handling and and cancels other coroutines too in case any one of them get some exception or issue 
"""
async def fetch_data(id,sleep_time):
    print(f"coroutine {id} started its execution")
    await asyncio.sleep(sleep_time)
    """
    asyncio.sleep():
        - Registers a timer with the event loop
        - Does not block the thread

    await:
        - Suspends this coroutine
        - Gives control back to the event loop
        - Allows other coroutines to run
    """
    # if id == 2:
    #     raise Exception
    
    return {f"This is data by {id}"}

async def main():
    tasks = []
    """No “forgotten background tasks”"""
    async with asyncio.TaskGroup() as tg:
        for i,sleepTime in enumerate([2,1,3],start=1):
            task = tg.create_task(fetch_data(i,sleepTime))
            """
            tg.create_task(...)
                → wraps coroutine into a Task
                → schedules it immediately in the event loop
                Execution starts immediately, not when awaited
            """
            tasks.append(task)

            """
            When execution leaves the TaskGroup block:
                - The event loop waits for all tasks to finish
                - If any task raised an exception → it propagates here
                - By this point, all tasks are done
            """
    results = [task.result() for task in tasks]

    for res in results:
        print(f"Received result : {res}")

asyncio.run(main())