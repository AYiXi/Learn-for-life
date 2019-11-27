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

