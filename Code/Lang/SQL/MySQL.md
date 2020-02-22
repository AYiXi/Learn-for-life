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

