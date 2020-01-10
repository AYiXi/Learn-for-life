# 如果 key 存在, 则 value 不变
a = {}
a.setdefault('a', 1)
a.setdefault('a', 2)
print(a)

# dict.copy() 不影响 [].copy(), 等价于 copy(), 而不是 deepcopy()
a = {'a': 1}
b = a.copy()


# 以下均不会报错
def A():
    "comment"

class A:
    "comment"

    