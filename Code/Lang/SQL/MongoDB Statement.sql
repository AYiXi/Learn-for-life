1. 查询列表中包含
db.test_li.find(
    {
        'data': {
            $elemMatch: {'schoolId': '6', 'classCode': 'GD07VS34004'}
        }
    }
)

2. 
