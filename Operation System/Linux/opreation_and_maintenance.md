# Note of operation and maintenance

## System partition

- Partition type
  - `MBR`
    - Max support 2.1TB
    - Four partitions
  - `GPT`
    - Max support 9.4ZB (ZB > PB > EB > TB)
    - Unlimited partitions
    - Windows limited 128 partitions
- Device name
  - `/dev/sdb5` >> the first logical partition of the second sata interface hard disk
- Mount point (using an existing empty directory as a mount point)
  - Must partition
    - `/`
    - `swap` >> virtual memory
  - Recommend partition (always must)
    - `/boot`
  - Common partition
    - `/home` >> file server
    - `/www`  >> web server


## Linux directory structure

- `/bin/` >> system commands, soft link of /usr/bin/
- `/sbin/` >> only super user can execute
- `/usr/bin/`
- `/usr/sbin/`
- `/boot/` >> boot files
- `/dev/` >> devices files
- `/etc/` >> system configure files, default installed services
- `/home/` >> general user's home
- `/lib/[lib64]` >> the function library of the system call, soft link of /usr/lib/
- `/mnt/` >> mount directory
- `/usr/local/` >> software install directory
- `/usr/local/src/` >> software source directory
- `/usr/src/kernels/` >> kernel source save location
- `/var/` >> dynamic data, logs, cache
- `/var/www/html` >> default apache web location
- `/var/lib/mysql/` >> default mysql location
- `/var/run/` >> PID(process id) location, soft link of /run/
- `/var/log/` >> system log
- `/var/spool/email/` >> emails
- `/var/spool/cron/` >> timed task


## Linux Permission

- general user can't change user or group


## Unzip / Zip
- tar 
  - z[gz]/j[bz2], x[unzip]/c[zip], v[view], f[filename], t[test]
  - `tar -zcvf xxx.tar.gz` >> zip
  - `tar -zxvf xxx.tar.gz -C path xxx/test.txt` >> unzip specific file
  - `tar -ztvf xxx.tar.gz` >> only view


## Netstat

- `cat /etc/sysconfig/network-scripts/ifcfg-eth0` >> check network card information
- `netstat -tuln` >> [TCP|UDP|link|ip:port], query all opened port in the system
- `netstat -an | grep "ESTABLISHED" | wc -l` >> established numbers
- `netstat -rn` >> view gateway ip


## System Trace Command
|
- log file: `/var/log/wtmp/`, `/var/run/utmp`, `var/log/btmp`, `/var/log/lastlog`
  - `w` >> current users
  - `last` >> all logged users
  - `lastlog` >> all users logged time
  - `lasttb` >> Incorrect login information


## Mount

- vim /etc/fstab
- CD
  - mount [-t iso9660] /dev/cdrom /mnt/cdrom >> mount cd
  - umount /mnt/cdrom
- U disk
  - fdisk -l
  - mount -v vfat -o iocharset=utf8 /dev/sdb1 /mnt/usb/
  - umount /mnt/usb/  


# Draft file

- linux 可以不加扩展名, 扩展名都是为了区分
- sync --> shutdown -r now
- IP, mac addr, port, protocol, data of data package

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

- soft link must be `absolute path`
- ln -s file link
- cp -r [copy dir]
  
- write >> send message to another user
- wall >> send message to other users
- w >> logged in user
- sync
- shutdown -r now

- driver: `/lib/modules/3.10.0-862.14.4.el7.x86_64/kernel`


## Vim
  - a
  - A
  - i
  - I
  - o
  - O
  - gg
  - G
  - :n
  - hjkl
  - ^
  - $
  - s, 10s
  - x, nx
  - dd, ndd, :n1,n2d
  - yy, nyy, :n1,n2y
  - p, P
  - u, ctrl + y
  - /xx, n, N
  - 1,10s/old/new/g, %s/old/new/g, /1,10s/^/#/g
  - :r /root/1.txt
  - vim -0 a.txt b.txt
  - vim -O a.txt b.txt

## software installation
- source package [.tar.gz]
  - ./configure --prefix=/usr/local/xxx/
  - make && make install
  - if error in [./configure|make] --> [make clean] else [delete install directory]
- binary package [.rpm] [.dpkg]
- `/var/lib/rpm` >> system db 
- rpm -ivh xxx.rpm >> install dependencies is complicated
- yum
  - yum -y [install|update|remove]
  - yum list
  - yum search
  - yum grouplist
  - yum groupsearch
  - yum groupinstall
  - yum groupremove

- apache -> httpd-2.2.15-15.e16.centos.1.i686.rpm
  - apache process named httpd 
  - ![apache](./images/apache.png)
- default installation position
  - `/etc/`
  - `/usr/bin/`
  - `/usr/lib/`
  - `/usr/share/doc/`
  - `/usr/share/man/`
  - ![pkg](./images/linux_pkg.png)
- service [/etc/init.d/]
- rpm
  - rpm pkg use default installation directory
  - source pgk point installation directory
  - rpm -qf /bin/ls
  - rpm -q[ail] python
  - rpm2cpio /xx/httpdxxx.rpm | cpio -idv ./etc/httpd/conf/httpd.conf
  - Digital certificate import
    - rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
    - rpm -qa | grep gpg-pubkey

- Authority
  - system
    - root
    - general user
  - mysql

- user --> /etc/passwd
- password --> /etc/shadow
- Add "!" Before the password to temporarily prohibit user login
- vim /etc/default/useradd 
  - INACTIVATE 0 >> password expire immediately
  - EXPIRE
  - SHELL=/bin/bash
  - SKEL=/etc/skel
- vim /etc/login.defs
  - PASS_MAX_DAYS 180

- passwd [-lu] user1 (lock, unlock)
  - echo "123" | passwd --stdin ayixi
  - chage -d 0 user1 >> change ayixi::[18227]:0:99999:7::: to 0, let user change password when it login in

- history -c

- usermod >> change user profile
  - usermod -G user1 user2 >> add user2 to user1 group
- gpasswd -a user group >> append user to group
- gpasswd -d user group >> del user from group

- userdel -r user1
- groupdel group
  
- chown -R *
- chown user:group /www/
- chgrp -R *

- su - user
  - env

## ACL permission : used to solve the problem of insufficient user identify for files
- getfacl
- setfacl
  - setfacl -m[b] [-R] [d:]u:user:5 /www/

# SUDO


- locate file  >> /var/lib/mlocate/mlocate.db

- permission
  - rwx

  - umask

  - acl

  - sudo
    - sudo -l
    - /etc/sudoers
    - user ALL=/sbin/shutdown -r now
    - user ALL=/usr/bin/vim   >>  very large permission
    - user ALL=/usr/bin/passwd [A-Za-z]*, !/usr/bin/passwd "", !/usr/bin/passwd root

  - suid
    - setuid >> root soul possession
      - chmod 4755 [u+s] /usr/bin/vim 
      - find -perm -4000 -o -perm -2000 > setuid.txt
    - suid 4 u+s
      - executable file
      - when execute file user >> file owner user
    - sgid 2 g+s
      - executable file and directory
      - when execute file group >> file owner group
    - sbit 1 o+t
      - directory
  
  - chattr
    - chattr [+-i] [+-a] file
    - lsattr file
    - lsattr -d directory

## File System
- Interface
  - IDE 133M/s
  - SCSI 320M/s
  - SATA 600M/s

- super block
  - dumpe2fs [-h] /dev/sda1
- block
- inode

- file system
  - ext
  - ext2
  - ext3
  - ext4 centos6
  - xfs contos7

- df -ahT
- du -sh --max-depth=2
  - du -h / --max-depth=1 

- stat file