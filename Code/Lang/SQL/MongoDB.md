```sql
// 查询
db.back_play_user_ip_address.find({'region_name':null})
db.pc_bianli_kechengbiao.find({"ts_short": {$gte: "2020-05-06"}}).count()

db.test_li_2.find({
	$and: [
		{$or: [{price: 0.99}, {price: 1.99}]},
		{$or: [{sale: true}, {qty: {$lt: 20}}]}
	]
})

db.inventory.find({tags: ["blank"]})         // tags exactly equals to blank
db.inventory.find({tags: {$all: ["blank"]}}) // tags contains blank
db.inventory.find({tags: "blank"})           // tags contains blank
db.inventory.find( { dim_cm: { $gt: 25 } } ) // at least one element greater than 25
db.inventory.find( { dim_cm: { $gt: 22, $lt: 30 } } )   // contains
db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } )  // at least one element 
db.inventory.find( { "tags": { $size: 3 } } )  // array length

db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } ) // field order is valid
db.inventory.find( { 'instock.qty': 15, 'instock.warehouse': 'C' } )

db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )  // no need one doc
db.inventory.find({instock: {$elemMatch: {qty: 5, warehouse: "A"}}}) // must be one doc

// Delete
db.inventory.remove({}) == mysql.truncate

// 查询列表中包含
db.test_li.find(
    {
        'data': {
            $elemMatch: {'schoolId': '6', 'classCode': 'GD07VS34004'}
        }
    }
)

// 索引相关 [https://blog.51cto.com/chenql/2071267]
db.pc_bianli_kechengbiao.getIndexes()
db.pc_bianli_kechengbiao.createIndex({"ts_short":1})
db.pc_bianli_kechengbiao.totalIndexSize()

```
