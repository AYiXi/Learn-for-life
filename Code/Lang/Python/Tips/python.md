```py
# 程序终止时执行
import atexit
 
@atexit.register
def clean():
    pass
```

