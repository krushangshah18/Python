import asyncio

async def someAsyncFunc():
    print("Started 1")
    await asyncio.sleep(2)
    print("Finished 1")
async def someAsyncFunc2():
    print("Started 2")
    await asyncio.sleep(2)
    print("Finished 2")
async def someAsyncFunc3():
    print("Started 3")
    await asyncio.sleep(2)
    print("Finished 3")


async def main():
    task1 =  asyncio.create_task(someAsyncFunc())
    task2 =  asyncio.create_task(someAsyncFunc2())
    task3 =  asyncio.create_task(someAsyncFunc3())
    print("I run immediately 1")
    print("I run immediately 2")
    await asyncio.sleep(1)
    print("I run immediately 3")
    result = await task1
    result = await task2
    result = await task3
    print("I run immediately 4")
    print("I run immediately 5")



if __name__ == "__main__":
    asyncio.run(main())