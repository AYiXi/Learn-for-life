# Patent

### *2019-07-09*
>- [FIXED] 继续破解cookie加密
>- [FIXED] 继续破解查询返回的网页

### *2019-07-10*
>- [REALI] 接手西青区爬虫项目
>- [LEARN] 完成网页请求下载EXCEL, 但是还不完善
>- [LEARN] 网页请求下载EXCEL很慢, 可能与IP有关, 准备换代理IP
>- [REALI] 成功使用浏览器解析查询返回数据, 但是查询次数多了之后会不返回内容, 
           而且太多进程也会崩溃, 4个最多了
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
           提升了入库 90% 的时间, 明天继续完善
>- [LEARN] 发现 `github gist`, 发现 `Cherry Tree`

### *2019-07-17*
>- [FIXED] 修复了 `re` 模块验证 sqh 错误的 BUG
>- [FIXED] 从 EXCEL 入库效率提升 80%, 由近 700s 提升到 120s
>- [LEARN] 明白 `re` 匹配非的逻辑
>- [FIXED] 实现了验证专利号的纯 `python` 逻辑  `js--> python`
           将 4000 多个专利号的验证时间由 `900s` 缩短到 `0.16s`
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
   切换 `frame(switch_to.frame)` 操作等
>- [FIXED] 完成多进程的插入与数据更新, 耗时 100s 左右, 以往需 600s+, 
           并且更新不会加量而且增加 `update_time` 字段
>- [LEARN] 了解进度条的实现方法
>- [LEARN] 进一步熟悉 `concurrent` 模块的异常处理和执行逻辑, 好像不会默认调用全局变量
>- [LEARN] 进一步熟悉 `selenium` 显示等待
>- [FIXED] 完成验证专利号的多进程爬虫

### *2019-07-23*
>- [REALI] 重新更新万象云数据并建立索引和完善数据
>- [LEARN] 明白 `and` `or` 的逻辑
>- [LEARN] 通过开启 `telnet`, 开放电脑入站规则的 5000 端口, 降级包 `python-m pip install wsgidav==2.4.1`
           终于开启了 `pyspider` 的主界面
>- [LEARN] 进一步熟悉 docker 命令和原理

### *2019-07-24*
>- [FIXED] 修复验证专利查询内容时出现 � 的 BUG
>- [LEARN] 安装好 `docker`
>- [LEARN] 阅读了 scrapy 和 scrapy-redis 的源码

### *2019-07-25*
>- [REALI] 安装并运行了 splash, 测试之后发现 splash 速度太慢, 可能与分配的内存小有关系, 
           以后换电脑再试试
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
           为唯一索引, 明白了很多事情想明白比做更简单, 以后应该多思考再动手
>- [REALI] 使用 `openpyxl` 基本完成 excel_api
>- [REALI] 感到未缴费专利信息查询的网页的实现不好实现, 得先系统的学习 django

### *2019-07-31*
>- [LEARN] 在 class 里面应该使用 `ThreadPoolExecutor` 而不是 `ProcessPoolExecutor`
            看上去效率也并没有区别, 那么这两种 线程 进程 有什么区别呢? 后来发现 class 里面也可以用 `ProcessPoolExecutor`
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
           另外调试很久终于完成一个白天和一个夜间的配色, 以后就不用调试主题了, 发现菜单页过长可
           以通过 `Material Theme` 调节但是没找到是哪个选项
>- [REALI] 第一次向 `123.56.13.12` 数据库更新缴费信息, 并且没有出错

### *2019-08-02*
>- [LEARN] `kwargs = kwargs or cf.MYSQL_LOCAL_IP` 实现 or 的用法, 判断非空语法很简洁
>- [LEARN] 从 `Scrapy` 的源代码中学习到了 `__init__`, `hasattr(self, 'start_urls')`, `getattr(self, 'name', None)`
           以及 `callable` 函数的使用, 可以先 import 到 `__init__` 文件里面, 然后就可以直接从外部导入,
           明白 `six` 模块是兼容 py2 和 py3 的, 因为类型有些不一样
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
           可以写入多个 sheet 并且插入超链接
