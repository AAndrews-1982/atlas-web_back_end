#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions

Custom Implementation of Parallel Async Comprehensions
This script imports the async_comprehension coroutine
from a previous implementation
and includes a custom coroutine, calculate_runtime,
that executes async_comprehension
four times concurrently.

The total execution time is measured and returned.

The execution time is expected to be around 10 seconds due
to the nature of asynchronous IO-bound tasks running in parallel.
"""
import asyncio
import time

# Importing the async comprehension coroutine from another file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def calculate_runtime() -> float:
    """
    Measures the runtime of executing four async comprehensions in parallel.
    """
    start_time = time.perf_counter()
    # Using list comprehension to create four async tasks
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    # Calculating the total runtime
    total_runtime = end_time - start_time
    return total_runtime
