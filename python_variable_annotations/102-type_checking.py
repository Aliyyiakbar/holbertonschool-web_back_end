#!/usr/bin/env python3
"""
This module provides a type-checked function to zoom into an array
by repeating its elements a specified number of times.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a zoomed-in list by repeating each element in the input tuple
    by the given multiplication factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
