# s = input().split(',')
zhuzi = [1, 2, 3, 4, 5, 6, 7, 8]

length = len(zhuzi)
left, right = zhuzi[0], zhuzi[-1]

s0 = length * min(left, right)

for index, i in enumerate(zhuzi):
    s1 = (length - index) * abs(zhuzi[index + 1] - zhuzi[length - index])
    s2 = (length - index) * abs(zhuzi[index] - zhuzi[length - index])

    s = max(s0, s1, s2)
    if s == s0:
        pass
    elif s == s1:
        pass
    else:
        s = (right - left) * abs(left - right)
