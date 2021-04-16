### Linux 下添加密码, 开放外网

```shell
# 安装
apt-get install mysql-server
apt-get install mysql-client

 
# 登录mysql    
mysql -u root -p 或 mysql

update user set authentication_string=PASSWORD("密码") where user='root';
update user set plugin="mysql_native_password";
flush privileges;
quit;
/etc/init.d/mysql restart;
mysql -u root -p 密码;

# let root login on any ip address
- grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
- flush privileges;

# 开放外网
1.https://blog.csdn.net/bird3014/article/details/78481104
2.在阿里云上面配置安全组
```

## [Shell 下免密码快速登陆 MySQL 数据库背景](https://imlonghao.com/7.html)
- vim ~/.my.cnf
- [client]   
  password=your_pass   
  user=your_user
- chmod 400 ~/.my.cnf
- export MYSQL_PWD=your_pass [或许不需要]

### 三范式

> 1. 字段不可分
> 2. 有主键, 非主键字段依赖主键
> 3. 非主键字段不能相互依赖

##### [解释](https://blog.csdn.net/WangQYoho/article/details/52900585)

> 1. 原子性: 字段不可再分, 否则就不是关系型数据库
> 2. 唯一性: 一个表只说明一个事物
> 3. 每列都与主键有直接关系, 不存在关系依赖



### [七种链接](https://blog.csdn.net/weixin_41963657/article/details/89644716)

>1. LEFT JOIN ON
>
>2. RIGHT JOIN ON
>
>3. INNER JOIN ON
>
>4. LEFT JOIN ON WHERE B.KEY IS NULL
>
>5. RIGHT JOIN ON WHERE A.KEY IS NULL
>
>6. RIGHT JOIN ON UNION LEFT JOIN ON (UNION:合并+去重, mysql 不支持 full) FULL OUTER JOIN
>
>7. RIGHT JOIN ON WHERE  A.KEY IS NULL UNION LEFT JOIN ON WHERE B.KEY IS NULL FULL OUTER JOIN ON WHERE A.KEY IS NULL ON B.KEY IS NULL



### 索引

##### 概述

> - 数据本身之外, 数据库还维护着一个满足特定查找算法的数据结构, 这些数据结构以某种方式指向数据, 可以实现一些高级的查找, 这就是索引
> - mysql索引算法: BTREE, 多路搜索树, 不一定是二叉, 有可能是三叉等, 唯一索引: B+树
> - 频繁删改的数据不适合建立索引, 索引本身也很大
> - 优势: 提高检索效率, 降低IO成本; 降低排序成本, 降低CPU消耗

##### 需要建立索引

> 1. 主键
> 2. 查询条件
> 3. 关联字段, 外键关系
> 4. 组合索引(高并发)
> 5. 分组的字段

##### 不要建立索引

> 1. 表记录太少
> 2. 经常增删改的表
> 3. 数据重复且平均的字段

##### [NULL](https://blog.csdn.net/lnotime/article/details/104847946)
- NULL is unknown
- `is null` is faster than `= null`
- 5 not in (1,2,3,null) -> null (not true)

##### Mysql 执行顺序
- ![Mysql 执行顺序](images/sql%20执行顺序.jpg)

### [时间函数](https://www.bilibili.com/video/BV1Qz4y1X7ZE)
```sql
-- 日期获取
NOW(); -- 执行一开始就获取时间
- 2020-11-15 18:19:50

select now(3)  -- 3 位毫秒, 后面是 000
- 2020-11-15 18:23:02.720000

select now(), sleep(3), now(); -- 两次时间一样
- 2020-11-15 18:20:05 0 2020-11-15 18:20:05

SYSDATE() -- 执行动态获取
- 2020-11-15 18:20:54
select sysdate(), sleep(3), sysdate(); -- 两次时间不一样
- 2020-11-15 18:20:54 0 2020-11-15 18:20:57

current_date() == curdate()
- 2020-11-15

current_time() == curtime()
- 18:20:54

-- 日期格式化
str_to_date('2020/01/02', '%Y/%m/%d')
- 2020-01-02

date_format(curdate(), '%Y.%m.%d')
- 2020.11.15

select year(now())
- 2020

select extract(year_month from now())
- 2020

-- 日期计算
date_sub(now(), interval 1 day)
date_add(now(), interval 2 day)
date_add(now(), interval '01:20:30' hour_second)
datediff('2020-08-08', '2020-09-09')
- 32
timediff('2020-08-08 01:00:00', '2020-09-09 02:00:00')
- -33 days, 23:00:00
timestampdiff(unit, begin, end)
timestampdiff(year, '2020-01-01', '2018-02-03')
- -1

-- 练习
1. 获取年龄
select year(now()) - year(birth) as age
2. 获取年龄, 根据出生日期, 不足一年不算
select timestampdiff(year, birth, curdate())
select *, case 
    when substr(birth, 6, 5) < substr(now(), 6, 5) then year(now()) - year(birth) 
    when substr(birth, 6, 5) > substr(now(), 6, 5) then year(now()) - year(birth) -1
3. 获取本周过生日的
select *, week(bitrh) as week, 
          yearweek(birth) as yweek,
          extract(week from birth) as eweek,
          extract(week from now()) as nweek
      from student
      where extract(week from birth) = extract(week from now())
```

### 表操作
```sql
-- 更改字段
ALTER TABLE company_xzcf_merge MODIFY COLUMN `source_url` VARCHAR(500) DEFAULT NULL COMMENT '来源url'

-- 添加字段
ALTER TABLE cods_company ADD before_name VARCHAR(255) DEFAULT NULL COMMENT "曾用名"

-- 添加索引
ALTER TABLE `table_name` ADD INDEX (`column`)
```