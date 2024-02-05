#!/usr/bin/env python3
"""
This module defines a Cache class for storing data in Redis with random keys.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    A Cache class to store data in Redis using randomly generated keys.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # Clean start

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis under a random key.

        :param data: Data to store (str, bytes, int, float).
        :return: The random key for the data.
        """
        # Generate a unique key
        key = str(uuid.uuid4())
        # Store data with the generated key
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, int]]] = None
            ) -> Optional[Union[str, bytes, int]]:
        """
        Retrieve data by key, optionally converting it.
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Get value as UTF-8 string."""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Get value as integer."""
        return self.get(key, fn=int)

    def count_calls(method: Callable) -> Callable:
        """
        Decorator that counts how many times a method is called.
        """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


# Test the Cache class with conversion functions
if __name__ == "__main__":
    cache = Cache()
    cache.store("Hello, Redis!")
    cache.store("Another value")

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value, "Assertion failed"

    print("All tests passed.")
