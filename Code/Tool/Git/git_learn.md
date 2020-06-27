## Git 基础
- 直接记录快照, 而非差异比较
- 近乎所有操作都是本地执行
- Git 保证完整性
    - 用SHA-1散列(校验)
    - Git 数据库中保存的信息都是以文件内容的哈希值来索引，而不是文件名
- Git 一般只添加数据
- 三种状态
    - 已提交(committed): 已提交表示数据已经安全的保存在本地数据库中
    - 已修改(modified):  已修改表示修改了文件，但还没保存到数据库中
    - 已暂存(staged): 已暂存表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中
- 基本的 Git 工作流程如下:
    1. 在工作目录中修改文件
    2. 暂存文件，将文件的快照放入暂存区域
    3. 提交更新，找到暂存区域的文件，将快照永久性存储到 Git 仓库目录

## Git 起步
- 安装之后
    - git config --global user.name "AYiXi"
    - git config --global user.email 821346679@qq.com
- 当前配置 / 每一项配置
    - git config --list
    - git config user.name
- 查看帮助
    - git help config
- `clone` 仓库重命名
    - git clone `https://github.com/libgit2/libgit` mylibgit
- Git 协议
    - https://
    - git://
    - SSH, 比如 user@server:path/to/repo.git 
