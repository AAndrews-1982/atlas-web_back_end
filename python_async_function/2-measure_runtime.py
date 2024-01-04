#!/usr/bin/env python3
import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of 'wait_n' and return the average time per call.

    Args:
        n (int): Number of times to execute 'wait_n'.
        max_delay (int): Maximum delay to pass to 'wait_n'.

    Returns:
        float: The average time taken per call to 'wait_n'.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n

if __name__ == '__main__':
    n = 5
    max_delay = 9
    print(asyncio.run(measure_time(n, max_delay)))
