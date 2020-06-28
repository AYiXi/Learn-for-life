### [安装](https://redis.io/download)

> 1. 安装到 /opt 目录下
> 2. cd /opt/redis/src
>
> 3. redis-server &
>
> 4. 任意目录 redis-cli
>
> 5. make install 后 usr/local/bin 下才有redis-server
>
> 6. 修改 redis.conf 中的 daemonize yes 为后台持久化运行

- vim /etc/redis.conf
- ps -ef | grep redis
- kill xxxx
- redis /etc/redis.conf 
- redis-cli -h 39.105.72.96 -p xxxx


### [Command](https://www.runoob.com/redis/redis-tutorial.html)
- Set
  - sadd key value
  - smembers key
  - scard key