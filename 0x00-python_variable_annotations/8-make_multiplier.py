#!/usr/bin/env python3
'''python module'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''callable function'''
    def func(num: float) -> float:
        '''function to call'''
        return num*multiplier
    return func
