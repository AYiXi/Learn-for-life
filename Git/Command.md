## Git 常用命令
- 获得版本库
    - git init
    - git clone
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
6. git config --global http.proxy 'socks5://127.0.0.1:1080'
