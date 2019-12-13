```py
md5 = hashlib.md5(string).hexdigest()

chr() ord() ^ %
base64.decodestring(code.encode())

XHR breakpoints

ord(a[0]) = a.charCodeAt(0)
```


py中字典转化为字符串和js中返回的Obj不一样, 老是报格式错误


```js
Boolean([]) = true

'0x4' - '0x0' = 0

var x = a || b || c ==>
var x;
if(a){
    x = a;
} else if(b){
    x = b;
} else {
    x = c;
}

var x = a && b && c  ==> 
var x = a;
if(a){
    x = b;
    if(b){
        x = c;
    }
}
```
## 加密方式
- 对称加密: 加密解密密钥相同
  - DES, DES3 AES
- 非对称加密: 分公钥私钥
  - RSA
- 信息摘要算法/签名算法
  - MD5, HMAC, SHA



