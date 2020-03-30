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
>- [FIXED] 实现了验证专利号的纯 `python` 逻辑  `js --> python`
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
>- [REALI] 完成测试网爬虫

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
>- [REALI] 下载 Excel 的爬虫第一次没报任何错误全部下载完毕, 耗时 145s, 不知道是不是国资局网速变快了, 如果以后也是这样的话, 就可以编写全,很大的进步
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

### *2019-11-26*
>- [LEARN] 学习 Linux
>- [LEARN] 学习配置 Linux 环境

### *2019-11-27*
>- [LEARN] 学习 Linux
>- [LEARN] 配置 Linux 环境, 安装 chrome, 新建用户 ayixi, 配置虚拟环境, chromedriver 等

### *2019-11-28*
>- [LEARN] 学习 Linux 的 包安装[rpm|source_code] 原理, 证书, yum 等 
>- [REALI] 在服务器安装好并成功运行 google-chrome
>- [REALI] 重构 `Patent` 代码, 结构更加合理精简, 删除不必要的文件夹, 但还没完成

### *2019-11-29*
>- [REALI] 基本完成重构 `Patent` 代码, 合并 `Apis` 到 `Patent`, 结构清晰明了, windows 和 linux 两个平台代码可以通用

### *2019-12-02*
>- [REALI] 使用 redis 做专利爬虫的时效验证, 以及学习 redis 的一些项, 如默认端口, 守护进程的配置
>- [REALI] 重构专利爬虫的代码

### *2019-12-03*
>- [LEARN] 学习 linux 的 `rwx|umask|suid|acl|sudo|chattr` 权限管理和文件系统
>- [REALI] 重建 django 项目到 patent 目录下, 准备以后都放在一起
>- [REALI] 对投票网站的探索, 刷屏, 需要更换 ip, 对爬虫 ip 的更换使用

### *2019-12-04*
>- [LEARN] 对国资局网站加密方式的研究
>- [LEARN] 大致了解 cookie 的生成方式, 有道翻译, 某个ip网址参数加密的破解方法, 还得动手实现才行.

### *2019-12-05*
>- [LEARN] 学习 `fiddler`
>- [LEARN] 研究国资局加密的 js 文件

### *2019-12-06*
>- [FIXED] 修复两个bug, 1. 数据更新字段错误, 2. 数据更新年度冲突
>- [LEARN] 配置 `debugger for chrome` 插件
>- [REALI] 调试国资局的js, 并取得一定的进展

### *2019-12-09*
>- [FIXED] 修复一个bug
>- [REALI] 对烯牛数据的加密代码的调试
>- [REALI] 对国资局加密算法的调试, 初步了解流程

### *2019-12-10*
>- [REALI] 继续了解瑞数的加密逻辑
>- [REALI] 破解中利汇网站的加密数据和专利查询, 可以留作备用
>- [REALI] 破解佰腾网的专利查询
>- [REALI] 对加密算法的调试和对js的深入学习

### *2019-12-11*
>- [REALI] 研究中利汇js的加密算法, 大致了解了一种js的加密逻辑, 对js加密有更加深入的认识
>- [FIXED] 修复一个bug, 导致同时出现两年年费有标记的情况, 因为数据已缴费但是并没有更改

### *2019-12-12*
>- [LEARN] 开会讨论工作中遇到的问题和解决方法, 对服务器权限管理, 数据库权限管理, 统一代码风格, 每日问题等多个重要不紧急的事情做了讨论, 大家都很积极的发言, 对之后的遇到问题的提交, 解决方法和开会时发言过程做了规划, 对沟通方式和态度都做了一些探讨, 总的来说收获还是很大
>- [LEARN] 在网上搜索国资局加密方式解决方案是看到了一种用 splash 渲染得到 cookie 的方式, 在浏览器通过 docker 配置 splash 框架并且运行发现并不能得到加密过的 cookie, 并且也不能请求商标网, 但是对其他网站倒是可以得到 js 渲染后的 cookie, 可能是这两个网站的瑞数加密比较严苛, 这种方法目前不行
>- [LEARN] 在网上找到了一个裁判文书网的爬虫库, 加密方式和国资局基本相同, 试着调试了一下, 虽然加密方法已经失效, 但是那个人的代码风格非常好, 从那个代码里学到很多新的东西, 而且加密逻辑也是可以借鉴的

