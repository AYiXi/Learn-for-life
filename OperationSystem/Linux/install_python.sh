# sudo 权限
# mac 下不行, 只适用于 linux
# ubuntu https://my.oschina.net/randomobject/blog/4300469
cd ~
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel git vim zsh curl net-tools tree epel-release
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
tar -zxvf Python-3.8.0.tgz
cd Python-3.8.0
./configure prefix=/usr/local/python3.8
make && make install
rm -f /usr/bin/python /usr/bin/pip /usr/bin/python-config /usr/bin/py
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/py
ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip
ln -s /usr/local/python3.8/bin/python3.8-config /usr/bin/python-config