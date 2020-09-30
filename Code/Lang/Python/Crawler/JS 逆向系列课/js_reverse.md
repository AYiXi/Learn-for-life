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
  - is: running, 查看 websocket 请求
- Source Panel
  - XHR breakpoints
  - DOM breakpoints
  - Event Listener breakpoints
  - Conditional breakpoint

### 无限 debugger
- 条件断点
- hook
- reres 替换本地修改过的文件
- 重写关键函数如上所述
- 对于 (function () {}).constructor === Function
  - Function.prototype.constructor = function() {}
- 点击刷新之后, 很快的点击取消, 可能定位到未跳转的 js, html 等
- `!function() {}`, 这种函数会在 F12 打开调试时自动执行


### 高阶课
- Accept-Encoding: gzip, deflate;  requests 包不会自动带, 可能有暗坑 
- [双核浏览器](http://chrome.cqttech.com/)
- 追溯参数
  - 明文搜索
  - xhr
  - hook
  - 调用栈, 全局断点
  - dom断点
  - 主动debugger
  - warning/error追溯
  - 内存优化分析
  - 事件监听
- 搜索
  - ( w ), (w: function) ...
  - Promise 请求参数
    - 尝试搜索 this.interceptors[.request]