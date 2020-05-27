salary = 80

if salary <= 500:
    print('史塔克')
    if salary <= 100:
        print('美元队长')
    else:
        print('弗瑞队长')
elif 500 < salary <= 1000:
    print('温饱')
elif salary > 1000:
    print('经济危机难不倒')
    if salary <= 20000:
        print('钢铁侠')
    else:
        print('瓦坎达')
print('程序结束')