## Git 常用命令
- 获得版本库
    - git init
    - git clone
        - git clone --depth=1 https://github.com/AYiXi/flask-reptiles.git
    - git tag
        - git tag -l 'v1.8.5*' [查看特点标签]
        - git tag -a v1.4 -m "my version 1.4" [添加标签]
        - git tag -a v1.2 9fceb02 [后期打标签]
    - git alias
        - git config --global alias.prebase "git pull --rebase" [别名]
        - git config --global alias.last "log -l HEAD"

- 版本管理
    - git add [将已修改的文件纳入暂存区]
    - git commit
        - git commit --amend [撤销 commit, 用第二次提交代替上一次提交]
    - git rm

- 查看信息
    - git help
    - git log
        - git reflog [查看最近操作]
        - git log -p [查看所有更新日志]
        - git log -p -2 [查看最近两次详细日志]
        - git log --stat [简略的统计信息]
        - git log --pretty
            - git log --pretty=oneline [比较直观]
            - git log --pretty=short
            - git log --pretty=full
            - git log --pretty=fuller
            - git log --pretty=format:"%h - %an, %ar : %s"
            - git log --pretty=format:"%h %s" --graph [以图的形式展示]
            - git log --pretty="%h - %s" --since="2008-10-01" [筛选条件]
    - git diff

- 远程协作
    - git remote
        - git remote -v [查看远程信息]
        - git remote add pb https://github.com/paulboone/ticgit [添加远程仓库]
        - git remote show origin [查看某个远程仓库]
        - git remote rename pb paul [远程仓库rename]

    - git fetch 
    - git pull
        - git pull = git fetch + git merge
    - git pull --rebase = git fetch + git rebase
    - git push
        - git push origin v1.4
        - git push origin --tags [传送所有tag]
        
## 分支模型


## git
1. yum install -y git
2. git config [--global] user.name "ayixi"
3. git config user.email 821346679@qq.com
4. git config --global core.editor vim
5. git config credential.helper store
6. git config --global http.proxy socks5://127.0.0.1:1080
7. git config --global http.proxy http://127.0.0.1:1081
8. git config --global --unset https.proxy

## Remote
- git remote add Sw http://libowang@139.199.23.176:10101/r/~libowang/ShangIp.git
- git remote rename old new
- git remote remove Sw
- git checkout -b local_dev remote_name/remote_dev
- git remote set-head Github -d [delete head branch on remote]
- git remote set-url --add Sw https://github.com/AYiXi/Patent.git [添加url,同时更新]
- git remote -v [detail of remote]

## Tag
- git tag -m "v1.0" 20200316 master
- git push Github v1.0
- git push Github --tags 
- git show v1.0

- git tag [-l]
- git ls-remote --tags
- git tag v1.0.0 [039bf8b] [-m "comment"] 
- git tag -d list
- git push remote :v1.0.0 == git push origin --delete v1.0.0

## Largefiles
- git lfs install
- git lfs track "Soft/Dragon_Center.zip"

## Reset
- git reset
  - --soft: 回退, 已 stage, 未 commit
  - --mixed: 回退, 未 stage, 未 commit
  - --hard: 回退到完全一样

## Stash
- git stash
- git stash list
- git stash apply [–index] [stash_id]
- git stash pop [–index] [stash_id]
- git stash drop [–index] [stash_id]

## Branch
- git checkout -b my-test  [在当前分支下创建my-test的本地分支分支]
- git push Github my-test  [将my-test分支推送到远程]
- git branch --set-upstream-to=origin/my-test [将本地分支my-test关联到远程分支my-test上]
- git branch -a [查看远程分支]
- git push Github :my-test [删除远程分支]
- git branch -r -d Github/my-test [删除远程分支]
- git branch --set-upstream-to=Github/master master[设置默认远程分支]

## New repository
- 在公司服务器上新建一个项目
- git remote add Sw http://libowang@139.199.23.176:10101/r/~libowang/ShangIp.git
- git remote set-url --add Sw https://github.com/AYiXi/ShangIp.git
- git push --set-upstream Sw master
- git pull Sw master --allow-unrelated-histories
- git remote show Sw

## Alias
- ```sh
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
    ```
