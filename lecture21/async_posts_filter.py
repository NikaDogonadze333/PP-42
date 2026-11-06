import asyncio
import aiohttp

async def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return data[:20]

async def main():
    posts = await get_posts()
    filtered_posts = [post for post in posts if post.get("userId") == 1]
    
    for post in filtered_posts:
        print(post.get("title"))

if __name__ == "__main__":
    asyncio.run(main())