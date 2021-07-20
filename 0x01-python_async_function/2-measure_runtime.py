#!/usr/bin/env python3
'''python module'''
from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure total time'''
    begin = time()
    run(wait_n(n, max_delay))
    finish = time()
    return (finish - begin)/n
