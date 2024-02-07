#!/usr/bin/env python3
"""
Manages data storage in Redis with unique keys for each entry.
"""

import redis
import uuid
import json
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.
    Uses the method's qualified name as a key in Redis to store the count.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Increments the count for the method's qualified name every time
        the method is called and returns the value returned by the method.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.
    Uses Redis lists to store the arguments (inputs) and results (outputs).
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Stores method arguments and output in Redis and returns the output.
        """
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular function.
    """
    key = method.__qualname__
    input_key = f"{key}:inputs"
    output_key = f"{key}:outputs"

    redis = method.__self__._redis
    counts = redis.get(key).decode("utf-8")
    print(f"{key} was called {counts} times:")

    list_in = redis.lrange(input_key, 0, -1)
    list_out = redis.lrange(output_key, 0, -1)
    zip_list = list(zip(list_in, list_out))
    for a, b in zip_list:
        attr, routput = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {routput}")


class Cache:
    """
    A Cache class to store data in Redis using randomly generated keys.
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
         Saves data in Redis and assigns it a unique key..
        """
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, int]]] = None
            ) -> Optional[Union[str, bytes, int]]:
        """
        Retrieves data from Redis by key and optionally transforms it.
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string value from Redis by key.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis by key.
        """
        return self.get(key, fn=int)
