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

async def getSymbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print('Working on symbol {}'.format(symbol))
            response = await asyncio.create_task(session.get(url.format(symbol,api_key),ssl=False))
            """
            session.get(...) : Creates an awaitable coroutine (HTTP request)
            asyncio.create_task(...) : Wraps it in a Task & Schedules it on the event loop
            await ... : Immediately waits for it to finish

            create_task + await immediately = NO concurrency
                - Requests are executed one after another
                - No parallel execution happening here
            """
            results.append(await response.json())


asyncio.run(getSymbols())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()
end_time = time.time()
total_time = end_time-start_time
print("it takes {} seconds to make {} api calls".format(total_time,len(symbols)))