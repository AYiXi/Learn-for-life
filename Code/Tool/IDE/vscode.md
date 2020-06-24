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

- 同时选择多行
  - alt + shift + click
  - shift + cmd + l

- Shortcuts
  - run                     -> ⌥ r
  - run in terminal         -> ⌥ f
  - find next/previous      -> ⌥ []
  - reveal in sidebar       -> ⌥ v
  - fold                    -> ⌘ .
  - unfold                  -> ⌘ ,
  - show all commands       -> ⌥ 1
  - go to line              -> ⌘ g
  - open previous editor    -> ⌥ j
  - open next editor        -> ⌥ k
  - close editor            -> ⌥ 2
  - reopen editor           -> ⌥ z
  - pin editor              -> ⌥ 3
  - expand selection        -> ⌘ w
  - scroll/page up          -> ⌥ -
  - scroll/page down        -> ⌥ =