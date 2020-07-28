### Install environment of appium

> install appium desktop
  - 
> install adb
  - brew cask install android-platform-tools
> install android-sdk
  - brew cask install android-sdk
> link adb to sdk
  - ln -s /usr/local/bin/adb /usr/local/share/android-sdk/tools/adb
> install appium-doctor
  - sudo npm install appium-doctor -g
  - brew install carthage

```shell
export JAVA_HOME=$(/usr/libexec/java_home)/bin/java
export PATH=$JAVA_HOME/bin:$PATH
export CLASS_PATH=$JAVA_HOME/lib

export ANDROID_HOME=/usr/local/share/android-sdkb
export PATH=$ANDROID_HOME:$PATH
```


### adb Command
- adb connect 127.0.0.1:5555
- adb kill-server
- adb start-server   

- adb devices [-l]
- adb install com.douguo....apk

### [Charles Settings](https://www.jianshu.com/p/73b134559c76)

### Mitmproxy
- pip install mitmproxy
- SwitchyOmega:http 192.168.80.156[127.0.0.1] 8080
- mitm.it -> install certificate
- z: clear flows
- f: 
  - !(~c 200) -> not 200 request
  - ~d baidu.com
  - ~m post & ~u baidu.com