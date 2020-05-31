### Start redis
- sudo redis-server /etc/redis.conf [whereis redis]
- redis-server -p 9379 &

### Stop redis
- redis-cli -p 9379 shutdown

# 切换数据库
- select 2

# 查看所有
- keys *

# List commands
- lrange key 0 -1
- llen key
- del key