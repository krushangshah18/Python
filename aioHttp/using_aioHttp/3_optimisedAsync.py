import asyncio,aiohttp
import os
import time

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []

print("Timer Started")
start_time = time.time()

def getTasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol,api_key),ssl = False)))
    return tasks
"""
1️⃣ session.get(...)
    - Returns a coroutine object
    - Does NOT start execution yet

2️⃣ asyncio.create_task(...)
    - Wraps coroutine into a Task
    - Schedules it on the event loop
    - Task starts executing immediately (soon)

3️⃣ Append to list
    - We keep references so they don’t get garbage-collected
    - Returns list of running tasks
"""

async def getSymbols():
    async with aiohttp.ClientSession() as session:
        tasks = getTasks(session) #Tasks are created and scheduled, Execution may already be in progress
        responses = await asyncio.gather(*tasks)
        """
            - Waits for all tasks concurrently
            - Preserves order
            - Returns results in a list
        """
        for response in responses:
            results.append(await response.json())


asyncio.run(getSymbols())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()
end_time = time.time()
total_time = end_time-start_time
print("it takes {} seconds to make {} api calls".format(total_time,len(symbols)))