export ZSH="/home/ayixi/.oh-my-zsh"
alias z="zsh"
alias c="clear"
alias dk="docker"
alias pag="ps -aux | grep"
alias pa="ps -aux"

# linux virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/python3/bin/virtualenvwrapper.sh
alias pm="python manage.py"

#mac virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_SCRIPT=/Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenv
source /Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh

ZSH_THEME=random

# 显示中文
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8