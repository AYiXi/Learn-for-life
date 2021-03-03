### 删除 apply_id, cost_type 字段相同的 id 小的信息

```sql
DELETE FROM t_ip_fee WHERE id IN (SELECT t.id FROM (SELECT id FROM t_ip_fee WHERE apply_id in('2017210778511', '2018213841691', '2018304723884', '2017210723453', '2017210725980', '2018213840538', '2018304733551', '2017210778460', '201830471993X',
'2018213846727') GROUP BY apply_id, cost_type HAVING count(*) >1) as t)

DELETE FROM ep_info
WHERE id IN
	(SELECT id FROM
		(SELECT
			id
		FROM
			ep_info
		WHERE
			`code` IN (SELECT `code` FROM ep_info GROUP BY `code` HAVING count(`code`)>1)
			AND id NOT IN (SELECT min(id) FROM ep_info GROUP BY `code` HAVING count(`code`)>1))
	AS f)
```

### 删除重复的最大的 apply_id

```sql
DELETE FROM t_ip_info WHERE id IN (SELECT t.id FROM (SELECT MAX(id) AS id FROM t_ip_info GROUP BY apply_id HAVING count(*) > 1) AS t)
```

### 找出相同年份标记 tag 的费用

```sql
SELECT
	is_paid,
	apply_id,
	cost_type,
	`money`,
	x_date,
	zhinajin_date,
	create_time,
	update_time,
	tag,
	is_monitor
FROM
	t_ip_fee
WHERE
	apply_id IN (
	SELECT
		apply_id
	FROM
		`t_ip_fee`
	WHERE
		tag = 1
		AND is_paid = 0
		AND is_monitor = 1
		AND cost_type LIKE '%年年费%'
	GROUP BY
		apply_id
	HAVING
		COUNT( * ) > 1
	)
ORDER BY
	apply_id,
	cost_type
```

### 更新同一专利号待缴费专利里有标记的年费信息其中比较小的年份的 is_paid=1 (重复 tag 年费表示国资局是已缴费状态)

```sql
UPDATE t_ip_fee
SET is_paid = 1
WHERE
	id IN (
	SELECT
		id
	FROM
		(
		SELECT
			id,
			apply_id,
			min( x_date ),
			cost_type
		FROM
			(
			SELECT
				id,
				is_paid,
				apply_id,
				cost_type,
				money,
				x_date,
				zhinajin_date,
				create_time,
				update_time,
				tag,
				is_monitor
			FROM
				t_ip_fee
			WHERE
				apply_id IN (
				SELECT
					apply_id
				FROM
					`t_ip_fee`
				WHERE
					tag = 1
					AND is_paid = 0
					AND is_monitor = 1
					AND cost_type LIKE '%年年费%'
				GROUP BY
					apply_id
				HAVING
					COUNT( * ) > 1
				)
			ORDER BY
				apply_id,
				cost_type
			) AS t
		GROUP BY
			apply_id
		) AS t2
	)
```

### 找出所有有效的有滞纳金的专利信息

```sql
SELECT
    info.apply_id,
    fee.cost_type,
    fee.money,
    fee.x_date,
    fee.zhinajin_date,
    info.proposer
FROM t_ip_fee as fee INNER JOIN t_ip_info as info ON fee.apply_id=info.apply_id
WHERE fee.cost_type LIKE '%滞纳金%' AND fee.is_paid=0 AND fee.is_monitor=1 AND info.is_del=0
ORDER BY fee.zhinajin_date DESC

SELECT
    info.apply_id as 专利号,
    fee.cost_type,
    fee.money,
    fee.x_date,
    fee.zhinajin_date,
    info.proposer,
    fee.create_time
FROM t_ip_fee as fee INNER JOIN t_ip_info as info ON fee.apply_id=info.apply_id
WHERE fee.cost_type NOT LIKE '%年年费%' AND fee.is_paid=0 AND fee.is_monitor=1 AND info.is_del=0 AND fee.x_date>'20191210' AND fee.x_date<'20191223'
ORDER BY fee.x_date
```

### 近几天未缴费的数据

