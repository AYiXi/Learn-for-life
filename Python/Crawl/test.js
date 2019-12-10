var CryptoJS = CryptoJS || function (u, l) {
    var d = {}
    var n = d.lib = {}
    var p = function () {}
    var s = n.Base = {   // d 是否会变
        extend: function(a) {
            p.prototype = this // this 指什么
            var c = new p
            a && c.mixIn(a)  // ???
            c.hasOwnProperty("init") || (c.init = function () {
                c.$super.init.apply(this, arguments)
            })
            c.init.prototype = c 
            c.$super = this
            return c
        },
        create: function () {
            var a = this.extend()
            a.init.apply(a, arguments)
            return a
        },
        init: function () {

        },
        mixIn: function () {
            for(var c in a) {
                a.hasOwnProperty(c) && (this[c] = a[c])
            }
            a.hasOwnProperty("toString") && (this.toString = a.toString)
        }
    }
}

