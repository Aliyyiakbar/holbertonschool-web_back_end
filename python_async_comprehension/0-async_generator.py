#!/usr/bin/env python3
"""
Async Generator Module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10
    after an asynchronous delay of 1 second, repeating 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
