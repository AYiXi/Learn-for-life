1. `pip install virtualenvwrapper-win`
2. 新增环境变量 `WORKON_HOME=虚拟环境路径`
3. 创建 `virtualenv D:/Files/Envs/Patent` 
4. `workon Patent`
5. `pip install -r requirements.txt`
6. `pip freeze >> requirements.txt`
7. 虚拟环境名称与项目同名在 Pycharm 中可能会发生错误, 改成 Python 3.7(Patent_), 多加个 "_"



- pip install virtualenvwrapper
- find / -name virtualenv
- find / -name virtualenvwrapper
- ln -s /usr/local/python/bin/virtualenv /usr/bin/virtualenv
- ln -s /usr/local/python/bin/virtualenvwrapper.sh /usr/bin/virtualenvwrapper
- vim .zshrc
  - export WORKON_HOME=$HOME/.virtualenvs
  - export MSYS_HOME=/c/msys/1.0
  - source /usr/local/python3/bin/virtualenvwrapper.sh

- mkvirtualenv -p python3.8 P
- workon P
