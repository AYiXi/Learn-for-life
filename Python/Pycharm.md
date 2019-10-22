pycharm64.exe.vmoptions
```
-Xms128(4096)m
-Xmx750(4096)m
-XX:ReservedCodeCacheSize=240(不可动)m
-XX:+UseConcMarkSweepGC
-XX:SoftRefLRUPolicyMSPerMB=50
-ea
-XX:CICompilerCount=2
-Dsun.io.useCanonPrefixCache=false
-Djava.net.preferIPv4Stack=true
-Djdk.http.auth.tunneling.disabledSchemes=""
-XX:+HeapDumpOnOutOfMemoryError
-XX:-OmitStackTraceInFastThrow
-Djdk.attach.allowAttachSelf
-Dkotlinx.coroutines.debug=off
-Djdk.module.illegalAccess.silent=true
```

[vmoptions补救](https://intellij-support.jetbrains.com/hc/en-us/articles/206544519)


- CTRL+SHIFT+P [POWER SAVE MODE][FLUENT]
- `hard wrap at` --> 80->10000, Format 时不会自动截断 