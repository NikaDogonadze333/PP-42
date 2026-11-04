import multiprocessing
import time
from math import factorial

def compute(n):
    return factorial(n)

if __name__ == "__main__":
    numbers = [50000] * 8

    start_single = time.time()
    single_results = [compute(n) for n in numbers]
    end_single = time.time()
    print(f"Single-process time: {end_single - start_single:.4f} seconds")

    start_multi = time.time()
    with multiprocessing.Pool() as pool:
        multi_results = pool.map(compute, numbers)
    end_multi = time.time()
    print(f"Multiprocessing time: {end_multi - start_multi:.4f} seconds")