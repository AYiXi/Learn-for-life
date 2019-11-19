基于Go语言, 开源
Build, Ship and Run Any App, Anywhere
三要素: 仓库, 镜像, 容器

- environment
    - Linux ubuntu 4.15.0-52-generic

- apt install docker.io

- config file
    - etc/default/docker

- execute file
    - /usr/bin/docker

- start
    - service docker start
    - service docker restart
    - docker version

- commands
    - ps -ef | grep docker [check mirror]
    - docker ps
    - docker ps -a
    - docker run hello-world