# Work Dialog

### *2019-07-09*
>- [FIXED] 继续破解cookie加密
>- [FIXED] 继续破解查询返回的网页

### *2019-07-10*
>- [REALI] 接手西青区爬虫项目
>- [LEARN] 完成网页请求下载EXCEL, 但是还不完善
>- [LEARN] 网页请求下载EXCEL很慢, 可能与IP有关, 准备换代理IP
>- [REALI] 成功使用浏览器解析查询返回数据, 但是查询次数多了之后会不返回内容, 
>           而且太多进程也会崩溃, 4个最多了
>- [LEARN] 初步了解了 `.gitignore` 文件

### *2019-07-11*
>- [LEARN] 使用 `pymysql` 同时插入多条的操作
>- [REALI] 实现了从万象云下载的 EXCEL 解析入库
>- [REALI] 基本完成专利查询网站爬虫, 但是网络请求很慢
>- [LEARN] 发现验证专利号的 js 并且成功使用 python 执行成功
>- [LEARN] 在 `__init__` 中添加变量, 知道了需要先赋值为 None

### *2019-07-12*
>- [LEARN] Logger 不能添加逗号分隔输出
>- [LEARN] 下载到正确的万象云 EXCEL 数据, 需要用中文引号
>- [FIXED] 优化了下载 EXCEL 的代码, 基本上不会在中途停止了
>- [FIXED] 优化专利查询网站爬虫
>- [FIXED] 修复了通过万象云 EXCEL 插入错误的问题
>- [FIXED] 整理专利爬虫逻辑
>- [LEARN] 进一步了解 `**kwargs` 参数的使用

### *2019-07-15*
>- [FIXED] EXCEL 入库的错误, 多进程和 `format` 会冲突？
>- [LEARN] 初步了解如何更换代理
>- [LEARN] 初步了解 `async`, 异步网络请求 `aiohttp`
>- [FIXED] 多进程下载 EXCEL 的爬虫, 只需要2分钟
>- [LEARN] linux 中引入必须加 `__init__.py` 文件
>- [LEARN] linux 中配置各种环境, 搞得头大
>- [REALI] 已经完成第二天的数据下载、更新任务

### *2019-07-16*
>- [LEARN] 了解 `__all__` 文件, 但还不确定具体用法
>- [LEARN] 了解代理和 `scheduler` 的实现
>- [LEARN] `Mysql` 用 `%s` 插入 `NULL`
>- [LEARN] `Mysql` 同时插入和更新 `ON DUPLICATE KEY UPDATE`
>- [FIXED] 完善六种判断专利的逻辑
>- [FIXED] 使用了 `re.sub` and `re.subn` 清洗专利号
>- [LEARN] 解决 `ON DUPLICATE KEY UPDATE` 和 `executemany` 冲突的问题, 
>           提升了入库 90% 的时间, 明天继续完善
>- [LEARN] 发现 `github gist`, 发现 `Cherry Tree`

### *2019-07-17*
>- [FIXED] 修复了 `re` 模块验证 sqh 错误的 BUG
>- [FIXED] 从 EXCEL 入库效率提升 80%, 由近 700s 提升到 120s
>- [LEARN] 明白 `re` 匹配非的逻辑
>- [FIXED] 实现了验证专利号的纯 `python` 逻辑  `js --> python`
>           将 4000 多个专利号的验证时间由 `900s` 缩短到 `0.16s`
>- [LEARN] 进一步了解 DEBUG 的逻辑和流程
>- [LEARN] 了解 `mysql` 中 `group by` 的逻辑

### *2019-07-18*
>- [REALI] 安装 `redis`, `mysql`, 能直接在命令行启动
>- [LEARN] 设置 SSH 超时连接为 1 天
>- [REALI] 在 `linux` 上面 push 成功并且本地成功 pull
>- [LEARN] 明白了 `linux` 上面引入包的问题
>- [FIXED] 优化了多进程的查询爬虫
>- [REALI] 准备在 `linux` 上识别验证码

