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