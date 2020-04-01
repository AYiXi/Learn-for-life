array = [1, 8, 15]
g = [x for x in array if array.count(x) == 1]
array = [2, 8, 22]

c = list(g)
print(c)

g = (x for x in [2, 8, 22] if [1, 8, 15].count(x) == 1)
print(list(g))

# 迭代器在迭代的时候
# 传入的 x 是取最新的
# 但是, if 判断的时候, 是取的代码定义时的
# 所以答案时诡异的8
