#!/usr/bin/env python3
"""task1: Reworked Async Comprehensions"""

from typing import List

# Importing the asynchronous number generator
number_generator = __import__("0-async_generator").async_generator


async def gather_async_numbers() -> List[float]:
    """Coroutine for collecting 10 random numbers asynchronously.
    This function uses an asynchronous comprehension to iterate over
    values produced by number_generator and assembles them into a list.

    Returns:
        List[float]: A list of 10 randomly generated floating-point numbers.
    """
    return [number async for number in number_generator()]
