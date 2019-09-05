## Linux安装部署环境

### Java环境部署

1. 下载对应tar.gz

2. 上传服务器

3. 服务器配置

   ```sh
   1.解压
   [root@localhost Java]# tar -zxvf jdk-8u211-linux-x64.tar.gz
   2.解压完毕需要配置，编辑profile文件：
   [root@localhost Java]# vim /etc/profile
   3.进去以后，在最后添加如下内容，配置环境变量：
   #Java开发者环境
   JAVA_HOME=/root/Java/jdk1.8.0_211
   JRE_HOME=$JAVA_HOME/jre
   CLASS_PATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:
   PATH=.:$JAVA_HOME/bin:$PATH
   export  PATH JAVA_HOME JRE_HOME  CLASS_PATH
   4.修改保存后让它生效
   [root@localhost jdk1.8.0_211]# source /etc/profile
   5.检验java或者javac命令
   [root@localhost jdk1.8.0_211]# java -version
   java version "1.8.0_211"
   Java(TM) SE Runtime Environment (build 1.8.0_211-b12)
   Java HotSpot(TM) 64-Bit Server VM (build 25.211-b12, mixed mode)
   ```



### Nginx安装

1.安装编译工具及库文件

```sh
[root@localhost jdk1.8.0_211]# yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
```

2.安装PCRE

> PCRE 作用是让 Nginx 支持 Rewrite 功能

1. 下载安装包

   ```sh
   [root@localhost ~]# cd /usr/local/src/
   [root@localhost src]# wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
   ```

   

2. 解压安装包

   ```sh
   [root@localhost src]# tar -zxvf pcre-8.35.tar.gz
   ```

3. 进入安装包目录

   ```sh
   [root@localhost src]# cd pcre-8.35
   ```

4. 编译安装

   ```sh
   [root@localhost pcre-8.35]# ./configure
   [root@localhost pcre-8.35]# make && make install
   ```

5. 查看版本

   ```sh
   [root@localhost pcre-8.35]# pcre-config --version
   8.35
   ```

3.安装Nginx

1. 下载Nginx

   ```sh
   [root@localhost pcre-8.35]# cd /usr/local/src
   [root@localhost src]# wget http://nginx.org/download/nginx-1.6.2.tar.gz
   ```

2. 解压安装包

   ```sh
   [root@localhost src]# tar zxvf nginx-1.6.2.tar.gz 
   ```

3. 进入安装包目录

   ```sh
   [root@localhost src]# cd nginx-1.6.2
   ```

4. 编译安装

   ```sh
     [root@localhost nginx-1.6.2]# ./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35
     nginx path prefix: "/usr/local/webserver/nginx"
     nginx binary file: "/usr/local/webserver/nginx/sbin/nginx"
     nginx configuration prefix: "/usr/local/webserver/nginx/conf"
     nginx configuration file: "/usr/local/webserver/nginx/conf/nginx.conf"
     nginx pid file: "/usr/local/webserver/nginx/logs/nginx.pid"
     nginx error log file: "/usr/local/webserver/nginx/logs/error.log"
     nginx http access log file: "/usr/local/webserver/nginx/logs/access.log"
     nginx http client request body temporary files: "client_body_temp"
     nginx http proxy temporary files: "proxy_temp"
     nginx http fastcgi temporary files: "fastcgi_temp"
     nginx http uwsgi temporary files: "uwsgi_temp"
     nginx http scgi temporary files: "scgi_temp"
   ```

5. 测试版本

   ```sh
   [root@localhost nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -v
   nginx version: nginx/1.6.2
   ```

6. 命令提示

   ```sh
   1.检查配置文件nginx.conf的正确性
   [root@localhost nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -t
   nginx: the configuration file /usr/local/webserver/nginx/conf/nginx.conf syntax is ok
   nginx: configuration file /usr/local/webserver/nginx/conf/nginx.conf test is successful
   2.重新载入配置文件
   [root@localhost nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -s reload 
   3.重启 Nginx
   [root@localhost nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -s reopen 
   4.停止 Nginx
   [root@localhost nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -s stop
   ```

### MySQL安装

1. 查看Linux系统版本和内核版本

   ```sh
   查看操作系统版本
   [root@localhost ~]# cat /etc/redhat-release
   CentOS Linux release 7.4.1708 (Core) 
   查看内核版本
   [root@localhost ~]#  uname -r 
   3.10.0-693.el7.x86_64
   ```

2. 卸载历史版本( 使用命令rpm -e --nodeps {-file-name}进行移除操作，移除的时候可能会有依赖，要注意一定的顺序。)我这里暂无

   ```sh
   [root@localhost ~]# rpm -qa | grep mysql
   ```

