try {
  var AG_onLoad = function(func) {
    if (
      document.readyState === "complete" ||
      document.readyState === "interactive"
    )
      func();
    else if (document.addEventListener)
      document.addEventListener("DOMContentLoaded", func);
    else if (document.attachEvent)
      document.attachEvent("DOMContentLoaded", func);
  };
  var AG_removeElementById = function(id) {
    var element = document.getElementById(id);
    if (element && element.parentNode) {
      element.parentNode.removeChild(element);
    }
  };
  var AG_removeElementBySelector = function(selector) {
    if (!document.querySelectorAll) {
      return;
    }
    var nodes = document.querySelectorAll(selector);
    if (nodes) {
      for (var i = 0; i < nodes.length; i++) {
        if (nodes[i] && nodes[i].parentNode) {
          nodes[i].parentNode.removeChild(nodes[i]);
        }
      }
    }
  };
  var AG_each = function(selector, fn) {
    if (!document.querySelectorAll) return;
    var elements = document.querySelectorAll(selector);
    for (var i = 0; i < elements.length; i++) {
      fn(elements[i]);
    }
  };
  var AG_removeParent = function(el, fn) {
    while (el && el.parentNode) {
      if (fn(el)) {
        el.parentNode.removeChild(el);
        return;
      }
      el = el.parentNode;
    }
  };
  var AG_removeCookie = function(a) {
    var e = /./;
    /^\/.+\/$/.test(a)
      ? (e = new RegExp(a.slice(1, -1)))
      : "" !== a && (e = new RegExp(a.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
    a = function() {
      for (var a = document.cookie.split(";"), g = a.length; g--; ) {
        cookieStr = a[g];
        var d = cookieStr.indexOf("=");
        if (-1 !== d && ((d = cookieStr.slice(0, d).trim()), e.test(d)))
          for (
            var h = document.location.hostname.split("."), f = 0;
            f < h.length - 1;
            f++
          ) {
            var b = h.slice(f).join(".");
            if (b) {
              var c = d + "=",
                k = "; domain=" + b;
              b = "; domain=." + b;
              document.cookie = c + "; expires=Thu, 01 Jan 1970 00:00:00 GMT";
              document.cookie =
                c + k + "; expires=Thu, 01 Jan 1970 00:00:00 GMT";
              document.cookie =
                c + b + "; expires=Thu, 01 Jan 1970 00:00:00 GMT";
              document.cookie =
                c + "; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
              document.cookie =
                c + k + "; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
              document.cookie =
                c + b + "; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
            }
          }
      }
    };
    a();
    window.addEventListener("beforeunload", a);
  };
  var AG_defineProperty = (function() {
    var p,
      q = Object.defineProperty;
    if ("function" == typeof WeakMap) p = WeakMap;
    else {
      var r = 0,
        t = function() {
          this.a = (r += Math.random()).toString();
        };
      t.prototype.set = function(a, b) {
        var d = a[this.a];
        d && d[0] === a
          ? (d[1] = b)
          : q(a, this.a, {
              value: [a, b],
              writable: !0
            });
        return this;
      };
      t.prototype.get = function(a) {
        var b;
        return (b = a[this.a]) && b[0] === a ? b[1] : void 0;
      };
      t.prototype.has = function(a) {
        var b = a[this.a];
        return b ? b[0] === a : !1;
      };
      p = t;
    }

    function u(a) {
      this.b = a;
      this.h = Object.create(null);
    }

    function v(a, b, d, e) {
      this.a = a;
      this.i = b;
      this.c = d;
      this.f = e;
    }

    function w() {
      this.g = /^([^\\\.]|\\.)*?\./;
      this.j = /\\(.)/g;
      this.a = new p();
    }

    function x(a, b) {
      var d = b.f;
      if (d && !("beforeGet" in d || "beforeSet" in d)) return z(d);
      var e = {
        get: function() {
          var c = b.f;
          c && c.beforeGet && c.beforeGet.call(this, b.a.b);
          a: if ((c = b.g))
            c = A(c) ? c.value : c.get ? c.get.call(this) : void 0;
          else {
            c = b.a.b;
            if (b.i in c && ((c = B(c)), null !== c)) {
              var d = C.call(c, b.i);
              c = d ? d.call(this) : c[b.i];
              break a;
            }
            c = void 0;
          }
          (this === b.a.b || D.call(b.a.b, this)) && E(a, c, b.c);
          return c;
        },
        set: function(c) {
          if (this === b.a.b || D.call(b.a.b, this)) {
            b.f && b.f.beforeSet && (c = b.f.beforeSet.call(this, c, this));
            var d = b.g;
            d && A(d) && d.value === c
              ? (c = !0)
              : ((d = F(b, c, this)),
                G(c) && ((c = H(a, c)), I(a, c, b.c)),
                (c = d));
          } else c = F(b, c, this);
          return c;
        }
      };
      d && J(d, e, K);
      return e;
    }

    function I(a, b, d) {
      for (var e in d.h) {
        var c = d.h[e];
        if (b.h[e]) {
          var h = a,
            g = b.h[e],
            k = c;
          !k.f || g.f || "undefined" === typeof g.a.b || g.g || (g.g = z(k.f));
          g.c && k.c && g.c !== k.c && I(h, g.c, k.c);
        } else {
          g = h = void 0;
          k = a;
          var f = b,
            l = c.i,
            m = "undefined" !== typeof f.b,
            y = !1;
          m && (g = L(f.b, l)) && !g.configurable && ((y = !0), (h = f.b[l]));
          var n = y ? H(k, h) : new u(c.c.b);
          I(k, n, c.c);
          n = new v(f, l, n, c.f);
          f.h[l] = n;
          m &&
            ((n.g = g),
            (m = x(k, n)),
            y
              ? E(k, h, c.c)
              : (q(f.b, l, m),
                g && A(g) && (M(m, g.value, f.b), E(k, g.value, c.c))));
        }
      }
    }

    function E(a, b, d) {
      G(b) && ((b = H(a, b)), I(a, b, d));
    }

    function F(a, b, d) {
      var e = a.g;
      if (!e) {
        e = B(a.a.b);
        if (null !== e && (e = N.call(e, a.i))) return e.call(d, b);
        if (!O(a.a.b)) return !1;
        a.g = {
          value: b,
          configurable: !0,
          writable: !0,
          enumerable: !0
        };
        return !0;
      }
      return M(e, b, d);
    }

    function H(a, b) {
      var d = a.a.get(b);
      d || ((d = new u(b)), a.a.set(b, d));
      return d;
    }

    function A(a) {
      return "undefined" !== typeof a.writable;
    }

    function J(a, b, d) {
      for (var e = 0, c = d.length; e < c; e++) {
        var h = d[e];
        h in a && (b[h] = a[h]);
      }
    }

    function z(a) {
      if (a) {
        var b = {};
        J(a, b, P);
        return b;
      }
    }

    function M(a, b, d) {
      if (A(a)) return a.writable ? ((a.value = b), !0) : !1;
      if (!a.set) return !1;
      a.set.call(d, b);
      return !0;
    }
    var P = "configurable enumerable value get set writable".split(" "),
      K = P.slice(0, 2),
      L = Object.getOwnPropertyDescriptor,
      O = Object.isExtensible,
      B = Object.getPrototypeOf,
      D = Object.prototype.isPrototypeOf,
      C =
        Object.prototype.__lookupGetter__ ||
        function(a) {
          return (a = Q(this, a)) && a.get ? a.get : void 0;
        },
      N =
        Object.prototype.__lookupSetter__ ||
        function(a) {
          return (a = Q(this, a)) && a.set ? a.set : void 0;
        };

    function Q(a, b) {
      if (b in a) {
        for (; !w.hasOwnProperty.call(a, b); ) a = B(a);
        return L(a, b);
      }
    }

    function G(a) {
      var b = typeof a;
      return "function" === b || ("object" === b && null !== a) ? !0 : !1;
    }
    var R;
    return function(a, b, d) {
      R || (R = new w());
      var e = R;
      d = d || window;
      var c = new u();
      a += ".";
      var h = c || new u();
      for (var g = e.g, k = e.j, f, l, m; a; ) {
        f = g.exec(a);
        if (null === f) throw 1;
        f = f[0].length;
        l = a.slice(0, f - 1).replace(k, "$1");
        a = a.slice(f);
        (f = h.h[l])
          ? (m = f.c)
          : ((m = new u()), (f = new v(h, l, m)), (h.h[l] = f));
        h = m;
      }
      if (!f) throw 1;
      a = f;
      a.f = b;
      E(e, d, c);
    };
  })();
  var AG_abortOnPropertyWrite = function(a, b) {
    var c = Math.random()
      .toString(36)
      .substr(2, 8);
    AG_defineProperty(a, {
      beforeSet: function() {
        b && console.warn("AdGuard aborted property write: " + a);
        throw new ReferenceError(c);
      }
    });
    var d = window.onerror;
    window.onerror = function(e) {
      if ("string" === typeof e && -1 !== e.indexOf(c))
        return b && console.warn("AdGuard has caught window.onerror: " + a), !0;
      if (d instanceof Function) return d.apply(this, arguments);
    };
  };
  var AG_abortOnPropertyRead = function(a, b) {
    var c = Math.random()
      .toString(36)
      .substr(2, 8);
    AG_defineProperty(a, {
      beforeGet: function() {
        b && console.warn("AdGuard aborted property read: " + a);
        throw new ReferenceError(c);
      }
    });
    var d = window.onerror;
    window.onerror = function(e) {
      if ("string" === typeof e && -1 !== e.indexOf(c))
        return b && console.warn("AdGuard has caught window.onerror: " + a), !0;
      if (d instanceof Function) return d.apply(this, arguments);
    };
  };
  var AG_abortInlineScript = function(g, b, c) {
    var d = function() {
        if ("currentScript" in document) return document.currentScript;
        var a = document.getElementsByTagName("script");
        return a[a.length - 1];
      },
      e = Math.random()
        .toString(36)
        .substr(2, 8),
      h = d();
    AG_defineProperty(b, {
      beforeGet: function() {
        var a = d();
        if (
          a instanceof HTMLScriptElement &&
          a !== h &&
          "" === a.src &&
          g.test(a.textContent)
        )
          throw (c &&
            console.warn("AdGuard aborted execution of an inline script"),
          new ReferenceError(e));
      }
    });
    var f = window.onerror;
    window.onerror = function(a) {
      if ("string" === typeof a && -1 !== a.indexOf(e))
        return c && console.warn("AdGuard has caught window.onerror: " + b), !0;
      if (f instanceof Function) return f.apply(this, arguments);
    };
  };
  var AG_setConstant = function(e, a) {
    if ("undefined" === a) a = void 0;
    else if ("false" === a) a = !1;
    else if ("true" === a) a = !0;
    else if ("noopFunc" === a) a = function() {};
    else if ("trueFunc" === a)
      a = function() {
        return !0;
      };
    else if ("falseFunc" === a)
      a = function() {
        return !1;
      };
    else if (/^\d+$/.test(a)) {
      if (((a = parseFloat(a)), isNaN(a) || 32767 < Math.abs(a))) return;
    } else return;
    var b = !1;
    AG_defineProperty(e, {
      get: function() {
        return a;
      },
      set: function(c) {
        if (b) var d = !0;
        else
          void 0 !== c && void 0 !== a && typeof c !== typeof a && (b = !0),
            (d = b);
        d && (a = c);
      }
    });
  };
  (function() {
    function d(a, c) {
      if (
        a instanceof Array &&
        "string" === typeof a[0] &&
        (0 <= a[0].indexOf("Crypt" + "onight") ||
          0 <= a[0].indexOf("_cryptonig" + "ht_create"))
      ) {
        var b = null;
        "undefined" === typeof sessionStorage
          ? (b = !1)
          : "1" === sessionStorage.getItem("__u7c4mop23r23239")
          ? (b = !0)
          : "0" === sessionStorage.getItem("__u7c4mop23r23239") && (b = !1);
        if (null == b) {
          b = window.confirm(g("confirm.miner"));
          try {
            if (b) sessionStorage.setItem("__u7c4mop23r23239", "1");
            else if (
              (sessionStorage.setItem("__u7c4mop23r23239", "0"),
              window.confirm(g("confirm.report")))
            ) {
              var d = window.location.hostname,
                f = encodeURIComponent(document.referrer);
              new Image().src =
                "https://crypto.adguard.com/report.png?host=" + d + "&ref=" + f;
            }
          } catch (k) {}
        }
        if (!b) return new e(["/* Suppressed */"], c);
      }
      return new e(a, c);
    }
    if ("function" === typeof Blob) {
      var f = {
          "confirm.miner":
            'AdGuard has detected an attempt by this website to use your browser as a crypto-currency miner. It can create significant CPU load. Press "Cancel" to prevent it.',
          "confirm.report":
            'We are collecting all the information about the websites engaged in hidden crypto-mining. Press "OK" to send an automatic report about this website.'
        },
        h = {
          "confirm.miner":
            'AdGuard обнаружил, что этот сайт пытается использовать ваш браузер для добычи криптовалюты. Это может создать заметную нагрузку на процессор. Нажмите "Отмена", чтобы заблокировать эту попытку.',
          "confirm.report":
            'Мы собираем данные обо всех сайтах, замеченных в попытках скрытого использования ресурсов вашего компьютера. Нажмите "ОК" чтобы отправить нам автоматическое уведомление об этом сайте.'
        },
        g = function(a) {
          var c = navigator.language;
          return c && 0 === c.indexOf("ru") ? h[a] : f[a];
        },
        e = Blob;
      d.prototype = e.prototype;
      window.Blob = d;
    }
  })();
} catch (ex) {
  console.error("Error executing AG js: " + ex);
}