### *2019-12-13*
>- [REALI] 新加入了更新未缴费信息的逻辑, 使得现在的缴费状态和国资局完全同步, 再也不用担心用户已缴费但是没有在我们平台记录的情况
>- [LEARN] 学习使用 retry 对代码进行优化, 减少了代码量并且使逻辑更加清晰

### *2019-12-16*
>- [REALI] 与后端协商和确认滞纳金数据信息的准确性问题
>- [REALI] 更改西青线上的 mysql 至全部 ip 可以使用 root 密码登录, 并且通过 django 连接上
>- [REALI] 设置环境变量替换django的配置, 使得代码更加安全, linux 环境变量只能用双引号而不能是单引号, 并且带有 root 的环境变量不生效
>- [REALI] 开会讨论费用未提醒到用户的原因, 并且确定了追责制度, 然后检查了自己的代码和数据库的数据, 目前尚未发现数据更新有什么异常问题
>- [LEARN] 学习使用 django 的 user 模型, 准备开发注册和登出页面
>- [REALI] 与张晗沟通需要更新西青区的项目数据的一些事项

### *2019-12-17*
>- [REALI] 沟通开发区的项目需要的数据, 但是还是没有定下来, 只给了个大体的范围, 我自己生成检索式在万象云查询了一下, 数据是能拿到的,  但就是需求不是很明确,  明天得再确认一下
>- [REALI] 寻找所有申请人大于一个的专利号, 但是
>- [REALI] 对之前西青区项目代码的研究, 对数据库的重建, 代码很乱, 看起来很吃力

### *2019-12-18*
>- [LEARN] 子类继承父类初始化参数时 super 不加参数, `super().__init__()`
>- [REALI] 完成之前西青区项目的数据统计


### *2019-12-19*
>- [REALI] 仔细处理西青区项目的数据, 检查准确性, 重新下载并更新数据, 有几点体会:
1. 数据中往往有很多脏数据需要先清洗才能分析
2. 对于sql条件查询的综合运用
3. 对业务逻辑的了解程度能决定工作的效率, 自己也没有太了解, 这也是导致花了很多时间去了解业务的各项数据, 作为数据统计, 应该对每项指标敏感并且了解详细, 这是应该好好学习的一点
4. 很多细节不是想象中那么简单, 处理数据时应该多加小心和注意

### *2019-12-20*
>- [REALI] 更新西青区项目数据, 可以保证和万象云一模一样, 并且可以动态更新了, 更新所有的只需要十几秒, 可以做到日更
>- [LEARN] 很多时候方法不行就换一种方法, 先想明白怎么做再做
>- [LEARN] 很多时候方法不行就换一种方法, 先想明白怎么做再做
>- [THINK] 
1. 有时候不该跟随别人的方法盲目的去做, 别人的方法很可能会误导自己的思路
2. 哪怕时间再紧急, 都应该先想明白怎么做, 然后再做, 要不然只是无用功 
3. 对业务逻辑代码优化是一个持续的过程
4. 应该多和领导沟通交流, 以确保自己的业务理解不会错, 以及正确的认识到项目的轻重程度

### *2019-12-23*
>- [REALI] 对西青区项目的文档的总结和书写
>- [LEARN] 使用 pandas 获取一些 sql 表达式才能获取的数据
>- [LEARN] 对 sql 中日期转换表达的学习和使用
>- [REALI] 解决 navicat 查询数据慢的问题
>- [REALI] 对缴费数据更新项目的一部分重构

### *2019-12-24*
>- [LEARN] 学习 pandas 的一些操作, 稍微熟练点了
>- [LEARN] 确认发文信息更新的代码

### *2019-12-25*
>- [REALI] 重新更新所有的企业的数据
>- [REALI] 对数据的压缩分类, 并传给后端
>- [LEARN] 阅读 `retrying` 的源码

