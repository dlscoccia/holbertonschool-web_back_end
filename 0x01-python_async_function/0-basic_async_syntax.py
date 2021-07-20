#!/usr/bin/env python3
'''python module'''
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    '''asyncrhonous coroutine'''
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
