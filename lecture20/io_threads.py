import threading
import time
import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

if __name__ == "__main__":
    start_time = time.time()
    threads = []

    for i in range(1, 101):
        t = threading.Thread(target=fetch_post, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Threads execution time: {end_time - start_time:.4f} seconds")