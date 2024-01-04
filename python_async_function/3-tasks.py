#!/usr/bin/env python3
"""3. Tasks"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from the wait_random coroutine.
    Args:
        max_delay (int): The maximum delay to pass to wait_random.
    Returns:
        asyncio.Task: The created task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
