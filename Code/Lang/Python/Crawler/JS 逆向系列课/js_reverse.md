# 逆向小知识点

```js
// 函数定义
function a() {} === var a = function() {}
new a() 是一样的


// 通过以上加入 window, document 参数
// sudo npm install -g jsdom
const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;


// 取得 b 的执行结果
function main() {
    var b = function(e) {
            return __g._encrypt(encodeURIComponent(e))
        };

    // 取得 b 的执行结果
    this.encrypt = function (encryptStr) {
        return b(encryptStr)
    }
}
```

### Nodejs Webserver
- window 对象没有, 使用  global 指向 window
- 使用 jsdom
- window.btoa -> base64编码 : Buffer.from("python").toString("base64)

### Chrome Developer Tools
- chrome developer tools filter:
  - -.jpg -.png, 排除某些资源
  - set-cookie-name:d_c0
  - <img src="images/chrome%20filter.png" alt="其他 filter" style="zoom:50%;" />
  - 按住 shift 悬停在请求上, 可以找到请求的发起者和产生的请求
- Source Panel
  - XHR breakpoints
  - DOM breakpoints
  - Event Listener breakpoints
  - Conditional breakpoint