### *2019-12-26*
>- [REALI] 完成西青区项目的数据更新的自动化流程
>- [LEARN] 学习到了 `Path` 模块的使用, `Path(p).glob('*.xlsx')`, `Path.joinpath(a, b, c)` 等
>- [LEARN] 阅读 `retrying` 的源码, 对装饰器用法的深入理解
>- [LEARN] 对 yield 的使用

### *2019-12-27*
>- [REALI] 把政务平台的爬虫项目迁移到西青区的服务器上面
>- [REALI] 优化政务平台的爬虫代码
>- [REALI] 配置服务器上django的开发环境, 包括环境变量
>- [REALI] 配置 vscode 上面的 django 项目开发环境 
>- [REALI] 修复一下迁移平台出现的错误
>- [REALI] 完成用户模型的创建, 各种表的创建

### *2019-12-30*
>- [LEARN] 对 `django` 用户系统的开发和学习
>- [LEARN] 对 python 接入阿里云短信服务文档的学习和查阅
>- [REALI] 对新增的政务平台的爬虫网站的查看, 并新完成 2 个网站的爬取

### *2020-01-02*
>- [REALI] 检查专利的更新情况
>- [REALI] 完成部分网站的政务平台公告的爬虫 (36 / 37)

### *2020-01-03*
>- [REALI] 基本完成政务平台公告爬虫的架构和设计, 可能还有需要修改的细节
>- [REALI] 修改一些源码的默认参数, json 和 logging 的编码都默认设置为 utf8

### *2020-01-06*
>- [REALI] 完成网站的政务平台公告的爬虫
>- [REALI] 对 django 用户系统的学习和开发

### *2020-01-07*
>- [LEARN] 学习了解 `show full processlist`; 和 `kill` 命令

### *2020-01-08*
>- [REALI] 更新专利信息并与王天勇讲解演示
>- [REALI] 更新西青区项目的专利数据
>- [REALI] 检查专利的更新情况
>- [REALI] 完成政务平台的部署和展示
>- [REALI] 对用户系统和权限系统的开发
>- [LEARN] 对 vscode 无法跟踪代码的设置
>- [LEARN] 对 `rest_framework` 的权限系统的了解

### *2020-01-09*
>- [REALI] 书写更新数据的文档
>- [LEARN] 查看 django 的源码, 包括 view, form等, 大概能看懂一些
>- [LEARN] 学习 classmethod 的实现方式和用法
>- [REALI] 使用 selenium 配合 firefox 对国资局进行爬取, 已初步见到成效

### *2020-01-10*
>- [REALI] `dict.setdefault(key, value)` 如果 key 存在, 则 value 不变
>- [LEARN] 学习 django 部分源码
>- [LEARN] 学习 pyppeteer
>- [REALI] 开发用户注册模块

### *2020-01-14*
>- [REALI] 完成除验证手机号之外的用户模块
>- [LEARN] 学习 django 部分源码
>- [REALI] 对国资局爬虫的浏览器结合代码方法的研究, 发现另外的加密参数, 暂时不能通过先浏览器再代码的方式获取到想要的数据, 可能需要考虑纯浏览器请求了

### *2020-01-15*
>- [REALI] 对国资局的 Firefox 爬虫进行编码, 可以实现查询功能, 还需要考虑部署和稳定性
>- [LEARN] 深入的学习了 selenium 的各种 api

### *2020-01-16*
>- [REALI] 检查专利数据正确性
>- [REALI] 国资局爬虫项目:
>- 本地可以通过登录爬虫查询专利了, 一个登录状态能查询 165 个专利号, 之后需要换号登录
>   - 服务器端使用模拟浏览器登录有几个问题
>       - 网速太差导致请求经常失败
>       - 一旦开始运行程序会导致服务器 CPU 资源占用瞬间达到 99%, 会影响其他进程
>   - 目前解决思路:
>       - 本地请求, 然后通过 redis 数据库与服务器同步, 这样就不能关闭本地的电脑很运行的程序
>       - 尝试其他模拟浏览器登录的方案, 不过资源消耗应该是差不多
>- [LEARN] 学习 selenium, pyppeteer