### *2019-07-19*
>- [FIXED] 独立了单独处理 12222 表的程序
>- [LEARN] 了解基本的 `redis` 命令, string、hash、list、set、zset
>- [LEARN] 了解微博 `手机端` 抓取, 能特定爬取一个人的微博
>- [LEARN] 了解 `APP` 爬取, 好像比网页要简单, 但是需要特定工具
>- [LEARN] 了解 `redis` 主从(复制)、哨兵(唤醒)、集群(高并发)及其对应的优势
>- [LEARN] 明白 `cookie` 池的实现原理, 准备实现获取发文信息的 `cookie` 池
>- [LEARN] 自己配置腾讯云安全组
>- [REALI] 完成测试网爬虫 1

### *2019-07-22*
>- [LEARN] 进一步熟悉 `selenium` 的操作, 如元素节点有 text、location 等属性, 打开新窗口用 `JS`
>   切换 `frame(switch_to.frame)` 操作等
>- [FIXED] 完成多进程的插入与数据更新, 耗时 100s 左右, 以往需 600s+, 
>           并且更新不会加量而且增加 `update_time` 字段
>- [LEARN] 了解进度条的实现方法
>- [LEARN] 进一步熟悉 `concurrent` 模块的异常处理和执行逻辑, 好像不会默认调用全局变量
>- [LEARN] 进一步熟悉 `selenium` 显示等待
>- [FIXED] 完成验证专利号的多进程爬虫

### *2019-07-23*
>- [REALI] 重新更新万象云数据并建立索引和完善数据
>- [LEARN] 明白 `and` `or` 的逻辑
>- [LEARN] 通过开启 `telnet`, 开放电脑入站规则的 5000 端口, 降级包 `python -m pip install wsgidav==2.4.1`
>           终于开启了 `pyspider` 的主界面
>- [LEARN] 进一步熟悉 docker 命令和原理

### *2019-07-24*
>- [FIXED] 修复验证专利查询内容时出现 � 的 BUG
>- [LEARN] 安装好 `docker`
>- [LEARN] 阅读了 scrapy 和 scrapy-redis 的源码

### *2019-07-25*
>- [REALI] 安装并运行了 splash, 测试之后发现 splash 速度太慢, 可能与分配的内存小有关系, 
>           以后换电脑再试试
>- [REALI] 在隔壁电脑运行起项目
>- [REALI] 全天监控专利查询内容的爬虫, 基本无问题
>- [REALI] 安装并运行 PostgreSQL

### *2019-07-26*
>- [REALI] 写未缴费专利信息查询的网页

### *2019-07-29*
>- [REALI] 重新搭建开发环境
>- [REALI] 重新设计数据库, 把费用信息表分为已缴费信息和未缴费信息表
>- [REALI] 写未缴费专利信息查询的网页

### *2019-07-30*
>- [LEARN] 链接上数据库必须加 `serverTimezone=UTC`, `URL=jdbc:mysql://localhost:3306/ip?serverTimezone=UTC`
>- [REALI] 重新设计数据库基本完成, 等后端消息, 最终还是用一个表, 找到 专利号+缴费类型+日期
>           为唯一索引, 明白了很多事情想明白比做更简单, 以后应该多思考再动手
>- [REALI] 使用 `openpyxl` 基本完成 excel_api
>- [REALI] 感到未缴费专利信息查询的网页的实现不好实现, 得先系统的学习 django

### *2019-07-31*
>- [LEARN] 在 class 里面应该使用 `ThreadPoolExecutor` 而不是 `ProcessPoolExecutor`
>            看上去效率也并没有区别, 那么这两种 线程 进程 有什么区别呢? 后来发现 class 里面也可以用 `ProcessPoolExecutor`
>- [REALI] 完成发文信息的更新, 更新所有账号大概需要 10s .
>- [FIXED] 优化 费用 与 发文 的 API, 准备设置一个 API 基类
>- [LEARN] 了解 django 的 html 表单向前端传值用 name 属性, 实现搜索功能, 目前只支持专利号搜索
>- [LEARN] 了解 django 从已有数据库开始项目
>- [REALI] 重新配置好 `GitKraken` , 并且 push 了 `Patent` 和 `Django_Patent` 两个项目 
>- [REALI] 更改了 `mysql` 的数据默认存储位置, 以后其他数据库应该也可以了
>- [REALI] 电脑安装上 `Fira Code` 并且使用在 Vscode 和 Sublime Text3 中, Vscode 用 `方正品尚黑` 实现中英多字体

