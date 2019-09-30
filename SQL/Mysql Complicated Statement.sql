1. 删除 apply_id, cost_type 字段相同的 id 小的信息
DELETE FROM t_ip_fee WHERE id IN (SELECT t.id FROM (SELECT id FROM t_ip_fee WHERE apply_id in('2017210778511', '2018213841691', '2018304723884', '2017210723453', '2017210725980', '2018213840538', '2018304733551', '2017210778460', '201830471993X', 
'2018213846727') GROUP BY apply_id, cost_type HAVING count(*) >1) as t)

2. 
DELETE FROM t_ip_info WHERE id IN (SELECT t.id FROM (SELECT MAX(id) AS id FROM t_ip_info GROUP BY apply_id HAVING count(*) > 1) AS t)