### *2020-01-17*
[REALI]
- 学习使用 redis 作为国资局爬虫的缓存
- 完成最基本的国资局爬虫, 能通过输入专利号查询专利信息, 但是速度有点慢, 大概查询一次要 6-7s, 有优化的空间
- 初步完成通过专利号查询专利信息的接口的架构, 使用 本地浏览器+redis缓存 
- 已经查询过的专利会在缓存中, 下一次再查寻同样的专利号会无延迟
- 目前还有很多地方需要优化:
    - 爬虫过期时效问题, 大概每15分钟, 或者查询 165 次就会失效, 需要重新登陆
    - 缓存数据库的时效问题, 过期时间和刷新时间
    - 验证码平台登录的费用问题, 是否需要一直登录, 还需要和后端商量
    - 是否需要接入中利汇的专利爬虫, 这样就会有两套方案, 返回速度也会更快
    - 代码逻辑结构如何优化
- 国资局自动下载excel测试可行, 但是还有也一些问题, 比如每下载完成一个表之后, 就会报错
[LEARN]
- `redis` 的相关操作
- `pyppeteer` 的大致操作

### *2020-01-20*
[REALI]
- 对数据存储到 redis 中进行压缩研究, 使用 pickle 压缩数据比之前节约了近一倍的容量, 这样网络传输时间更少, 返回更快
- 对国资局爬虫的各项参数的调整和验证, 发现每个账号每天能查询 165 个专利, 并且不受时间限制
- 完成对多个网页同时提取的代码, 现在基本上一个请求可以在 2-3s 返回数据
- 有个问导致返回时不时为空, 进行调试后发现主要是等待时间不够 js 执行完成, 但是直接加长等待时间会使得每个请求等待时间都长, 降低了效率, 对此针对性优化的思考是: 重写提取数据的代码, 明天将会做这部分的工作
[LEARN]
- 学习 Hadoop 的概念和基本结构

### *2020-01-21*
[REALI]
- 对查询时间的优化, 通过一个申请号查询费用信息api基本可用, 每个请求第一次查询大约耗时2.5s, 之后有缓存, 返回时间缩短至30ms
- 整合代码到线上, 通过 http://39.105.72.96:9003/?sqh=201910648227X 这个网址可以查询专利号的费用, 发文, 状态等所有信息, 只需要更改专利号即可
[LEARN]
- 学习 Hadoop 的安装与一些流程

### *2020-02-03*
[REALI]
- 编写下载 excel 的代码
[LEARN]
- 学习 Hadoop 相关知识
[FIXED]
- 修复政务平台爬虫的错误

### *2020-02-04*
[REALI]
- 新增全量更新专利缴费数据的代码, 优化逻辑实现, 准备每个月都全量更新一次数据
- 对图片验证码处理方式的探讨
- 对下载 excel 代码的优化

### *2020-02-05*
[REALI]
- 与后端探讨实现图片验证码坐标的返回细节
- 对全自动下载 excel 的设计实现
- 对商标网商标查询的分析研究    
[LEARN]
- 学习 Hadoop 相关知识

### *2020-02-11*
[REALI]
- 调用中利汇接口给后端返回专利数据

### *2020-02-18*
[REALI]
- 返回通过企业名称查询相关专利的 api
[LEARN]
- 学习 Mysql 索引相关知识

### *2020-02-19*
[REALI]
- 合并多个 api 接口到一个网址
[LEARN]
- 学习 Mysql 索引相关知识, B+ 树, 联合索引优先顺序, 失效问题
- 对 `threading.Thread` 模块的学习和使用
[FIXED]
- 修复一个专利查询的逻辑问题, 使中利汇接口可以正常使用

### *2020-02-20*
[REALI]
- 基本完成商标网爬虫
- 完成此阶段的简历

### *2020-02-21*
[REALI]
- 重装系统, 啥都没做

