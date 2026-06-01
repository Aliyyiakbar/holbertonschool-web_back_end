#!/usr/bin/env python3
"""
This module provides a types-annotated function to safely retrieve
a value from a mapping object using a TypeVar for dynamic default typing.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely returns a value from a dictionary/mapping if the key exists,
    otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
