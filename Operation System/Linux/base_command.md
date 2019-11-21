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


### 设置永久环境变量(windows)

```sh
setx mypc "ssh root@39.105.37.123"
远程登录： %mypc%
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



### 虚拟环境设置

```sh
vim ~/.bashrc

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
export WORKON_HOME=$HOME/envs
source /usr/local/bin/virtualenvwrapper.sh

source ~/.bashrc
```


### Change Computer Hostname
```sh
vim /etc/hostname
reboot
```

### start shangip projects
- nohup python3 /root/ShangIp/manage.py runserver - 0.0.0.0:8000 >> /root/update_zhengwu.txt &
- nohup python3 /root/BigData/manage.py runserver 0.0.0.0:8001 >> /root/bigdata.log &
- nohup python3 /root/Patent/My_API/send_ma
il_to_songjiajia.py >> /root/update_zhengwu.log &

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