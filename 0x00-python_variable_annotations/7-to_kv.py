#!/usr/bin/env python3
"""Create a tuple with the input string
and the square of the integer/float value."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return A tuple with the string 'k' and the square of 'v' as a float."""
    return k, float(v**2)
