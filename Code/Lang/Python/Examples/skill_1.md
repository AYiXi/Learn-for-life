```python
# 爬虫线程池, 队列
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=4)
while queue_list.qsize() > 0:
    pool.submit(main, queue_list.get())
```