### *2020-02-24*
[REALI]
- CentOs 上面安装 tesseract 验证码识别软件
- 对通过企业名称查询企业专利信息的爬虫的实现
[LEARN]
- `from urllib import parse`, 用这个方法合并 url 可以保证 url 的正确性
- 

### *2020-02-25*
[FIXED]
- 对数据库中英文括号问题的解决, `UPDATE `t_ip_info` SET proposer=REPLACE(proposer,'（','(');`
- 对发文信息证书图片爬取可行性的研究

### *2020-02-26*
[REALI]
- 修复政务平台爬虫的错误, 新增邮件提醒功能
[LEARN]
- 对日志文件的编码方式做了更改 `handler = logging.FileHandler(filename=f, encoding='utf8')`
- Linux kill 多个进程 `ps -aux | grep ep_info/crawl.py | awk '{print $2}' | xargs kill`

ps -aux | grep jjs | awk '{print $2}' | xargs kill

### *2020-03-02*
[REALI]
- 添加`中新天津生态城管理委员会`到政务平台
- 基本完成发文通知书的下载测试, 对 `retry` 的使用使程序更加简洁高效
- 更新 11622 账户的专利数据到数据库
[FIXED]
- 修复一个政务平台的索引错误

### *2020-03-03*
[REALI]
- 服务器重启之后的各个项目的启动与总结
- 整理最近好几个项目的代码
[LEARN]
- redis 的启动与停止
- selenium "--disable-gpu" 参数可以提高性能
- 京东爬虫通过 js 返回 json 文件

### *2020-03-04*
[REALI]
- 与后端沟通下载发文通知书到 fastdfs
- 通过 python 实现文件上传到 fastdfs
[LEARN]
- 爬虫 Ip 代理的使用
- selenium 登录B站的图片截取与坐标识别

### *2020-03-05*
[REALI]
- 重构专利查询的代码, 优化逻辑与查询时间
- 对每个专利号费用查询设置过期时间
- 对万象云的接口重新优化逻辑
[LEARN]
- JS 的 $ 四种方法
  - 选择器
  - 添加元素
  - window.onload
  - DOM 转换为 jQuery 对象
[FIXED]
- 修复费用信息有时候查询为空的BUG

### *2020-03-06*
[REALI]
- 使用 redis 不同的数据库来做缓存, 而不是只使用 DB0, 这样有利于区别哪个程序有什么问题
- 修改关于 redis 数据库的代码结构, 对必要的地方都加以更详细的注释, 扩展了不同功能的代码使用不同的数据库的能力
- 编写下载通知书与 fastdfs 的逻辑, 设计动态可变的代码结构, 以后只要数据库里面更改即可, 不需要更改代码
- 对通过企业名称统计企业的商标信息爬虫做规划, 下周开始正式开始该项目
[LEARN]
- 进一步了解 scrapy 的代码结构和运行逻辑
- 对通过代理的 app 爬虫做了解

### *2020-03-09*
[REALI]
- 下载通知书到 Fastdfs, 修复一些问题
- 研究通过企业名称查询商标的爬虫, 但是 IP 封的很频繁, 或许要考虑其他方法了
- 对接口返回状态的重新完成与后端对接
[LEARN]
- Appium 和 Xposed 爬取抖音信息爬虫的了解
- 对 Kafka 官方文档的阅读和了解

### *2020-03-10*
[REALI]
- 对新加入 32407 的账户入库并检验, 更改更新专利缴费数据为多进程 + 多线程模式, 更新总耗时从之前的大概十分钟减少至一分钟左右(网速够快的情况下)
- 修改专利查询接口关于 status 字段与后端逻辑冲突的问题
- 对商标爬虫进行测试, 发现封 IP 很频繁, 即使是人手动操作, 也在查询几次之后被封 IP(这就有点不懂了), 每次被封时间是半小时-两小时不等
- 通过阿布云付费代理测试, 发现即使是换了动态 IP, 返回也是会检测出侦测行为, 总之依旧是无效, 目前暂时没想到解决方案
[LEARN]
- Tomcat 的 bin, conf, lib, webapps等目录结构的了解, 对 Tomcat 的了解更加清晰
- 对使用 Docker, Appium 部署多个手机端的爬虫项目的了解
- 对 Java Servlet 的学习
[FIXED]
- 修复另一个 BUG(网页返回不完全), 曾导致专利接口的费用信息返回为空
- 发现一个 BUG, 导致在请求一段时间后返回的页面为同一个, 准备明天多测试并修复

