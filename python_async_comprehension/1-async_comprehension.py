#!/usr/bin/env python3
"""1. Async Comprehensions

Import async_generator from the previous task
It then writes a coroutine called async_comprehension

The coroutine will collect 10 random numbers
using async comprehension over async_generator,
then return the 10 random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, and then returns these numbers.
    """
    return [i async for i in async_generator()]