>- [FIXED] 插入原本的字符串报错, 但是 `str(s)` 之后, 却没问题了, 也算是一个小坑吧
>- [REALI] 对数据库的重新讨论和设计
>- [REALI] 对邮件发送 API 的熟悉, 但是好像不能发送带有 css 和 js 引用的网页
>- [LEARN] 学会使用 all() 函数, 简洁高效
>- [REALI] 对政务平台的爬虫抽象提取, 以后只需要对新加的网页传入特定参数就可以了
           熟悉了 lambda, callable 等方法的使用

### *2019-08-08*
>- [LEARN] 进一步熟悉装饰器, 是最先加载的, 会在 `__name__ == __main__` 之前执行, 类似于函数加载
>- [FIXED] 优化完成通过专利号查询在哪一个 excel 里面
>- [FIXED] 重构代码, 新建 main.py 主函数, 以后可以打算在这一个文件里面做所有事情
>- [LEARN] 在 linux 里面布置好程序并且运行成功, 但是阿里云默认关闭 25 端口以致于没法发邮件

### *2019-08-09*
>- [REALI] 完成每天定时 8 点钟给宋老师发政务平台爬虫邮件的代码, linux 的定时任务 `crontab` 不能执行
           不是可执行的 py 文件, 但是 shell 脚本可以单独执行, 而 shell 添加到 `crontab` 里面也无法执行
           实在是搞不定, 最后用 python 的 `schedule` 模块搞定 
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
           目前还需要详细了解 git 的 merge, fetch 等功能 
>- [REALI] 安装 Node.js, 配置 vscode 的 JavaScript 和 Python 的运行环境
>- [LEARN] 学会 sql 七种 join 和 mysql 的 union, 了解原子性, 唯一性和关系依赖等三范式,
           `DELETE FROM t_ip_info WHERE id IN (SELECT t.id FROM (SELECT MAX(id) AS id FROM t_ip_info GROUP BY apply_id HAVING count(*) > 1) AS t)`
           对 mysql 的子查询和清除重复数据有新的认识, 不能在同一个表上既查询又更改, 需要另建一个临时表
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
>- [LEARN] 学习集合的 并 交 差 对称差 操作 `| &- ^`
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
           `ZhengWuCrawl.objects.filter(pk=id_, see=0).update(see=1) or ZhengWuCrawl.objects.filter(pk=id_, see=1).update(see=0)`

### *2019-08-26*
>- [LEARN] 学习 `django` 的高级视图, 表单验证, 分页, 文件上传, cookie session 处理, 上下文处理器
[LEARN] 学习 `memcached` 的安装和初步使用

### *2019-08-27*
>- [LEARN] 学习 `django` 的上下文管理器, 中间件
>- [REALI] 更改更新费用信息的印花税不打标记的需求, 使用正则匹配来判断 `if re.search('滞纳金|恢复权利|申请费|附加费|印刷费|要求费|审查费', cost_type)`
>- [REALI] 删除以前更新数据库的方法, 精简代码结构
>- [REALI] 按照要求备份新的数据库, 并且只保留一部分代理人的信息
>- [FIXED] 修复爬虫文章名字不全的 BUG, `/a/text()--> /a/@title`
>- [REALI] 删除这个项目多余的文件和代码, 添加必要的注释

### *2019-08-28*
>- [LEARN] 学习 `django` 的验证和授权, 代理用户模型(无法添加新的 Field)和其他用户模型, 权限管理 
>- [LEARN] 了解`gulp`, `npm` 的基本用法
>- [LEARN] 批量创建文件夹 `md/mkdir css js images` 必须进入该父文件夹才行

### *2019-08-29*
>- [REALI] 优化和重写解析入库代码, info 表添加 paid 字段, 添加判断是否是第一次缴费处理函数, 
            第一次使用 `set` 操作, 大大节约了判断时间, 整个更新时间大概是 `100s` 以内
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
>- [LEARN] 使用 `vim笔记了` 查找  `/name` 和全局查找 `find /-name virtualenvwrapper.sh`
>- [LEARN] `alias pycharm="bash xx/xx"` Linux 上快速启动程序
>- [REALI] 万象云接口调用成功
>- [REALI] 配置好 Typora, 以后可以好好写
>- [LEARN] 学习 css 和 js

