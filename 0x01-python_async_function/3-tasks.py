#!/usr/bin/env python3
"""async tasks"""

import importlib
import asyncio

MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')

async def test(max_delay: int) -> float:
    """a function (do not create an async function, use the regular function syntax to do this)
    task_wait_random that takes an integer max_delay and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))

