#!/usr/bin/env python3
"""Safely retrieve a value from a dictionary"""
from typing import TypeVar, Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return The value associated with the key if found"""
    if key in dct:
        return dct[key]
    else:
        return default