### *2020-03-11*
[REALI]
- 寻找并排查服务器的 CPU 占用过高的问题, 暂时修复 linux 的 jjs 病毒错误, 但是还没找到源代码, 目前已正常, 但是仍然有可能复发
- 与张超沟通商标爬虫目前暂时爬取不到的原因, 考虑第三方平台的数据, 但是因为第三方的都不准确, 所以还在等张超回复
- 连续爬取上千个专利号调试费用信息接口爬虫的稳定性, 找到多出隐藏的小问题, 目前还有一个问题没有修复, 全部修复后, 再修改用户随机访问逻辑, 目标是做到不需要关闭的本地浏览器爬虫, 但是模拟浏览器请求确实稳定性很差, 很多小问题不断, 而且不一定会复发, 所以还需要进一步优化和调试
[LEARN]
- 对 Java Hashmap 的学习了解, Map<String, String> map = new HashMap<String, String>();
- 对 Linux `xargs`, `find`, `crontab`, `ps`, `top` 命令的进一步使用和了解
[FIXED]
- 专利爬虫图片返回今日爬取量已失效的 BUG
 
### *2020-03-12*
[REALI]
- 整理代码结构
[LEARN]
- 进一步了解 python *args 的传参方式
[FIXED]
- 修复专利查询数据重复的 BUG

### *2020-03-13*
[REALI]
- 使用服务器在国资局登录成功, 之前不行是因为加载时间有点久导致报错

### *2020-03-15*
[LEARN]
- 实现 Hadoop 的安装启动运行, 并配置端口给外部访问
- 第一次安装和使用 Gradle 和 Maven, Gradle Build 速度非常的慢, 我怀疑是我设置的问题
- 明白 @Override 是为了修饰实现 interface 中的方法
- `firewall` 端口的开放 `firewall-cmd --zone=public --add-port=50070/tcp --permanent`, `firewall-cmd --reload`
- 查看开放的网络端口 `netstat -tpnl`

### *2020-03-16*
[REALI]
- 服务器上登录国资局的验证码部分代码重写
- 服务器上成功登录国资局
[LEARN]
- 添加多个远程 Git 库并同时更新, 对 Git 操作的更加深入的认识
- Yarn 架构和 Map-Reduce 的认识, 以及如何提交 Task 到 Hadoop 的分布式计算
  
### *2020-03-17*
[REALI]
- 公司电脑上实现自动化的 Excel 下载以及数据更新
- 在服务器实现专利 API 代码的运行
- 对公众用户登录的功能开发, 部分代码重构优化逻辑, 以后就可以不使用机构账号了
[LEARN]
- Github 的大文件上传 `git lfs track "xx.zip"`
- 明白 git reset --soft|--hard|--mixed 的区别
- 学习 Github tag, stash 命令
- 第一次新建分支操作
- 第一次尝试 `assert` 配合 `retry` 的使用
- 使用 `tail -f 2020_03_17.log` 动态查看文本文件 `-f == --follow`
- 使用 `find ./ -name "*.xls" -print | wc -l`

### *2020-03-18*
[REALI]
- 成功通过服务器下载和更新专利数据
- 完成专利查询接口需要添加标记的逻辑
- 完成专利法律状态接口解析
- 完成公众登录专利查询接口
- 增加自动下载 Excel 的代码的稳定性和合理性
[LEARN]
- xpath `//tbody/tr[position()<last()]/td[1]`, `tr[position()=1 or position()=2]`
- Git 关联远程仓库并同时 push
- 设置并备份 git config --global alias.xx "xx"
- 进一步熟悉 Git 操作

