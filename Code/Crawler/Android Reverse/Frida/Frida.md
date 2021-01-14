### 安装
- pip install frida-tools
  - SSL Error: `sudo /Applications/Python\ 3.n/Install\ Certificates.command`
- frida --version: 下载对应版本的 [frida-server](https://github.com/frida/frida/releases)
- 查询对应的版本: `adb shell getprop ro.product.cpu.abi` -> x86 or arm
- 解压 `unxz frida-server-14.2.3-android-x86_64.xz`
- `mv frida-server-14.2.3-android-x86_64.xz frida-server`
- `adb push frida-server /data/local/tmp/frida-server`
- `chmod +x frida-server`
- `nohup ./frida-server &`