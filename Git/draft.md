 - rm / rm --cached
 - mv 

> delete remote branch and local branch
 - git branch --delete windows
 - git push Patent :windows

> merge branch from master to windows
 - git checkout windows
 - git merge master


> new branch
 - git checkout -b xiqing
 - git push origin xiqing:xiqing
 - git branch -a 
 - git push origin :xiqing == git push origin --delete xiqing

> pull remote branch
 - git fetch origin xiqing:xiqing