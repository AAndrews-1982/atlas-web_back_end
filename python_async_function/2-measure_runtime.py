#!/usr/bin/env python3
"""2. Measure the runtime"""

import asyncio
import time
from typing import Callable

# Import wait_n from the previous file. Adjust the import path as needed.
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of the wait_n
    function and return the average.
    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay parameter for wait_n.
    Returns:
        float: The average time per execution of wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 9
    print(f"Average time per call: {measure_time(n, max_delay)} seconds")