### *2019-08-01*
>- [LEARN] 学会使用 `pymysql` IN 查询 `IN (%s);''' % ','.join(['%s'] * len(data))`
>- [LEARN] 使用 `openpyxl` 一次插入一行完成 excel api 
>- [REALI] 基本完成 Excel 的 API, 能直接接收 json 并直接返回二进制文件, 但是目前张晗还不清楚如何调用直接下载文件
>- [REALI] Pycharm 里面的 Appearance 的 IDE 和 Editor 设置都该用 Greyscale, 否则会有锯齿,
>           另外调试很久终于完成一个白天和一个夜间的配色, 以后就不用调试主题了, 发现菜单页过长可
>           以通过 `Material Theme` 调节但是没找到是哪个选项
>- [REALI] 第一次向 `123.56.13.12` 数据库更新缴费信息, 并且没有出错

### *2019-08-02*
>- [LEARN] `kwargs = kwargs or cf.MYSQL_LOCAL_IP` 实现 or 的用法, 判断非空语法很简洁
>- [LEARN] 从 `Scrapy` 的源代码中学习到了 `__init__`, `hasattr(self, 'start_urls')`, `getattr(self, 'name', None)`
>           以及 `callable` 函数的使用, 可以先 import 到 `__init__` 文件里面, 然后就可以直接从外部导入,
>           明白 `six` 模块是兼容 py2 和 py3 的, 因为类型有些不一样
>- [LEARN] _xx: 不能 import, 只允许本身和之类访问(保护)  __xx: 只允许本身访问(私有) 
>- [LEARN] 阅读 `Scrapy` 文档, 今天阅读了 `Spider`, `Command line`, `Item`, `Selector` 等模块, 安装 `chromedriver`
>- [LEARN] 尝试 `ajax` 成功, 但是 `django` 里面还是不行, 好像是和 `csrf_token` 有关系

### *2019-08-05*
>- [LEARN] 了解 `traceback` 模块, 可以通过 `traceback.extract_stack()[-2].name` 得到该函数调用者的名字
>- [FIXED] 优化费用和发文 API, 优化费用入库的代码结构
>- [LEARN] 阅读 `scrapy` 官方文档和部分源码

### *2019-08-06*
>- [LEARN] 查看B站视频的提取接口
>- [LEARN] 阅读 `scrapy` 官方文档
>- [REALI] 使用 `decorator` 实现同时插入多个数据库, 进一步封装入库的代码结构 
>- [FIXED] 删除项目中不必要的文件, 精简结构, 完善分类

### *2019-08-07*
>- [REALI] 完成政务平台的爬虫, 并且可以根据需要写入到 excel, 对 `openpyxl` 更加熟悉了
>           可以写入多个 sheet 并且插入超链接
>- [FIXED] 插入原本的字符串报错, 但是 `str(s)` 之后, 却没问题了, 也算是一个小坑吧
>- [REALI] 对数据库的重新讨论和设计
>- [REALI] 对邮件发送 API 的熟悉, 但是好像不能发送带有 css 和 js 引用的网页
>- [LEARN] 学会使用 all() 函数, 简洁高效
>- [REALI] 对政务平台的爬虫抽象提取, 以后只需要对新加的网页传入特定参数就可以了
>           熟悉了 lambda, callable 等方法的使用

### *2019-08-08*
>- [LEARN] 进一步熟悉装饰器, 是最先加载的, 会在 `__name__ == __main__` 之前执行, 类似于函数加载
>- [FIXED] 优化完成通过专利号查询在哪一个 excel 里面
>- [FIXED] 重构代码, 新建 main.py 主函数, 以后可以打算在这一个文件里面做所有事情
>- [LEARN] 在 linux 里面布置好程序并且运行成功, 但是阿里云默认关闭 25 端口以致于没法发邮件

