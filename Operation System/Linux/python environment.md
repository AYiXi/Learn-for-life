
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

- yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel 
- yum install -y git vim wget zsh curl net-tools tree

- apt-get install libpcre3 libpcre3-dev zlib1g-dev openssl libssl-dev  libffi-dev  dist-upgrade  build-essential python-dev python-setuptools python-pip python-smbus build-essential libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev 

- sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

- [install compile tools and libraries]

- yum -y install epel-release 
- yum install python-pip
- pip install wget

- wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
- tar -zxvf Python-3.8.0.tgz
- cd Python-3.8.0
- ./configure prefix=/usr/local/python3.8
- make && make install

- rm /usr/bin/python /usr/bin/pip /usr/bin/python-config
- ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python 
- ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/py
- ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip
- ln -s /usr/local/python3.8/bin/python3.8-config /usr/bin/python-config
- 