#!/usr/bin/env python3
"""1. Async Comprehensions"""


from your_previous_module import async_generator
# Replace with the actual module name


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, and then returns these numbers.
    """
    return [i async for i in async_generator()]
