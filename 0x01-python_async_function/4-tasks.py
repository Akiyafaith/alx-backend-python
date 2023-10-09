#!/usr/bin/env python3
"""[Tasks]
"""

import importlib
import asyncio
from typing import List

MODULE_NAME = '3-tasks'
module = importlib.import_module(MODULE_NAME)
task_wait_random = getattr(module, 'task_wait_random')


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and
    alter it into a new function task_wait_n"""
tasks = [task_wait_random(max_delay) for _ in range(n)]
return [await task for task in asyncio.as_completed(tasks)]
