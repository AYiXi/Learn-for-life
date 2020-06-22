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

### [Redis](https://www.jianshu.com/p/3bdfda703552)
- mv redis.tar.gz -> /usr/local/redis-3.2.8
- cd redis-3.2.8
- make
- sudo make install 

### [Charles](https://juejin.im/post/5c0a430f51882516207d205d)
- https://zhile.io
- 48891cf209c6d32bf4