#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine named 'async_generator'.
"""

import asyncio
import random

async def async_generator():
    """
    Asynchronous generator coroutine that yields a random number between 0 and 10.
    It waits for 1 second before yielding each number and does this 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)