#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with elements and their lengths.
    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences.
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
