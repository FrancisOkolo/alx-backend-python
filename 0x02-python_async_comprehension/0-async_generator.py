#!/usr/bin/env python3
'''async generator
'''

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]::
    '''
    yield a random number between 0 and 10.
    '''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