### *2019-08-09*
>- [REALI] 完成每天定时 8 点钟给宋老师发政务平台爬虫邮件的代码, linux 的定时任务 `crontab` 不能执行
>           不是可执行的 py 文件, 但是 shell 脚本可以单独执行, 而 shell 添加到 `crontab` 里面也无法执行
>           实在是搞不定, 最后用 python 的 `schedule` 模块搞定 
>- [FIXED] 优化代码结构, 提取出 `settings` 文件, 把操作数据库的几个文件合并, 删除, 使结构清晰

### *2019-08-11*
>- [FIXED] 修复 excel 发送邮件的爬虫的错误

### *2019-08-12*
>- [FIXED] 完善政务平台爬虫, 更加熟悉了对 `all` 和 `any` 的用法, 可以是代码很简洁
>- [LEARN] 阅读 `scrapy` 文档, 了解 `Bloom Filter` 和分布式爬虫的实现, 部署

### *2019-08-13*
>- [LEARN] 继续阅读 `scrapy` 文档, 基本已经都熟悉了, 找时间实操一下 
>- [LEARN] 学习 `mysql` 了解 `ifnull`, `concat`, `isnull` 等函数
>- [LEARN] 学习 `redis` 的基本知识, 模型, 配置, 关键字

### *2019-08-14*
>- [REALI] 调试新的更新方法, 其中有些专利号未更新是因为不在 excel 表中
>- [REALI] 实现进度条并明白其原理, 更改费用 API 的核心代码, 但是进度条并不适用于多线程输出
>- [REALI] 修改所有输出格式为新的类型, 更加直观
>- [LEARN] 使用 `re.match(pattern, str)` 可替换 `any` 函数, 更加简洁, 不知性能如何
>- [LEARN] 学习 `redis` 的基本教程, 了解持久化 rdb/aof , 事务, 消息订阅, 主从复制等常用知识 
>- [REALI] 使用新的程序更新数据库, 更新一次耗时 50s 左右

### *2019-08-15*
>- [FIXED] 修复每天发送邮件的 API, 因为阿里云宕机了, 所以重新启动程序, 顺便修改了一些必要的文件
>           目前还需要详细了解 git 的 merge, fetch 等功能 
>- [REALI] 安装 Node.js, 配置 vscode 的 JavaScript 和 Python 的运行环境
>- [LEARN] 学会 sql 七种 join 和 mysql 的 union, 了解原子性, 唯一性和关系依赖等三范式,
>           `DELETE FROM t_ip_info WHERE id IN (SELECT t.id FROM (SELECT MAX(id) AS id FROM t_ip_info GROUP BY apply_id HAVING count(*) > 1) AS t)`
>           对 mysql 的子查询和清除重复数据有新的认识, 不能在同一个表上既查询又更改, 需要另建一个临时表
>- [LEARN] 学习 JS 的一些基本语法, String 的 charAt, indexOf, index 和 typeof 等

### *2019-08-16*
>- [REALI] 基本完成政务平台爬虫的网页版编写, 实现了 ajax 的发送, css 的自定义, 还剩部署

### *2019-08-17*
>- [REALI] 部署好政务爬虫到 linux
>- [LEARN] django 静态文件部署要分开发环境和生产环境, 学会配置安全组, 配置 mysql 

### *2019-08-19*
>- [REALI] 实现政务爬虫网页的分页机制, `{% if forloop.counter|divisibleby:2 %}` 中 `|` 左右不能加空格
>- [LEARN] 明白 `executor.map` 和 `executor.submit` 的区别, 明白 `ProcessPoolExecutor` 和 `ThreadPoolExecutor` 的区别
>- [LEARN] 明白 `__repr__` 和 `__str__` 的区别, `__str__` 打印有效, `__repr__` 直接有效, 如果 `__str__` 没有被定义,那么就会使用 `__repr__`来代替输出
>- [LEARN] 学习 `collections.namedtuple` 用法, namedtuple('Name', ['attr', 'attr'])
>- [LEARN] 学习 `assert` 用法, `assert not bool([])` 如果 False 则报错
>- [LEARN] 学习集合的 并 交 差 对称差 操作 `| & - ^`
>- [REALI] 第一次写总结性技术博客在简书

