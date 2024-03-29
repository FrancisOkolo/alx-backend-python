#!/usr/bin/env python3
'''Async comprehension
'''
import asyncio
from typing import List
import random
from importlib import import_module as find


async_generator = find('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    looping through an async async generator function
    using async list comprehension
    '''
    b = [i async for i in async_generator()]
    return b
