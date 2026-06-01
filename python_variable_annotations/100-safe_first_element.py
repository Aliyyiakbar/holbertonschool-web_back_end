#!/usr/bin/env python3
"""
This module contains a duck-typed annotated function that safely
returns the first element of a sequence.
"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
