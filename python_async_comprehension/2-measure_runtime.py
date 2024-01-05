#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""


import asyncio
import time


async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime of executing 'async_comprehension'
    four times in parallel. Returns the total runtime.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
