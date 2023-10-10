#!/usr/bin/env python3
'''Task 1
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
     takes in 2 int arguments and returns a list
     """
    delay_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    delay_list = sorted(delay_list)
    return delay_list
