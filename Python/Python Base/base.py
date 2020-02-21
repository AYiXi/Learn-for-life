d1 = {'a': 1, 'b': 2}
d2 = {'a': 2, 'b': 3, 'c': 4}

d3 = {**d1, **d2}

def f(a, *, b, c):
    print(a, b, c)

f(1, b=2, c=3)

def f2(n, *names):
    print(*names)

f2(1,2,3)

print(d3)