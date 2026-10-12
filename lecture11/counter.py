from typing import Callable


def make_counter(start_value: int = 0) -> Callable[[], int]:
    count = start_value

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner