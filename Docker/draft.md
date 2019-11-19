Based on Go-lang, Open Source
Build, Ship and Run Any App, Anywhere
Three Elements: Repository, Image, Container 

- environment
    - Linux ubuntu 4.15.0-52-generic

- apt install docker.io

- config file
    - etc/default/docker

- execute file
    - /usr/bin/docker

- restart
    - service docker start
    - service docker restart
    - docker version

    - systemctl daemon-reload
    - systemctl restart docker

- change aliyun image
    - 容器镜像服务 > 镜像中心 > 镜像加速器
    - vim /etc/docker/daemon.json
    - add {"registry-mirrors": ["https://o01kk3qg.mirror.aliyuncs.com"]}
    - restart

- commands
    - ps -ef | grep docker [check mirror]
    - docker ps
      - docker ps -a          // all
      - docker ps -l          // display recently contains
      - docker ps -n 5        // recent 5 containers
      - docker ps -lq         // only display container id
    - docker run hello-world  
    - docker rmi -f python
    - docker rmi -f $(docker images -qa)

