#!/bin/bash
sudo vim /etc/sysctl.conf
add "fs.inotify.max_user_watches=524288"
sudo sysctl -p