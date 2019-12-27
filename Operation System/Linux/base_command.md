### 登录ECS云服务器

```sh
login：root
password：实例密码，可以自己设置
远程登录： ssh root@39.105.37.123
  	                  NIANshao1
```

### VIM 显示行号

```sh
vim ~/.vimrc
set number
```



### 美化终端教程

```sh
https://sspai.com/post/45332
```

### 重新连接

```sh
# 删除之前的信息 
ssh-keygen -R 39.105.37.123
```


### 上传文件/下载文件

```sh
scp a.txt root@39.105.37.123:~
scp -r Patent\ root@39.105.37.123:~ 

scp root@39.105.37.123:/var/www/test.txt
```



### SSH连接超时

```sh
vim /etc/ssh/ssh_config
TCPKeepAlive yes
```

![1567670888529](images/1567670888529.png)



### 生成/安装 requirements.txt(需要虚拟环境)

```sh
pip freeze > requirements.txt
pip install -r requirements.txt
```



### 定时任务 crontab

```sh
crontab -l  显示定时任务
crontab -e 编辑定时任务
vim /etc/crontab 编辑全局定时任务
service cron restart/start/stop

# 执行每日邮件:
nohup python3 /root/Patent/send_mail_to_songjiajia.py >> /root/email.txt &
```



### SSH

```sh
把 C:\Program Files\Git\usr\bin 添加到path环境变量, 就能使用ssh和scp了
```



### 快捷方式

```sh
vim ~/.bashrc

alias pycharm="bash xx/xx"

source ~/.bashrc
```

### Change Computer Hostname
```sh
vim /etc/hostname
reboot
```

### start projects
- nohup python3 /root/ShangIp/manage.py runserver - 0.0.0.0:8000 >> /root/update_zhengwu.txt &
- nohup python3 /root/BigData/manage.py runserver 0.0.0.0:8001 >> /root/bigdata.log &
- nohup python3 /root/Patent/My_API/send_ma
il_to_songjiajia.py >> /root/update_zhengwu.log &
- nohup python app.py >> logs.log &

### files count 
- ls -l | grep "^-" | wc -l  // files count by line
- ls -l | grep "^d" | wc -l  // directory count by line

### curl
- curl https://ip.cn
- curl -i https://ip.cn  // display headers

### tree
- tree -L 2	
- tree -L 2 -p -d 

### du/df
- `du <dir>` (disk usage)
- `du --help`
- `du -sh <dir> <dir>`
- `du -h --max-depth=1 <dir> <dir>`
- `du -ah --max-depth=2`

### Centos Open Ports
1. 查看已打开的端口  # netstat -anp
2. 查看想开的端口是否已开 # firewall-cmd --query-port=666/tcp
若此提示 FirewallD is not running 
表示为不可知的防火墙 需要查看状态并开启防火墙

3. 查看防火墙状态  # systemctl status firewalld
running 状态即防火墙已经开启
dead 状态即防火墙未开启
4. 开启防火墙，# systemctl start firewalld  没有任何提示即开启成功
5. 开启防火墙 # service firewalld start  
关闭防火墙 # systemctl stop firewalld
centos7.3 上述方式可能无法开启，可以先#systemctl unmask firewalld.service 然后 # systemctl start firewalld.service

6. 查看想开的端口是否已开 # firewall-cmd --query-port=666/tcp    提示no表示未开
7. 开永久端口号 firewall-cmd --add-port=666/tcp --permanent   提示    success 表示成功
8. 重新载入配置  # firewall-cmd --reload    比如添加规则之后，需要执行此命令
9. 再次查看想开的端口是否已开  # firewall-cmd --query-port=666/tcp  提示yes表示成功
10. 若移除端口 # firewall-cmd --permanent --remove-port=666/tcp

11. 修改iptables  有些版本需要安装iptables-services # yum install iptables-services 然后修改进目录 /etc/sysconfig/iptables   修改内容


## adduser
1. useradd ayixi
2. passwd ayixi
3. usermod –g root ayixi
4. chmod 640 /etc/sudoers
5. vim /etc/sudousers >> append `ayixi    ALL=(ALL)       ALL`, `Defaults    timestamp_timeout = -1
6. chmod 440 /etc/sudoers
7. userdel -r ayixi
   

## change permission
1. chown ayixi .*
2. chgrp [-R] ayixi .*

