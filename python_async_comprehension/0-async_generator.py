#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator coroutine that yields
    a random number between 0 and 10.
    It waits for 1 second before yielding each number
    and does this 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
