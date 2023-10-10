#!/usr/bin/env python3
'''Task 4
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple tasks concurrently time with asyncio
    """
    delay_list = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)
        delay_list = sorted(delay_list)
    return delay_list
