from contextlib import contextmanager, asynccontextmanager
import asyncio


@contextmanager
def f():
    try:
        yield 2
    finally:
        print(1)


with f() as t:
    print(t)


@asynccontextmanager
async def g():
    try:
        yield 3
    finally:
        print(4)


async def x():
    async with g() as h:
        print(h)


loop = asyncio.get_event_loop()
loop.run_until_complete(x())