```sql
SELECT
    info.apply_id as 专利号,
    fee.cost_type as 费用类型,
    fee.money as 费用,
    fee.x_date as 缴费日期,
    fee.zhinajin_date as 最终缴费日期,
    info.proposer as 申请人
FROM t_ip_fee as fee INNER JOIN t_ip_info as info ON fee.apply_id=info.apply_id
WHERE fee.is_paid=0 AND fee.is_monitor=1 AND info.is_del=0 AND fee.x_date BETWEEN (CURRENT_DATE - INTERVAL 3 DAY) AND (CURRENT_DATE + INTERVAL 7 DAY) ORDER BY fee.x_date;
```

### 创建表

```sql
CREATE TABLE `kfq_qys` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(200)	COMMENT '企业名称',
    `test` VARCHAR(45) COMMENT '测试无用',
    `ok` int(11) COMMENT '是否更新完成',
    `result_code` VARCHAR(45) COMMENT '测试无用',
    `total_count` int(11) COMMENT '专利数',
    PRIMARY KEY (`id`) USING BTREE
);
```

### 组成 300s 未响应的 kill 语句

```sql
SELECT
	concat( 'kill ', id, ';' )
FROM
	information_schema.PROCESSLIST
WHERE
	Command = 'Sleep'
	AND Time > 300
ORDER BY
	Time DESC;
```

### 通过正则表达式搜索到某些字段

```sql
SELECT
	*
FROM
	`zhengwu_crawl`
WHERE
	`name` REGEXP '招聘|地块|价格|道德模范|规划|电价|展位|消防|民心工程|报告|事故|安全|治理|隐患|竣工|同志|放假|街道|执法|免费|住房|环保招聘|地块|价格|道德模范|规划|电价|展位|消防|民心工程|报告|事故|安全|治理|隐患|竣工|同志|放假|街道|执法|免费|住房|环保';
```

### 发文状态与对应的通知书名称查询

```sql
SELECT
	info.apply_id,
	info.`name`,
	info.state,
	dis.tongzhismc,
	dis.create_date,
	info.update_time
FROM
	`t_ip_info` AS info
	INNER JOIN t_ip_dispatch_info AS dis ON info.apply_id = dis.apply_id
WHERE
	info.is_del = 0
	AND info.is_sell = 0
GROUP BY
	dis.apply_id
ORDER BY
	info.update_time DESC
```

### 替换括号

```sql
UPDATE `t_ip_info` SET proposer=REPLACE(proposer,'（','(');
UPDATE `t_ip_info` SET proposer=REPLACE(proposer,'）',')');
```

### TAG

```sql
SELECT id, apply_id, cost_type, x_date FROM t_ip_fee WHERE apply_id IN (SELECT apply_id FROM `t_ip_fee` WHERE is_paid=0 AND is_monitor=1 AND cost_type LIKE "%年年费%" GROUP BY apply_id HAVING COUNT(tag)>1) AND is_paid=0 AND tag=1 AND cost_type LIKE "%年年费%" ORDER BY apply_id, update_time DESC

UPDATE t_ip_fee SET tag=NULL WHERE id IN (SELECT id FROM (SELECT max(id) as id, apply_id, x_date FROM t_ip_fee WHERE apply_id IN (SELECT apply_id FROM `t_ip_fee` WHERE is_paid=0 AND is_monitor=1 AND cost_type LIKE "%年年费%" GROUP BY apply_id HAVING COUNT(tag)>1) AND is_paid=0 AND tag=1 AND cost_type LIKE "%年年费%"  GROUP BY apply_id ORDER BY apply_id DESC) as t)
```

### left join, right join, inner join 连接

```sql
-- A left join B: A 所有, B 中与 A 的交集
SELECT
	a.*,
	b.score
FROM student AS a
LEFT JOIN SC AS b
ON a.id=b.id
[WHERE b.score IS NOT NULL]
```

### 对索引操作, 先删除, 后增加新的索引

```sql
ALTER TABLE move_blink_user DROP INDEX idx_csdn_username;

CREATE UNIQUE INDEX idx_csdn_username ON move_blink_user (`csdn_username`) USING BTREE COMMENT 'csdn 的唯一索引';
```

### 查询 cods_names 里面有但 cods_company 里面没有的公司名称
```sql
select `name` from cods_names left join (select name as i from cods_company) as t1 ON cods_names.name=t1.i where t1.i is null
```