### *2019-08-20*
>- [REALI] 熟悉 `django` 的 `re_path`, `reverse`, `namespace` 以及一些常用的过滤器和标签
>- [FIXED] 完善政务爬虫的分页机制
>- [REALI] 完成 `jupyter notebook` 的部署, 以及主题设置
>- [LEARN] 了解 `modin` 库以替代 `pandas`, 但是目前该库并不支持 `windows`

### *2019-08-21*
>- [LEARN] 学会 django 模板 `{{ block.super }}` 继承父类语句, `{{ include "i.html" id="1" }}` 传递变量
>- [LEARN] 学习 django
>- [LEARN] 查看 ip反爬, css反爬, 图片反爬, 验证码反爬等小知识

### *2019-08-22*
>- [REALI] 部署好每天更新政务平台爬虫的程序, 以后不用每天手动更新了 
>- [REALI] 更新政务平台信息公示网站的分页机制和类型颜色改变
>- [LEARN] 学习 `django`
>- [FIXED] 修复 cponline api 的一个BUG, 导致 `实质审查费` 更新不全 

### *2019-08-23*
>- [LEARN] 学习 `django`
>- [FIXED] 优化政务平台的 ajax 逻辑代码, 熟悉 `or` 语句的用法 
>           `ZhengWuCrawl.objects.filter(pk=id_, see=0).update(see=1) or ZhengWuCrawl.objects.filter(pk=id_, see=1).update(see=0)`

### *2019-08-26*
>- [LEARN] 学习 `django` 的高级视图, 表单验证, 分页, 文件上传, cookie session 处理, 上下文处理器
>[LEARN] 学习 `memcached` 的安装和初步使用

### *2019-08-27*
>- [LEARN] 学习 `django` 的上下文管理器, 中间件
>- [REALI] 更改更新费用信息的印花税不打标记的需求, 使用正则匹配来判断 `if re.search('滞纳金|恢复权利|申请费|附加费|印刷费|要求费|审查费', cost_type)`
>- [REALI] 删除以前更新数据库的方法, 精简代码结构
>- [REALI] 按照要求备份新的数据库, 并且只保留一部分代理人的信息
>- [FIXED] 修复爬虫文章名字不全的 BUG, `/a/text() --> /a/@title`
>- [REALI] 删除这个项目多余的文件和代码, 添加必要的注释

### *2019-08-28*
>- [LEARN] 学习 `django` 的验证和授权, 代理用户模型(无法添加新的 Field)和其他用户模型, 权限管理 
>- [LEARN] 了解`gulp`, `npm` 的基本用法
>- [LEARN] 批量创建文件夹 `md/mkdir css js images` 必须进入该父文件夹才行

### *2019-08-29*
>- [REALI] 优化和重写解析入库代码, info 表添加 paid 字段, 添加判断是否是第一次缴费处理函数, 
>            第一次使用 `set` 操作, 大大节约了判断时间, 整个更新时间大概是 `100s` 以内
>- [LEARN] 跟着教程写小饭桌项目, 开始写前端 `sass` 代码, `gulpfile` 运行成功

### *2019-08-30*
>- [LEARN] 学习前端 scss 和一些 js
>- [REALI] 配合后端处理需要的数据, 主要是 sql 语句的书写

### *2019-09-02*
>- [FIXED] 更改 excel 的密码
>- [LEARN] 学习 js 的原型链, 匿名函数的 this 指向 window

### *2019-09-03*
>- [LEARN] 学习 css, js

### *2019-09-04*

>- [LEARN] 搭建好虚拟环境 `virtualenvwrapper` , 并解决引用出错的问题
>- [LEARN] 使用 `vim` 查找  `/name` 和全局查找 `find / -name virtualenvwrapper.sh`
>- [LEARN] `alias pycharm="bash xx/xx"` Linux 上快速启动程序
>- [REALI] 万象云接口调用成功
>- [REALI] 配置好 Typora, 以后可以好好写
>- [LEARN] 学习 css 和 js

### *2019-09-05*

> - [REALI] 