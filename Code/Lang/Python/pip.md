- 添加 sys.path
> windows 添加环境变量 PYTHONPATH=DIR

# Change pip mirror
1. vim ~/.pip/pip.conf
2. Add
```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

3. windows
4. C:\Users\82134\pip\pip.ini
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

5. pip install .\Twisted-20.3.0-cp38-cp38-win_amd64.whl