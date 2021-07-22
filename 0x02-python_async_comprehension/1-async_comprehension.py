#!/usr/bin/env python3
'''python module'''
import random
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''coroutine'''
    nums = [i async for i in async_generator()]
    return nums
