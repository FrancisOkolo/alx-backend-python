#!/usr/bin/env python3
'''basic async syntax
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    returns a random float in random time
    '''
    b = random.uniform(0, max_delay)
    await asyncio.sleep(b)
    return b
