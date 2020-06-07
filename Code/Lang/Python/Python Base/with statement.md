```python
1. 计算表达式,所得到的对象成为环境管理器, 它必须有 __enter__ 和 __exit__ 方法;
2. 环境管理器的 __enter__ 方法会被调用。如果 as 子句存在,其返回值会赋值给 as 子语句中的变量,否则,直接丢弃。
3. 代码块中嵌套的代码会执行。
4. 如果 with 代码块引发异常,__exit__(type, value, trackback)方法会被调用（带有异常细节）。如果此方法返回值为    False,则异常会重新引发。否则,异常会终止。
6. 如果 with 代码块没有引发异常,__exit__ 方法依然会被调用, 其 type, value 以及 trackback 参数都会以 None 传递。
```

python -m http.server