#!/usr/bin/env python3
'''python module'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes a list of floats and return a float sum'''
    return (k, v*v)
