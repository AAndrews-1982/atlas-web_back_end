#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    # Calculate a random delay between 0 and max_delay (inclusive).
    # random.uniform(a, b) returns a floating point number between a and b.
    delay = random.uniform(0, max_delay)

    # Await for the duration of the calculated delay.
    # asyncio.sleep(delay) asynchronously pauses execution for the given delay.
    await asyncio.sleep(delay)

    # Return the amount of time delayed.
    # This value is a float and represents the actual time spent waiting.
    return delay

