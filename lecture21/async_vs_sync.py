import asyncio
import time
import aiohttp
import requests

def sync_fetch():
    start_time = time.time()
    for i in range(1, 11):
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{i}", timeout=10)
        response.raise_for_status()
    return time.time() - start_time

async def fetch_one(session, url):
    async with session.get(url) as response:
        return await response.json()

async def async_fetch():
    start_time = time.time()
    urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 11)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        await asyncio.gather(*tasks)
    return time.time() - start_time

if __name__ == "__main__":
    sync_duration = sync_fetch()
    print(f"Sync time: {sync_duration:.4f} seconds")

    async_duration = asyncio.run(async_fetch())
    print(f"Async time: {async_duration:.4f} seconds")

    time_difference = sync_duration - async_duration
    print(f"ასინქრონულმა ვერსიამ {time_difference:.4f} წამით უფრო სწრაფად იმუშავა!")