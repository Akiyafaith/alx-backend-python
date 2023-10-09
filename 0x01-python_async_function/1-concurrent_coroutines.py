#!/usr/bin/env python3
"""concurrent coroutines"""


import asyncio
from typing import List


MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