3. 使用rpm命令安装MySQL组件(使用命令rpm -ivh {-file-name}进行安装操作)

   > 按照依赖关系依次安装rpm包 依赖关系依次为common→libs→client→server

   ```
   [root@localhost ~]# rpm -ivh mysql-community-common-5.7.27-1.el7.x86_64.rpm
   [root@localhost ~]# rpm -ivh mysql-community-libs-5.7.27-1.el7.x86_64.rpm
   [root@localhost ~]# rpm -ivh mysql-community-client-5.7.27-1.el7.x86_64.rpm
   [root@localhost ~]# rpm -ivh mysql-community-server-5.7.27-1.el7.x86_64.rpm  --force --nodeps
   ```

   [^注]: **ivh中， i-install安装；v-verbose进度条；h-hash哈希校验**`

   ```sh
   [root@localhost ~]# rpm -ivh mysql-community-libs-5.7.27-1.el7.x86_64.rpm
   警告：mysql-community-libs-5.7.27-1.el7.x86_64.rpm: 头V3 DSA/SHA1 Signature, 密钥 ID 5072e1f5: NOKEY
   错误：依赖检测失败：
   	mysql-community-common(x86-64) >= 5.7.9 被 mysql-community-libs-5.7.27-1.el7.x86_64 需要
   	mariadb-libs 被 mysql-community-libs-5.7.27-1.el7.x86_64 取代
   
   解决方案:清除yum里所有mariadb依赖包
   [root@localhost ~]# rpm -qa | grep mariadb
   mariadb-libs-5.5.56-2.el7.x86_64
   [root@localhost ~]# rpm -e --nodeps mariadb-libs-5.5.56-2.el7.x86_64
   
   [root@localhost ~]# rpm -ivh mysql-community-server-5.7.27-1.el7.x86_64.rpm
   警告：mysql-community-server-5.7.27-1.el7.x86_64.rpm: 头V3 DSA/SHA1 Signature, 密钥 ID 5072e1f5: NOKEY
   错误：依赖检测失败：
   	net-tools 被 mysql-community-server-5.7.27-1.el7.x86_64 需要
   原因：这是由于yum安装了旧版本的GPG keys造成的
   解决方案:
   [root@localhost ~]# rpm -ivh mysql-community-server-5.7.27-1.el7.x86_64.rpm  --force --nodeps
   ```

4. 注意细节

   1. 执行 yum remove mysql-libs   命令后，会自动删除掉 /etc/ 下的 my.cnf 文件
   2. 对于安装mysql组件，只有安装了 mysql-community-server-5.7.22-1.el7.x86_64.rpm 组件，才会:
      -  在 /etc/下生成 my.cnf 文件 和 my.cnf.d 文件夹
      -  在/var/lib/下生产以下三个文件夹
      -  在/var/log/ 下生成 mysqld.log 文件
      -  在/var/run/ 下生成 mysqld 目录



### MySQL配置

1. 启动mysql

   > 安装完后，使用命令 **service mysqld start** 或 **systemctl start mysqld.service** 启动MySQL服务。（如果mysql服务无法启动，就重启一下系统）

   ```sh
   启动mysql
   [root@localhost ~]# systemctl start mysqld.service 
   查看mysql状态
   [root@localhost ~]# systemctl status mysqld.service
   关闭mysql
   [root@localhost ~]# systemctl stop mysqld.service
   ```

   补充说明

   ```
   查看mysql进程
   [root@localhost ~]# ps -ef|grep mysql
   查看3306端口
   [root@localhost ~]# netstat -anop|grep 3306
   
   Linux使用netstat或者ifconfig命令时，显示命令未找到。
   [root@localhost ~]# netstat -anop|grep 3306
   -bash: netstat: 未找到命令
   [root@localhost ~]# yum search netstat
   已加载插件：fastestmirror
   Loading mirror speeds from cached hostfile
    * base: mirror.jdcloud.com
    * extras: mirror.bit.edu.cn
    * updates: mirror.jdcloud.com
   ============== 匹配：netstat =================
   dstat.noarch : Versatile resource statistics tool
   net-snmp.x86_64 : A collection of SNMP protocol tools and libraries
   net-tools.x86_64 : Basic networking tools
   [root@localhost ~]# yum install net-tools -y
   ```

   

   2.登录MySQL修改root密码

   1. 查看临时密码:
   
      ```sh
      [root@localhost ~]# grep 'temporary password' /var/log/mysqld.log
      2019-09-05T03:42:23.844021Z 1 [Note] A temporary password is generated for root@localhost: nUdCNyay/8B#
      ```
   
      nUdCNyay/8B# 就是登陆密码
   
   2. 使用临时密码登陆,修改root密码
   
      ```sh
      mysql> ALTER USER root@localhost IDENTIFIED  BY '123123';
      ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
      解决方案:
      1.更改策略，设置 validate_password_policy=0;
      mysql> set global validate_password_policy=0;
      Query OK, 0 rows affected (0.00 sec)
      2.重设密码
      mysql> set password for root@localhost=password('ab123123');
      Query OK, 0 rows affected, 1 warning (0.31 sec)
      3.授予远程访问权限
      mysql>  grant all privileges on *.* to 'root' @'%' identified by 'ab123123';
      Query OK, 0 rows affected, 1 warning (0.00 sec)
      4.刷新权限
      mysql> flush privileges;
      Query OK, 0 rows affected (0.00 sec)
      ```
   
   3. 查看当前数据库密码策略
   
      ```sh
      mysql> show VARIABLES like "%password%";
      +---------------------------------------+-------+
      | Variable_name                         | Value |
      +---------------------------------------+-------+
      | default_password_lifetime             | 0     |
      | disconnect_on_expired_password        | ON    |
      | log_builtin_as_identified_by_password | OFF   |
      | mysql_native_password_proxy_users     | OFF   |
      | old_passwords                         | 0     |
      | report_password                       |       |
      | sha256_password_proxy_users           | OFF   |
      | validate_password_check_user_name     | OFF   |
      | validate_password_dictionary_file     |       |
      | validate_password_length              | 8     |
      | validate_password_mixed_case_count    | 1     |
      | validate_password_number_count        | 1     |
      | validate_password_policy              | LOW   |
      | validate_password_special_char_count  | 1     |
      +---------------------------------------+-------+
      14 rows in set (0.35 sec)
      ```
   
      | Policy      |                                                              |
      | ----------- | :----------------------------------------------------------: |
      | 0 or LOW    |                            Length                            |
      | 1 or MEDIUM |  Length;numeric,lowercase/uppercase,and special characters   |
      | 2 or STRONG | Lengt;numeric,lowercase/uppercase,and special characters;dictionary file |

### Linux防火墙相关

> CentOS 7默认使用的是firewall作为防火墙

1. 查看防火墙运行状态

   ```sh
   [root@localhost ~]# firewall-cmd --state
   running
   ```

2. 停止firewall

   ```sh
   [root@localhost ~]# systemctl stop firewalld.service
   ```

3. 禁止firewall 开机自启

   ```sh
   [root@localhost ~]# systemctl disable firewalld.service 
   Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
   Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
   ```

### Linux安装Redis

1. 下载源码包

   ```sh
   [root@localhost src]# wget http://download.redis.io/releases/redis-5.0.5.tar.gz
   ```

2. 解压 

   ```sh
   [root@localhost src]# tar -zxvf redis-5.0.5.tar.gz 
   ```

3. 进入源码包编译安装

   ```sh
   [root@localhost src]# cd redis-5.0.5
   [root@localhost redis-5.0.5]# make 
   ```

4. 检验

   ```sh
   [root@localhost redis-5.0.5]# cd src
   [root@localhost src]# redis-server 
   14627:C 05 Sep 2019 13:48:31.173 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
   14627:C 05 Sep 2019 13:48:31.173 # Redis version=5.0.5, bits=64, commit=00000000, modified=0, pid=14627, just started
   ```

5. 更改配置设置后台运行

   ```sh
   [root@localhost src]# pwd
   /usr/local/src/redis-5.0.5/src
   [root@localhost src]# vim ../redis.conf 
    132 ################################# GENERAL #####################################
    133 
    134 # By default Redis does not run as a daemon. Use 'yes' if you need it.
    135 # Note that Redis will write a pid file in /var/run/redis.pid when daemonized.
    136 daemonize no
    
   将136行修改为
    136 daemonize yes
   ```

#### Redis daemonize介绍

1. daemonize介绍
   - redis.conf配置文件中daemonize守护线程，默认是NO
   - daemonize是用来指定redis是否要用守护线程的方式启动
2. daemonize设置yes或者no的区别
   - `daemonize yes`:redis采用的是单进程多线程的模式。当redis.conf中选项daemonize设置成yes时，代表开启守护进程模式。在该模式下，redis会在后台运行，并将进程pid号写入至redis.conf选项pidfile设置的文件中，此时redis将一直运行，除非手动kill该进程。
   - `daemonize no`:当daemonize选项设置成no时，当前界面将进入redis的命令行界面，exit强制退出或者关闭连接工具(putty,xshell等)都会导致redis进程退出。



### Tomcat的安装

1. 下载

   ```sh
   [root@localhost src]# wget http://us.mirrors.quenda.co/apache/tomcat/tomcat-8/v8.5.45/bin/apache-tomcat-8.5.45.tar.gz
   ```

2. 解压

   ```sh
   [root@localhost src]# tar -zxvf apache-tomcat-8.5.45.tar.gz 
   ```

3. 测试

   ```sh
   [root@localhost bin]# cd /usr/local/src/apache-tomcat-8.5.45/bin
   [root@localhost bin]# sh catalina.sh run
   ```