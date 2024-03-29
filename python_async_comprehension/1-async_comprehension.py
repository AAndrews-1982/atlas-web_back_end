#!/usr/bin/env python3
""" 1. Async Comprehensions
Module Description: Async Comprehensions Module
This module imports an asynchronous generator from a previous task and defines
an asynchronous comprehension function, async_comprehension, which gathers
and returns 10 random numbers generated by the async_generator.
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers using an
    asynchronous comprehension.
    This function uses the async_generator to generate 10 random numbers,
    collects them using an async comprehension, and returns them in a list.
    Returns: List[float]: A list containing 10 randomly generated numbers.
    """
    return [i async for i in async_generator()]
