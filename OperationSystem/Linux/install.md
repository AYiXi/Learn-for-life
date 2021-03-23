1. 选择 minimize install
2. NAT 网络模式
3. 配置 .ssh
   1. ssh-keygen
   2. 把本机的 .pub 放入 authorized_keys 中
   3. 把远程机器的 .pub 放入 authorized_keys 中
4. yum install -y git zsh
5. sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   - [无法翻墙的安装方式](https://www.jianshu.com/p/6b47198fd430)
6. 备份 .zshrc
   1. 安装 [python](https://segmentfault.com/a/1190000015628625)
   2. pip install virtualenvwrapper
7. 安装 [java](https://www.cnblogs.com/stulzq/p/9286878.html)