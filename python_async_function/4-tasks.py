#!/usr/bin/env python3
"""4. Tasks"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns 'task_wait_random'
    'n' times with the specified 'max_delay'.
    Args:
        n (int): The number of times to spawn 'task_wait_random'.
        max_delay (int): The maximum delay for 'task_wait_random'.
    Returns:
        List[float]: List of delays in the order they were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
