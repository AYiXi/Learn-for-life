有文件上级目录的写权限才能删除文件

对文件而言最大权限是x, 对目录而言最大权限是w, 目录的x表示可以cd

目录: 0 5 7 
文件: 0 4 6 

umask 默认权限
/etc/profile 环境变量配置文件
whatis uname == man -f uname 
info ls
vim --> n N g G /? 
type ls
help cd

search commands:
whereis 
which
locate dir:/var/lib/mlocate/mlocate.db 
    yum install -y mlocate 
    updatedb
    `vim /etc/updatedb.conf [db conf]`
find
    -a   and
    -o   or
    -not==! not

    find . -name abc
    find . -iname abc
    find . -size +2.1G
    find . [-atime|-mtime|-ctime]
        -atime 文件访问时间
        -mtime 文件数据修改时间
        -ctime 文件状态修改时间 
    find . -perm +444
    find . -type [f|d]
    find . -size +1k -a -type f
    find . -size +1M -a -type f -exec ls -lh {} \;
    find /var/log -mtime +300 -exec ls -lh {} \;