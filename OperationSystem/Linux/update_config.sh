#!/bin/bash
file="~/.bashrc"
git config --global alias.cm commit & 
git config --global alias.s status &
git config --global alias.ps push &
git config --global alias.pl pull &
git config --global alias.ck checkout &
git config --global alias.cf "config --list" &
git config --global alias.cfg "config --global --list" &
git config --global alias.a "add ." &
git config --global alias.c "commit -a -m" &
git config --global alias.pu push &
git config --global alias.rt remote &
git config --global alias.lg "log --pretty=format:'%h - %an, %ar : %s'" &

echo 'alias mas="git ck master"' >> $file
echo 'alias dev="git ck dev"' >> $file

source $file