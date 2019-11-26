# Note of operation and maintenance

## System partition

- Partition type
  - **MBR**
    - Max support 2.1TB
    - Four partitions
  - **GPT**
    - Max support 9.4ZB (ZB > PB > EB > TB)
    - Unlimited partitions
    - Windows limited 128 partitions
- Device name
  - **/dev/sdb5** >> the first logical partition of the second sata interface hard disk
- Mount point (using an existing empty directory as a mount point)
  - Must partition
    - **/**
    - **swap** >> virtual memory
  - Recommend partition (always must)
    - **/boot**
  - Common partition
    - **/home** >> file server
    - **/www**  >> web server

## Linux directory structure

- **/bin/** >> system commands, soft link of /usr/bin/
- **/sbin/** >> only super user can execute
- **/usr/bin/**
- **/usr/sbin/**
- **/boot/** >> boot files
- **/dev/** >> devices files
- **/etc/** >> system configure files, default installed services
- **/home/** >> general user's home
- **/lib/[lib64]** >> the function library of the system call, soft link of /usr/lib/
- **/mnt/** >> mount directory
- **/usr/local/** >> software install directory
- **/usr/local/src/** >> software source directory
- **/usr/src/kernels/** >> kernel source save location
- **/var/** >> dynamic data, logs, cache
- **/var/www/html** >> default apache web location
- **/var/lib/mysql/** >> default mysql location
- **/var/run/** >> PID(process id) location, soft link of /run/
- **/var/log/** >> system log
- **/var/spool/email/** >> emails
- **/var/spool/cron/** >> timed task

## Netstat
- **netstat -tuln** >> [TCP|UDP|link|ip:port], query all opened port in the system
- **netstat -an | grep "ESTABLISHED" | wc -l** >> established numbers