import concurrent.futures
import time
import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

if __name__ == "__main__":
    start_time = time.time()
    post_ids = list(range(1, 101))

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(fetch_post, post_ids)

    end_time = time.time()
    print(f"ThreadPoolExecutor execution time: {end_time - start_time:.4f} seconds")