(function () {
    'use strict'
    function hook(object, attribute) {
        let original_func = object[attribute]
        object[attribute] = function (){
            console.log('hooked', object, attribute)
            // 执行原函数的逻辑
            let ret = original_func.apply(object, arguments)
            debugger
            return ret
        }
    }
    hook(window, 'btoa')
})()