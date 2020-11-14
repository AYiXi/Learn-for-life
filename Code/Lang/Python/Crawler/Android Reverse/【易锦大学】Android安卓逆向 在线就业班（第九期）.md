## 环境安装
- JAVA 
  - jdk
  - jre
- Android
  - sdk
  - ndk
- <img alt="env" src="../images/环境.png" height="400px" />

## apk 结构
- lib
  - .so 动态库
- assets
  - 静态资源
- META-INF
  - 签名文件夹
  - MANIFEST.MF
  - MYCERT.RSA
  - MYCERT.SF
  - <img alt="sign" src="../images/sign.png" height="400px" />
- res
- 打包流程
  - <img alt="apk compile" src="../images/apk%20compile.png" height="400px" />

## apk 安装
- /data/app/xx.apk
- /data/dalvik-cache/x86
- /data/data/package_name
- /data/system/packages.xml 
- /system/app system app
- <img alt="apk install" src="../images/apk%20install.png " height="400px" />

## 虚拟机
- <img alt="xuniji" src="../images/xuniji.png" height="400px" />
- Android 5.0 之后就不一样了
- 底层暴露出的接口是一样的, 开发不受影响 

## Android Killer
- 只有 windows 有
- mac 用 [Android Crack Tool](https://github.com/Jermic/Android-Crack-Tool/releases)
- 更新 Apk tool 工具 
- 替换 Android killer/cfgs/injectcode (插件)
- <img alt="android killer" src="../images/android%20killer.png" height="400px" />
- 更改 app 名称, 图标
- <img alt="change app name" src="../images/change_app_name.png"/>
- <img alt="change app icon" src="../images/change_app_icon.png"/>
- 网络有关权限(去除广告)
- <img alt="net" src="../images/android_net_permission.png" />
- 入口文件, 同时有 `main` 和 `LAUNCHER`
  ```xml
  <activity-alias android:theme="@style/lo" android:name="com.ss.android.ugc.aweme.splash.SplashActivity" android:screenOrientation="portrait" android:targetActivity="com.ss.android.ugc.aweme.main.MainActivity">
    <intent-filter>
        <!-- 复制以下两行到另一个 activity, 跳过启动页面 -->
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
  </activity-alias>
  ```
  - 切换主启动的 activity, 然后重新编译 apk
  - onDestroy() 软件退出时执行

## Android System
- <img alt="android" src="../images/android.png" height="400px" />
- <img alt="android2" src="../images/android2.png" height="400px" />
- <img alt="activity" src="../images/activity-life.png" height="400px" />
- <img alt="component" src="../images/compoent.png" height="400px" />
- 布局
  - LinearLayout
  - RelativeLayout
  - ...

## Dalvik
- 寄存器命名
- <img alt="register_param" src="../images/register_param.png" height="400px" />
- dex 文件反汇编
  - .java -> .class -> .dex -> .smali
  - dx --dex --output=Dir: class -> dex
  - Baksmali.jar: dex -> smali
    - java -jar baksmali.jar -o smali_out/classes.dex
  - Smali.jar: smali -> dex
    - java -jar smali.jar smali_out/ -o classes.dex
- [dalvik 指令集](https://juejin.im/post/6844903871500812296)
  - 格式
    - 基础字节码 - 名称后缀/字节码后缀 目的寄存器 源寄存