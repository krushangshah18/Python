import requests
import os
import time

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []

def run_tasks():
    for symbol in symbols:
        response = requests.get(url.format(symbol,api_key))
        results.append(response.json()) 

print("Timer Started")
start_time = time.time()
run_tasks()
end_time = time.time()
total_time = end_time-start_time
print("it takes {} seconds to make {} api calls".format(total_time,len(symbols)))