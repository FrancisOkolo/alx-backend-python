#!/usr/bin/env python3
'''Task 2
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the time for wait_n function
    """
    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    total_time = stop - begin
    return total_time / n
