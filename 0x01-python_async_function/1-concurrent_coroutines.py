#!/usr/bin/env python3
'''python module'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''async func'''
    delay_list = []
    task_list = []
    for x in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task_list.append(task)
    for task in asyncio.as_completed(task_list):
        value = await task
        delay_list.append(value)
    return delay_list
