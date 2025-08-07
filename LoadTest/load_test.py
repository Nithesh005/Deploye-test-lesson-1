import requests
from concurrent.futures import ThreadPoolExecutor
import time

def call_url(_):
    print("Test")
    return requests.get("http://127.0.0.1:5001").text

start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(call_url, range(5)))
end = time.time()

print(f"Total time for 5 requests: {end - start:.2f} seconds")
