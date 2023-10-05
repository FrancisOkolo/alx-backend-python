#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function with complex types.
    '''
    return lambda x: x * multiplier
