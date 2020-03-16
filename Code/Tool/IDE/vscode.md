### [自定义代码片段](https://www.jianshu.com/p/1f1132df1def)
```js
File>Preferences>User snippets
javascript.json:
    "Print to console":{
            "prefix":"log",
            "body" :[
                "console.log('$1')",
                "$2"
            ],
            "description":"Log User"
        }

settings.json:
   "editor.snippetSuggestions":"top"

```