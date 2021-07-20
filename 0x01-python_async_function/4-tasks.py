#!/usr/bin/env python3
'''python module'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''async func'''
    delay_list = []
    task_list = []
    for x in range(n):
        task = task_wait_random(max_delay)
        task_list.append(task)
    for task in asyncio.as_completed(task_list):
        value = await task
        delay_list.append(value)
    return delay_list
