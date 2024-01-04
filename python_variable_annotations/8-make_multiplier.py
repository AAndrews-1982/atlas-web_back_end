#!/usr/bin/env python3
""""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.
    Parameters:
    multiplier (float): The multiplier value.
    Returns:
    Callable[[float], float]: A function that takes a float
    and multiplies it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
