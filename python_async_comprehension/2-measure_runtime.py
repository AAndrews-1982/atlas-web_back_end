#!/usr/bin/env python3
"""
This module imports 'async_comprehension' from the previous task and contains
a coroutine called 'measure_runtime' which measures the runtime of executing
'async_comprehension' four times in parallel.
"""

import asyncio
from your_previous_module import async_comprehension  # Replace with the actual module name

async def measure_runtime():
    """
    Coroutine that measures the runtime of executing 'async_comprehension'
    four times in parallel. Returns the total runtime.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