### *2019-09-05*
>- [LEARN] 了解 mycat 和 mysql 的读写分离和主从同步
>- [REALI] 对于没有未缴费信息的专利号更新 is_paid 字段为 1
>- [REALI] 用 `Typora` 整理笔记

### *2019-09-09*
>- [REALI] 重新制作了官网视频, 但还需要改进
>- [LEARN] 学习 `django`

### *2019-09-10*
>- [REALI] 继续官网视频, 基本已经完成
>- [LEARN] 学习 `django`

### *2019-09-11*
>- [REALI] 检查缴费数据的正确性
>- [LEARN] 学习 `django`

### *2019-09-12*
>- [FIXED] 配合张晗修改一个查询费用时间错误的 BUG
>- [FIXED] 修复有些费用字段未更新的 BUG

### *2019-09-16*
>- [REALI] 配置电脑一些常用的信息
>- [REALI] 重构专利缴费的代码

### *2019-09-17*
>- [LEARN] 在操作列表时使用 `deepcopy` 
>- [REALI] 完成部分重构代码
>- [REALI] 进度条更新 `print(f'\r[下载进度]:[{"#" * int((len(self.downloaded_sqh) / self.bar_count)):50}] {"%.2f" % (ratio * 100)}%', end='')`
`

### *2019-09-18*
>- [REALI] 完成对更新费用信息, 发文信息代码逻辑的重构, 效率提高 1.5 倍
>- [LEARN] 了解 G2 和 Echarts 图形框架
>- [LEARN] 了解 `run coverage, profile, concurrency diagram` 分析代码的工具,
           能对代码耗时分模块看清楚
>- [REALI] 使用了异常断点, 但是并没有触发到, 不知道使用的正不正确

### *2019-09-19*
>- [REALI] 完成通过专利权人名称统计专利数量的程序
>- [REALI] 学习 `echarts`, 配置 `vscode`
>- [REALI] 购买 `hugo` 网站模板, 并确定以后的网站风格

### *2019-09-20*
>- [REALI] 配置超人云打码平台自己的账号, 并试用成功
>- [REALI] 增加 `print_not_update_fields` 方法, 打印每天未更新的专利号字段
>- [REALI] 增加流程注释, 代码更加易读易理解 
>- [LEARN] `mysql` 查询日期的语法 `'''SELECT DISTINCT(apply_id) FROM t_ip_info WHERE update_time<'%s';''' % '2019-09-20'`
>- [LEARN] 阿里云安全组配置需要指定端口(3306)
>- [LEARN] EXCEL 函数 `=IF(D2="支出",(true):E2,(false):-E2)`, 文本一定要双引号
>- [FIXED] 修复 `info table` 代理人错误的 BUG


### *2019-09-23*
>- [REALI] 政务平台完成最简单的搜索功能
>- [REALI] 对大数据面板网页进行梳理
>- [REALI] 完成万象云数据的破解   
    1. 空字符串填 None   
    2. session.post 有时候需用参数用 data 而非 params


### *2019-09-24*
>- [LEARN] 知道国资局可以分日期分类型下载 
>- [REALI] 对下载函数进行重构, 但是还没有成功
>- [REALI] 提取大数据网页的模板, 分析网页结构
>- [REALI] 配置 Vscode 开发环境


### *2019-09-25*
>- [REALI] 安装 mongodb, 配置 vscode 的 django 开发环境, 还是用起来不习惯, 代码补全命令不合适
>- [LEARN] 尝试 django 中集成 mongodb, 还不是很理想
>- [LEARN] 了解 flask 中集成 mongodb, 也还没成功
>- [REALI] 实现 B站 爬虫下载一个序列的视频和音频并合并


### *2019-09-26*
>- [REALI] 对公司电脑重装系统, 下载安装必备软件, 准备国庆之后就换成公司电脑工作
>- [REALI] 统计万象云能下载到的数据
>- [REALI] 破解万象云常用统计字段 Excel 的下载
>- [REALI] 完成大的费用信息 Excel 表分时间下载
>- [REALI] 完成 33278 Excel 表的入库

### *2019-09-27*
>- [REALI] 给孟老师统计一些专利信息
>- [LEARN] 调试 js, 了解 js 对象是 {} 
>- [REALI] 对大数据看板网页进行调试
>- [REALI] 完成大的费用信息 Excel 表分时间多线程下载, 基本成功

### *2019-09-29*
>- [REALI] 使用 `yield` 返回数据, 接收之后只需要遍历取值即可
>- [REALI] 实现万象云的数据爬取与解析, 暂存为 json 文件
>- [REALI] 给前端返回 json 数据
>- [REALI] 自定义 `with` 语句, 适用 class 每次结束都要调用一些方法
>- [LEARN] 了解学习 `async/await`, `yield from` 等, 但是目前还没用于实战,
           没有发现比 `concurrent.futures` 的明显优势
>- [REALI] 完善 Excel 爬虫, 有时候可以下载大的 Excel, 但成功不一定是 100%
>- [FIXED] 分析, 删除多个表中不存在的申请号
>- [LEARN] 发现多个线程里面又可以开多个进程

### *2019-09-30*
>- [FIXED] 修复三个数据库中有些专利号未更新的情况, 保证数据最新
>- [LEARN] 创建复杂语句记录的 sql 文件
>- [LEARN] 学习写 js 代码, 并完成了一个很重要的数据处理函数, 对 js 的操作更加熟练
>- [REALI] 下载 Excel 的爬虫第一次没报任何错误全部下载完毕, 耗时 145s, 不知道是不是
           国资局网速变快了, 如果以后也是这样的话, 就可以编写全自动化的代码了, 很大的
           进步
>- [REALI] 部署完成大数据看板, 但是网站访问很慢, 应该和请求的数据量太大和服务器垃圾有关系          


### *2019-10-08*
>- [REALI] 配置新电脑的工作环境, 包括安装 `mysql`, 配置 `pycharm`, 安装 `anaconda`, `git` 设置, 浏览器各种设置等
>- [LEARN] 学习到 `glob.glob1(path, '*.py')` 函数和 `zlib.compress('bytes')` 函数, 对于长文本可以先压缩后存储
>- [LEARN] 学习 `mongodb` 数据库, 了解增删改查等基本操作和一对一, 一对多, 多对多关系的表示


### *2019-10-09*
>- [LEARN] 学会虚拟环境 `virtualenvwarpper-win` 的使用和包管理
>- [REALI] 配置硬件
>- [REALI] 对大数据平台网站结构进行优化调整


### *2019-10-10*
>- [FIXED] 检查并更新未更新的数据
>- [REALI] 尝试下载 11544 的 Excel 表, 但是一直没有成功
>- [REALI] 对大数据平台的网页提取基类, 后续扩展就方便一点
>- [REALI] 更改 Pycharm 的内存大小, 导致打不开, 重新安装破解软件
>- [REALI] 下载 11544 Excel 表成功, 并正常更新到数据库, 通过专利分类的方式下载


### *2019-10-11*
>- [REALI] 实现 js 的匿名函数调用
>- [REALI] 修改 `北京金蓄专利代理有限公司` 不监控的专利 `t_ip_info.is_del=1, t_ip_fee.is_monitor=0` 共 1986 条
>- [REALI] 对万象云分析下载所需要的数据


### *2019-10-12*
>- [REALI]  整理万象云数据来源, 分类统计
>- [LEARN]  修改大数据看板页面, js, css, html 之类


### *2019-10-14*
>- [REALI] 开发大数据看板
>- [LEARN] 完成 `go` 语言的环境安装和初步运行 `var x int = 10 | x := 10`


### *2019-10-15*
>- [FIXED] 修复大数据看板的一些数据显示
>- [REALI] 对区域专利页面的企业数量数据查找和展示
>- [REALI] 对专利年度统计页面的 `js` 文件书写, `forEach 中只能用 A[B], 不能 A.B`
>- [LEARN] 对网站服务架构的探讨(主要是听)
>- [LEARN] 对 `GitHub` 团队合作的了解

### *2019-10-16*
>- [REALI] 配置 `pycharm` 和 `idea`
>- [LEARN] `sqlite3` 插入用 '?' 而不是 '%s', 教程[https://likegeeks.com/python-sqlite3-tutorial/]
>- [REALI] 更改大数据看板首页的饼图为万人均发明数量折线图
>- [REALI] 修改插入缴费数据不更新已经放弃监控的专利
>- [REALI] 修改 `11544` 代理账号的 `dept_id` 为 11
>- [LEARN] 学习一部分 `js`

### *2019-10-17*
>- [REALI] 帮助后端写通过授权号查询专利信息的 `Flask` 接口
>- [REALI] 整理缴费数据的代码, 与宋老师协商解决方案, 准备把全量更新变成增量更新, 以备将来出现未缴费信息接口关闭的问题

### *2019-10-18*
>- [REALI] 修改未缴费数据的代码, 用 `set, tuple, dict` 比较不同, `list` 不可哈希, 所以不可以比较

### *2019-10-21*
>- [REALI] 修改未缴费数据的代码的滞纳金规则
>- [REALI] 为大数据看板重新查找数据

### *2019-10-22*
>- [REALI] 测试未缴费数据的代码
>- [LEARN] 与宋老师沟通大数据看板的一些细节, 战略方向对, 但是细节做的好, 特别是页面布局这块
>- [LEARN] 学习 `git`, 重新认识 `add`, `commit`, `diff`, `config` 等操作的原理, 对自己代码的版本控制做优化
>- [FIXED] 修复不更新专利号依旧在更新的 BUG 

### *2019-10-23*
>- [REALI] 完成未缴费数据部分更新的测试, 以后就可以一直用部分更新的代码运行了, 极大的缩短了时间
>- [REALI] 从社标网商标的简单查询, 官方网站用的是瑞数的js动态混淆, 非常难破解, 等待进一步需求
>- [LEARN] 清楚 `赋值, copy, deepcopy, b=a[:]` 的区别, copy 在第一个参数改变`复杂子元素(如"[] | {} | 序列里的嵌套序列, 字典里的嵌套序列等")`的时候同时会改变(非复杂子元素不会变), js 也是如此
>- [LEARN] 对 js 基础函数 `Math, Array` 等 API 学习, 对 Echarts 的配置项 `title, tooltip` 学习


### *2019-10-28*
>- [LEARN] 学习 `git`, `js`
>- [LEARN] 了解 `Teambition`


### *2019-10-29*
>- [REALI] 帮助后端定制需要返回数据
>- [LEARN] 学习 `js`, 了解 `zsh` 的 random 主题设置和 `alias` 配置(区分 shell)
>- [LEARN] 明白 `js` 中的原型链和上下文执行环境, 作用域和作用域链等

### *2019-10-30*
>- [FIXED] 修复专利名称过长导致数据库插入失效的 `BUG`, 修改 `t_ip_info.name` 的长度为 200 
>- [LEARN] 学习 `js`

### *2019-10-31*
>- [FIXED] 对于新加入专利没有缴费信息的问题, 重新运行一次发现正常, 并且其他数据库并没有出现类似情况, 可能是程序中断 `info` 表先更新导致的 `BUG`
>- [FIXED] 修复部分更新导致标记 `tag` 可能全部为空的情况, 并且对不监控和删除的专利重新整理

### *2019-11-01*
>- [FIXED] 修复标记 `tag` 未随缴费信息更新的 `BUG`

### *2019-11-04*
>- [REALI] 未缴费信息数据更新与检查
>- [LEARN] 
```js
document.querySelectorAll()[0].classList.add('activate') (.remove)
10 + null + true + [] + undefined + 'ok' + null + [] + 10 + false == '11undefinedoknull10false'
'', 0, NaN, undefined, null  == false
!1, !!11 == Boolean(11)
除了 + 可能是字符串拼接, 其余运算符都是数学运算 
删除属性: delete person['name'], person['name'] = null
数组和object是一样的; var a = [1,3,4]; a.length == a['length'];
基本类型: 按值操作; 引用类型: 操作堆heap的内存地址
```
>- [REALI] 对 `Debugger for Chrome` 插件的调试, 能用 `vscode` 调试 `chrome` 代码
 

### *2019-11-05*
>- [REALI] 分析国资局单个专利的各部分信息查询代码, 打算研究 `js` 然后破解到本地使用, 目前还不行
>- [LEARN] 学习 `js` 的类型检测, 操作 DOM, 验证数字, `console.dir()`, `box.style.backgroundColor` 的探索
>- [LEARN] 对 `Mysql` 的继续了解


### *2019-11-06*
>- [REALI] 开需求讨论会
>- [REALI] 重构 + 完善通过专利号查询专利信息的代码

### *2019-11-15*
>- [REALI] 重构代码, 更改 settings 文件以及文件出现的位置
>- [REALI] 测试专利查询的 cookies 过期时间, 准备使用 cookies 池常登录再查询
>- [LEARN] 对正则表达式的学习运用, `\n` 匹配换行
>- [LEARN] 探索 github, 查看 issue 的加载方式(hover 时候加载一个小网页), 对别人的修改评论

### *2019-11-18*
>- [LEARN] 禁止软件联网, 语言乱码的修复, `bandicam` 的设置
>- [LEARN] 学习盒子模型居中以及了解 `flex` 布局, 感觉 `flex` 布局用起来更舒服
>- [LEARN] 学习 docker

### *2019-11-19*
>- [FIXED] 修复连接数据库偶尔连接不上的问题, `pymysql.err.OperationalError` 捕获异常, 重新连接
>- [LEARN] 使用 docker, 用 WSL 连接 windows 的 linux 子系统
>- [LEARN] 对 ssh 的学习, 私钥公钥的配置以及用 vscode 连接远程服务器进行操作
>- [LEARN] 对 linux 软连接以及 bash 启动目录 `/usr/bin` 的理解 
>- [LEARN] 学习 docker

### *2019-11-20*
>- [LEARN] 对阿里云进行快照备份和开放端口访问
>- [LEARN] 学习 docker

### *2019-11-21*
>- [LEARN] 学习 docker
>- [REALI] 实践操作 docker
>- [REALI] 用 git 上传项目到公司服务器
>- [REALI] 对商标信息抓取的研究

### *2019-11-22*
>- [REALI] 给后端在服务器上搭建接口
>- [LEARN] 实战操作 `docker`

### *2019-11-25*
>- [REALI] 测试各网站的商标查询准确性, 除了官方的都不准确
>- [LEARN] 学习 Linux

### *2019-11-26 *
>- [LEARN] 学习 Linux
>- [LEARN] 学习配置 Linux 环境

### *2019-11-27 *
>- [LEARN] 学习 Linux
>- [LEARN] 配置 Linux 环境, 安装 chrome, 新建用户 ayixi, 配置虚拟环境, chromedriver 等

### *2019-11-28 *
>- [LEARN] 学习 Linux 的 包安装[rpm|source_code] 原理, 证书, yum 等 
>- [REALI] 在服务器安装好并成功运行 google-chrome
>- [REALI] 重构 `Patent` 代码, 结构更加合理精简, 删除不必要的文件夹, 但还没完成

### *2019-11-29 *
>- [REALI] 基本完成重构 `Patent` 代码, 合并 `Apis` 到 `Patent`, 结构清晰明了, windows 和 linux 两个平台代码可以通用

### *2019-12-02 *
>- [REALI] 使用 redis 做专利爬虫的时效验证, 以及学习 redis 的一些项, 如默认端口, 守护进程的配置
>- [REALI] 重构专利爬虫的代码