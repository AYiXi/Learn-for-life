
### 虚拟环境设置
```sh
vim ~/.zshrc

> export WORKON_HOME=/root/Envs
> export MSYS_HOME=/c/msys/1.0
> source /usr/local/bin/virtualenvwrapper.sh

ln -s /usr/local/python3.8/bin/virtualenv /usr/bin/virtualenv
source ~/.zrc

USE:
    mkvirtualenv XXX
    workon
    deactivate
```
[MAC install virtualenvwrapper](https://www.jianshu.com/p/dc7ec6a303e3)


### python 找不到 moudle

```shell
vim /etc/profile 
export PYTHONPATH=$PYTHONPATH:/home/my_python_module/
source /etc/profile 
```

### 添加PATH
```shell
在/etc/profile 或者 ~/.bashrc 中输出环境变量
    
export PYTHONPATH=$PYTHONPATH:模块路径
    
source /etc/profile
```

### [Install Python](https://segmentfault.com/a/1190000015628625)
- cd /usr/bin
- ll python*

- yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel  git vim wget zsh curl net-tools tree epel-release 

- apt-get install libpcre3 libpcre3-dev zlib1g-dev openssl libssl-dev  libffi-dev  dist-upgrade  build-essential python-dev python-setuptools python-pip python-smbus build-essential libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev 

- sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

- [install compile tools and libraries]

- wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
- tar -zxvf Python-3.8.0.tgz
- cd Python-3.8.0
- ./configure prefix=/usr/local/python3.8
- make && make install

[link]
- rm /usr/bin/python /usr/bin/pip /usr/bin/python-config /usr/bin/py
- ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python 
- ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/py
- ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip
- ln -s /usr/local/python3.8/bin/python3.8-config /usr/bin/python-config


[settings](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html)
- timedatectl set-timezone Asia/Shanghai
- hostnamectl set-hostname Ayixi_c


[Font](https://blog.csdn.net/azhegps/article/details/79385809)
- cd /usr/share/fonts
- mkdir fangzheng
- cp 方正品尚黑简体.ttf /usr/share/fonts/fangzheng/方正品尚黑简体.ttf
- cd /usr/share/fonts/fangzheng
- mkfontscale
- mkfontdir
- fc-cache -fv
- fc-list :lang=zh

[scrapy]
- pip install incremental
- wget https://files.pythonhosted.org/packages/0b/95/5fff90cd4093c79759d736e5f7c921c8eb7e5057a70d753cdb4e8e5895d7/Twisted-19.10.0.tar.bz2#sha256=7394ba7f272ae722a74f3d969dcf599bc4ef093bc392038748a490f1724a515d
- tar -jxvf Twisted-19.10.0.tar.bz2
- cd Twisted-19.10.0
- python setup.py install
- pip install scrapy
  
[google-chrome]
- wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
- yum install ./google-chrome-stable_current_*.rpm -y
- google-chrome --version
- https://cdn.npm.taobao.org/dist/chromedriver/2.36/chromedriver_linux64.zip
- chmod 755 chromedriver
- cp Li/files/chromedriver /usr/bin/chromedriver

[virtualwrapper]
- vim ~/.zshrc
```sh
export WORKON_HOME=$HOME/.virtualenvs
export MSYS_HOME=/c/msys/1.0
source /usr/local/python3/bin/virtualenvwrapper.sh
```

[vscode]
```py3
{
    "python.pythonPath": ".virtualenvs/Patent/bin/python",
    "code-runner.executorMap": {
        "python": ".virtualenvs/Patent/bin/python",
    }
}
```
