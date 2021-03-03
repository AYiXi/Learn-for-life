## 启动简单的服务器
- `python -m http.server`

## ContextManager
```py
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
```

## Generator
```py
array = [1, 8, 15]
g = [x for x in array if array.count(x) == 1]
array = [2, 8, 22]

c = list(g)
print(c)

g = (x for x in [2, 8, 22] if [1, 8, 15].count(x) == 1)
print(list(g))

# 迭代器在迭代的时候
# 传入的 x 是取最新的
# 但是, if 判断的时候, 是取的代码定义时的
# 所以答案是8
```

## 程序终止时执行
```py
import atexit
 
@atexit.register
def clean():
    pass

# python 打印多个换行
info = (f'Model: {MINI14}',
        f'Memory: {self.memory}GB',
        f'Hard Disk: {self.hdd}GB',
        f'Graphics Card: {self.gpu}')
print('\n'.join(info))
```