### *2020-03-19*
[REALI]
- 返回后端法律状态查询的接口
- 完成对专利费用接口添加标记
- 修改 Redis 插入和删除专利号逻辑
- 部署更新数据爬虫到服务器定时任务中
- 完成 twitter 爬虫的数据获取功能, 不会这么简单吧? 前几天还乱码, 今天就好了, 就很奇怪
[LEARN]
- Scrapy 插入自定义 headers
- Scrapy 插入自定义 proxies
- Scrapy 插入自定义 get params
- .gitignore 不起作用: git rm -rf xxx, 然后再添加到 .gitignore 里面
- 了解 spark, scala, flink 等大数据框架

### *2020-03-20*
[REALI]
- 中利汇加密算法失效也会重新请求并返回
- 完成中利汇重新更新 js 代码
- 对 redis 连接错误的重试
- 添加 fdfs_client 到公司, 并备份安装包
- 发现万象云同时多人登录出现挤掉的情况, 应该考虑 cookie 通过 redis 保存, 然后共同调用
[LEARN]
- a 调用 b, b import c, 得出结论: a 每次调用 b 的时候 import c 的结果不会变, 在 c 中定义的全局变量只会执行一次
- Linux Htop 的使用, 进程的父进程的查看
- 对 Flask 的 render_template 的简单使用
- Flask 在 js 文件改变之后, 不管是不是 DEBUG 模式, 都会加载新的 js 文件
- 对 gist 的了解
- 找到新插件 CodeSnap
- 找到永久设置 windows 环境变量的方法, 以后不用打开图形界面设置了
[FIXED]
- 修复服务器 CPU 占用率过高的问题, 原来是中利汇加密算法失效导致 js 测试无限重试

### *2020-03-21*
[REALI]
- 通过 [RePKG.exe](https://github.com/notscuffed/repkg) 完成 wallpaper engine 图片提取的功能

### *2020-03-22*
[LEARN]
- 学习了解一些 python 内置库的大致功能和用法

### *2020-03-23*
[REALI]
- 基本实现 `CookiePoolRedis`, 并支持多个网站的复用, 目前还存在有时候 redis 连接报错的问题, 尚不清楚是什么原因
- 对每日自动更新数据任务不执行问题的排查, 重启试验
- 对招标平台的政务爬虫做分析, 发现每个平台都返回当天上千条的数据, 考虑会不会多个平台重复, 并在验证
[LEARN]
- Scrapy 的结构的熟悉, Shell 的编写, 基本语法的熟悉

### *2020-03-24*
[REALI]
- 对服务器自动下载更新 Excel 失效问题的排查, 对之前不返回无限重试的程序添加重试次数限制
- 调整 settings_patent 文件中的目录结构, 优化代码逻辑
- 对 BigData 的启动错误排查, 发现全局 ~/.zshrc -> DJANGO_SETTINGS_MODULE 设置会影响其他 Django 项目的启动
- 完成 cookies 池并经过测试稳定后部署到服务器上
- 攥写国资局注册文档, 然后配合张晗把新注册的号存入数据库中
[LEARN]
- In SQL, NULL is [unknown], 5 NOT IN (1, 2, NULL) != true, but is NULL, because SQL not know where NULL compare with 5

### *2020-03-25*
[REALI]
- Refactored sele/base.py to compatible with the situation of wrong gzj password
- Almost finished the online training courses crawler
- Detected account whose password need to be changed and leave it to LiYuanYuan
[LEARN]
- Python `hasattr()`, `delattr()`, `__setattr__()`, `setattr()`, `__getattribute__()` function

### *2020-03-26*
[REALI]
- Rebuild the log system of Patent by `loguru`, it can classified logs by `year/month/date.log`
- Finish '天津市政府采购网' Notice crawler
[LEARN]
- Read official document to learn the `loguru` module, and use it to Patent
- If need real-time variable in python, it should be calculate again
- Learn deeply about the dynamic language of python, it can change the value of variable when DEBUGGING

### *2020-03-30*
[REALI]
- Finish '天津市虹桥区人民政府' crawl
- 
[LEARN]
- retry: usage of `retry_error_callback` and `before_sleep`
- A glance of pyppeteer API, learn a little of the structure of pyppeteer