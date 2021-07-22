#!/usr/bin/env python3
'''python module'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''coroutine'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
