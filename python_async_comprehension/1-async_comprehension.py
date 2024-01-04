#!/usr/bin/env python3
"""1. Async Comprehensions

Import async_generator from the previous task
It then writes a coroutine called async_comprehension

The coroutine will collect 10 random numbers
using async comprehension over async_generator,
then return the 10 random numbers.
"""


from your_previous_module import async_generator
# Replace with the actual module name


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, and then returns these numbers.
    """
    return [i async for i in async_generator()]
