```python
# requests.exceptions.SSLError: HTTPSConnectionPool
# 对于证书过期的 https 网址
r = requests.get('https://www.astarblog.cn/index.php/2019/03/14/520.html', verify=False)


```