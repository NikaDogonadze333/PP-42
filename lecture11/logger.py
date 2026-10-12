import time
from functools import wraps
from typing import Callable, Any


def log_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Running [{func.__name__}]... Executed in {elapsed_time:.2f} seconds.")
        return result

    return wrapper