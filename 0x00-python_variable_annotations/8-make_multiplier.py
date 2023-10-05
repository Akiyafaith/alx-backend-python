#!/usr/bin/env python3
"""Create and return a function that multiplies a float
by the specified multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return A function that takes a float and returns the product."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
