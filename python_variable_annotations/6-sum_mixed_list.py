#!/usr/bin/env python3
"""6. Complex types - mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.
    Parameters:
    mxd_lst (List[Union[int, float]]):
    A list of integers and floating-point numbers.
    Returns:
    float: The sum of the elements in the list.
    """
    return sum(mxd_lst)
