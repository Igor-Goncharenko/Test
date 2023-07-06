import asyncio
from time import time


async def print1(sec, max_value):
    await asyncio.sleep(abs(max_value // 2 - sec))
    print(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i, 16))


if __name__ == '__main__':
    start = time()
    asyncio.run(main())
    print(time() - start)
