## Apis (接口)

- api_9005.py (对于9005端口的接口, 之后需要转移到9003端口)
    - `wxy_enterprise_info`: 通过企业名称查询专利信息
- api.py (主要的接口数据, 端口使用9003)
    - `patent_info_query`: 通过申请号查询费用信息
    - `law_status`: 查询法律状态
    - `wxy_enterprise_info`: 通过企业名称在万象云该企业拥有的专利数量
    - `wxy_sqh_info`: 通过申请号在万象云查询该专利的一些基本信息(不包括费用信息)
    - `trademark_query`: 通过商标号查询商标信息, 目前已搁置, 因为商标网总是封 IP

## Captcha (所有与验证码相关的代码)

- `captcha_images`: 验证码图片暂存目录
    - `merged_images`: 合并之后的验证码图片存放地址, 纯代码登录过自己的时候使用, 现在基本废弃
    - `num_captcha`: 保存数字验证码的目录, 基本也没用了
    - `word_captcha`: 保存临时的图片验证码
- `captcha_http.py`: 通过 http 的方式向打码平台获取验证码(windows + linux)
- `captcha_recognize.py`: 通过 dll 文件的方式向打码平台获取验证码(只适用于 windows )
- `captcha_tools.py`: 验证码工具, 截图, 裁切图, 模拟点击等一系列国资局验证码流程
- `dcb64.dll`: windows 端验证码处理程序
- `merge_captcha_image.py`: 合并图片验证码的图片与文字, 之前纯代码访问国资局时候用到, 现在基本已经无用
- ` white_board.png`: 白色纯底图片, 之前纯代码访问国资局时候用到, 现在基本已经无用

## Crawler (爬虫相关)

- `ep_information`: 通过企业名称查询企业一些信息的爬虫, 一次性项目, 以后可能用到
- `patent_crawler`: 国资局专利相关爬虫
    - `base.py`: 模拟浏览器的登录的基类
    - `purecode`: 纯代码访问国资局, 之前一直用这个, 后来国资局更改反爬虫方式之后就没用了
    - `sele`: 通过 selenium 模拟浏览器爬取国资局信息
        - `download_excel.py`: 每日下载 Excel
        - `download_review.py`: 更新审查信息
        - `patent_query.py`: 通过专利号查询专利费用信息的模拟浏览器爬虫接口
    - `zlhui_crawler`: 中利汇网站的费用信息接口爬虫, 通过专利号查询专利费用信息的接口
    - `query_api.py`: 查询专利的逻辑代码
- `trademark_crawler`: 商标爬虫相关, 暂时没有使用了
- `wxy_crawler`: 万象云网站有关爬虫
    - `xiqing`: 西青区项目, 更新各企业年度专利数据
    - `enterprise_query_info.py`: 通过企业名称查询专利信息
    - `wxy.py`: 万象云爬虫的基类
    - `wxy_params.py`: 万象云爬虫各个项目的参数信息
- `zhengwu_crawler`: 政务网站信息搜集页爬虫
    - `analyze_func.py`: 对于特定的需求, 自定义函数, 需要返回特定的内容
    - `crawl.py`: 爬取网站主逻辑
    - `sites.py`: 需要爬取的站点
    - `update.py`: 每日更新逻辑

## Files (所有文件的目录)

- `dfs_conf`: fastdfs 相关配置文件目录
- `html_others`: html 相关文件
- `js`: js 文件

## OpDatabase (操作数据库相关代码)

- `op_redis`: redis 相关类
- `shangwen`: 每日更新专利数据代码
- `mysql_base.py`: Mysql 操作相关代码
- `compare.py`: 比较两个数据库直接不同的数据量, 主要是 debug 使用
- `exclude_sqh.py`: 不需要更新的专利号
- `wan_xiang_yun.py`: 更新万象云查询到的企业数据到数据库
- `xiqing_patent_query.py`: 西青区判断专利号状态的代码, 目前很多设置改了, 以后可以使用

## Practice (做测试代码的文件夹)

## Utils (一些通用的工具代码)

- `check_sqh_utils.py`: 检查专利号是否合法
- `common_utils.py`: 通用的一些方法
- `cponline_api_utils.py`: 电子申请网工具类, 发文更新, 专利未费用查询
- `db_utils.py`: 数据库的一些方法
- `decorator_utils.py`: 装饰器方法
- `exception_utils.py`: 自定义错误
- `mail_utils.py`: 邮件方法
- `sele_utils.py`: selenium 工具方法

## `settings_patent.py` (通用设置)

## `task.py` (Linux 定时任务)