# [python爬虫js加密解密系列文章合集](https://zhuanlan.zhihu.com/p/56157552)

## selenium的封杀与突破，记录一次出师未捷身先死，淘宝、美团对爬虫的深入打击
- unquote
- PID=EC412E1F-C8F4-3AA3-B67B-48A1565D374B 像是身份 ID
- 'browser': {'ie': False, 'chrome': True, 'webdriver': True/undefined},
- [Mitmproxy 替换 js 检测脚本](https://blog.csdn.net/qq_26877377/article/details/83307208)

## Python实现DES、DES3、AES、RSA、MD5、SHA、HMAC加密方式及示例
- 加密总结: 
  - 对称加密(加密解密密钥相同):DES、DES3、AES
  - 非对称加密(分公钥私钥):RSA
  - 信息摘要算法/签名算法:MD5、HMAC、SHA
  - 前端实际使用中MD5、AES、RSA使用频率是最高的
  - 几种加密方式配合次序:采用非对称加密算法管理对称算法的密钥，然后用对称加密算法加密数据，用签名算法生成非对称加密的摘要
  - DES、DES3、AES、RSA、MD5、SHA、HMAC传入的消息或者密钥都是bytes数据类型，不是bytes数据类型的需要先转换; 密钥一般是8的倍数
  - Python实现RSA中，在rsa库中带有生成签名和校对签名的方法
  - 安全性:`DES<DES3=AES<RSA`, 至于MD5、SHA、HMAC不好说了
- [python 实现](https://github.com/ganchaofan0000/crawler/blob/9ff724e5f7a4233f640dc75990cc371c92854c58/crawler_test/Encryption_%20Algorithm.py))