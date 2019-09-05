容器 容器是独立运行的一个或一组应用

客户端 客户端通过命令行或者其他工具使用Docker

主机 一个物理或者虚拟的机器用于执行Docker的守护进程和容器 安装了Docker程序的主机(直接在操作系统上)

仓库 保存镜像，可以理解为代码控制中的代码仓库 DockerHub

 

### 使用步骤

安装Docker

docker仓库下载镜像文件

使用docker运行镜像，会产生一个docker容器

对容器的启动停止既是对软件的启动停止

 

### Linux安装

查看版本(Docker要求内核版本高于3.10)

uname -r

3.10.0-957.el7.x86_64

安装docker

yum install docker

启动docker

systemctl start docker

验证

docker -v

Docker version 1.13.1, build b2f74b2/1.13.1

停止docker

systemctl stop docker

设置开机启动

systemctl enable docker

 

### Docker常用操作

#### 1.镜像操作

检索: docker search 关键字

eg: docker search mysql

rk: 检索镜像信息比如镜像的tag

拉取:docker pull 镜像名:tag

eg：docker pull redis:4.0

rk: :tag是可选的 tag代表标签 大多数是指软件版本,默认是latest

列表: docker images 查看所有本地镜像

删除: docker rmi image-id 删除指定的本地镜像

#### 2.容器操作

运行：docker run -name `container-name` -d image-name

eg: docker run -name myredis -d redis

rk：-name 自定义容器名称  -d 后台运行 image-name 指定镜像模板

列表：docker ps(查看运行中的容器)

rk:加上 -a可以查看所有容器

停止:docker stop container-name/container-id 停止当前运行的容器

启动:docker start container-name/container-id 启动容器

端口映射:-p 80:8080

eg:

docker run -d --name=myTomcat -p 80:8080 238e6d7313e3

docker run -d --name=myTomcat1 -p 81:8080 tomcat:8.5-jdk8

rk：主机端口映射到容器内部端口

容器日志:docker logs container-name/container-id