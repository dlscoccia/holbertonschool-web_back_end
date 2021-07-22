#!/usr/bin/python3
'''python module'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''coroutine'''
    begin = time.time()
    tasks = []
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    for task in tasks:
        await asyncio.gather(task)
    end = time.time()
    return end - begin
