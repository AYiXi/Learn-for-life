### install gcc
- `xcode-select --install`

### 安装任意来源软件
- sudo spctl --master-disable

### App store Soft
- hidden bar

### Proxy -> Homebrew + Oh-my-zsh
- export https_proxy=http://127.0.0.1:1081 http_proxy=http://127.0.0.1:1081 all_proxy=socks5://127.0.0.1:1080
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
- sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
- export HOMEBREW_NO_AUTO_UPDATE=true
- scutil --proxy [查看代理使用情况]
- lsof -i:1081 [查看端口使用情况]

### [Redis](https://www.jianshu.com/p/3bdfda703552)
- sudo mv redis.tar.gz /usr/local/redis.tar.gz
- cd /usr/local/
- tar -zxvf redis.tar.gz
- cd redis
- sudo make
- sudo make install

### [Charles](https://juejin.im/post/5c0a430f51882516207d205d)
- https://zhile.io
- 48891cf209c6d32bf4

### [JAVA_HOME](https://blog.csdn.net/caoxiaohong1005/article/details/73611424)
- 查询 mac 下的所有 java
  - /usr/libexec/java_home -V

### [Termius 中文乱码](https://www.jianshu.com/p/48228ee59c46)
- export LANG=en_US.UTF-8

### Mac ShortKeys
- ⇧ ⌘ .            -> 显示隐藏文件夹

### Mysql 
- Install
  - Download .dmg file
- Soft link
  - sudo ln -s /usr/local/mysql/bin/mysql /usr/local/bin/mysql
  - sudo ln -s /usr/local/mysql/bin/mysql /usr/bin/mysql 
    - [Operation not permitted operate /usr/bin]

### You-get CERTIFICATE_VERIFY_FAILED
- /Applications/Python\ 3.8/Install\ Certificates.command

### Tesseract
- brew install tesseract

### SSHPASS
- cd ~/Downloads
- curl -O -L http://downloads.sourceforge.net/project/sshpass/sshpass/1.06/sshpass-1.06.tar.gz && tar xvzf sshpass-1.06.tar.gz && cd sshpass-1.06 && ./configure && make && sudo make install