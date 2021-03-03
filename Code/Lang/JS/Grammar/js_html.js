document.querySelectorAll()[0].classList.add('activate') // (.remove)
10 + null + true + [] + undefined + 'ok' + null + [] + 10 + false == '11undefinedoknull10false'
'', 0, NaN, undefined, null == false
!1, !!11 == Boolean(11)
除了 + 可能是字符串拼接, 其余运算符都是数学运算
删除属性: delete person['name'], person['name'] = null
数组和object是一样的; var a = [1, 3, 4]; a.length == a['length'];
基本类型: 按值操作; 引用类型: 操作堆heap的内存地址
栈内存: 执行代码, 存储变量和基本类型
let a = 1; 先等号左边, 再右边, 再赋值
a.x = a = 1; a.x = 1; a = 1; 有先后顺序
类型检测:
typeof //是运算符; typeof null = 'object' 但是null不是对象, 无法区分 /\d1/, [], {}     instanceof 1;
    constructor //基于构造函数检测, 也是基于类
Object.prototype.toString.call() //检测数据类型的最好办法
a > 10 ? (a < 10 ? a++ : a--) : (a > -10 ? a += 2 : null)
css: 子元素相对于父元素定位; 父元素: position: relative;
子元素: position: absolutely; 然后更改子元素的left, right属性
操作DOM, jquery, 操作数据, vue

循环:
// for
// for in
// for of
// do while

验证是否是有效数字, isNaN(), NaN和谁都不相等; if (!isNaN(n)) { 如果是有效数字 }
console.dir()

let bb = box.style.backgroundColor //bb = 'blue'
bb = 'red' // 只改变了值, 未改变堆内存

数据类型 = 基本数据类型 + 引用数据类型

arguments; (...arg) => { }
eval(arg.join('+'))

var a = [2, 3, 4]; a = [1, ...a]
pop, splice, shift, push, slice, replace
concat, indexOf, lastIndexOf, includes, reverse, sort

forEach, map, filter, find, reduce, some, every

floor, ceil, round, random

a.sort((x, y) => x - y)

arr = [...new Set()]

'str'.charAt(0)
'str'.charCodeAt(1)
String.fromCharCode(122)

var st = 'str'
st.substr(); st.substring(), st.slice(), st.indexOf(), st.replace()

str = '123@r13'; str.replace(/[@1]/g, '-')

str.trim()

new Date().toDateString()

setInterval(() => {
    console.log(1)
}, 1000);

document.head; document.body; document.documentElement // head, body, html
document.querySelector('#id')
document.querySelectorAll([selector])
document.querySelectorAll('a')
document.querySelectorAll('#box .aa:nth-child(2)')

children //only element nodes
childNodes //(Include comment and text and elements nodes)
nodeType // node type=node name, 1='#element', 3='#text', 8='#comment', 9='#document'
nodeName
parent

firstChild, lastChild, previousSibling, nextSibling
firstElementChild, lastElementChild, previousElementSibling, nextElementSibling

document.createTextNode('123')
document.createElement()
appendChild //add element to container tail 
removeChild
insertBefore(new_node, specified_node) //add new node before specified node
cloneNode(true / false) //whether clone children nodes
node.querySelector('span').innerText = '123' // span -> text
node.innerHTML = '123'

node.setAttribute('data-index', '1')
node.getAttribute('data-index')
node.removeAttribute('data-index')

let box = document.getElementById('box')
// 获取盒子可视区域宽度 = 内容宽度 + 左右 padding
// 获取盒子可视区域高度 = 内容高度 + 上下 padding
// 内容溢出对它无影响
// 结果属性没有单位
// 结果是整数, 四舍五入
box.clientHeight
box.clientWidth

// one screen w/h
let winH = document.documentElement.clientHeight || document.body.clientHeight
let winW = document.documentElement.clientWidth  || document.body.clientWidth

// left border and top border, no right/bottom attribute
box.clientLeft
box.clientTop

// box real size
box.offsetHeight
box.offsetWidth