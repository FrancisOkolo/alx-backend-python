#!/usr/bin/env python3
'''Async comprehension
'''
import asyncio
from typing import Generator
import random


async def async_comprehension() -> Generator[float, None, None]:
    '''
    looping through an async async generator function
    using async list comprehension
    '''
    b = [i async for i in async_generator()]
    return b
