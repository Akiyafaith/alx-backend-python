#!/usr/bin/env python3
"""[Measure the runtime]
"""

import importlib
import asyncio
import time

MODULE_NAME = '1-concurrent_coroutines'
module = importlib.import_module(MODULE_NAME)
wait_n = getattr(module, 'wait_n')


def measure_time(n: int, max_delay: int) -> float:
    """a measure_time function with integers n and max_delay as arguments
    that measures the total execution time
    for wait_n(n, max_delay), and returns total_time / n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
