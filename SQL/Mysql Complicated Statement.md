1. 删除 apply_id, cost_type 字段相同的 id 小的信息
```sql
DELETE FROM t_ip_fee WHERE id IN (SELECT t.id FROM (SELECT id FROM t_ip_fee WHERE apply_id in('2017210778511', '2018213841691', '2018304723884', '2017210723453', '2017210725980', '2018213840538', '2018304733551', '2017210778460', '201830471993X', 
'2018213846727') GROUP BY apply_id, cost_type HAVING count(*) >1) as t)
```

2. 
```sql
DELETE FROM t_ip_info WHERE id IN (SELECT t.id FROM (SELECT MAX(id) AS id FROM t_ip_info GROUP BY apply_id HAVING count(*) > 1) AS t)
```


3. 找出相同年份标记 tag 的费用
```sql
SELECT
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
```

4. 更新同一专利号代缴费专利里有标记的年费信息其中比较小的年份的 is_paid=1 (重复tag年费表示国资局是已缴费状态)
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

5. 找出所有有效的有滞纳金的专利信息
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

```sql
SELECT
    info.apply_id as 专利号,
    fee.cost_type as 费用类型,
    fee.money as 费用,
    fee.x_date as 缴费日期,
    fee.zhinajin_date as 最终缴费日期,
    info.proposer as 申请人
FROM t_ip_fee as fee INNER JOIN t_ip_info as info ON fee.apply_id=info.apply_id
WHERE fee.cost_type NOT LIKE '%年年费%' AND fee.is_paid=0 AND fee.is_monitor=1 AND info.is_del=0 AND fee.x_date>'20191210' AND fee.x_date<'20191223'
ORDER BY fee.x_date 
```