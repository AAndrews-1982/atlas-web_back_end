#!/usr/bin/env python3

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple consisting of a string and the square of a number.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): An integer or floating-point number to be squared.

    Returns:
    Tuple[str, float]: A tuple where the first element is k and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
