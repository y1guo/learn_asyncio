# use
# PYTHONASYNCIODEBUG=1 PYTHONTRACEMALLOC=1 python examples/8_await.py
# to see traceback

import asyncio
import time


async def keep_printing(message: str):
    while True:
        print(f"{message} {time.time()}")
        await asyncio.sleep(0.5)


async def async_main():
    kp = keep_printing("Hey")
    waiter = asyncio.wait_for(kp, 3)
    try:
        waiter
    except asyncio.TimeoutError:
        print("Timeout")


asyncio.run(async_main())
