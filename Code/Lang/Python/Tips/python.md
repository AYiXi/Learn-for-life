```py
# 程序终止时执行
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

