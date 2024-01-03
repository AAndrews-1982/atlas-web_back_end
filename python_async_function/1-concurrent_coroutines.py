#!/usr/bin/env python3

import asyncio
from previous_file import wait_random  # Replace 'previous_file' with the actual name of your Python file

async def wait_n(n: int, max_delay: int) -> list:
    # Create a list to store the tasks
    tasks = []

    # Spawn n instances of wait_random with the specified max_delay
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Wait for all tasks to complete and collect the results
    # asyncio.as_completed(tasks) returns an iterator that yields tasks as they complete
    delays = [await task for task in asyncio.as_completed(tasks)]

    # The list of delays is already in ascending order because of concurrency
    # Tasks that finish first (with shorter delays) will be added to the list first
    return delays

