import math

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(float(input()))

def is_good(x: float):
    s = 0
    for num in a:
        s += math.floor(num / x)
    return s >= k

def findMaxRopeLength():
    l = 0.0
    r = math.pow(10, 8) * 1.0
    for _ in range(100):
        m = (l + r) / 2
        if is_good(m):
            l = m
        else:
            r = m
    print(l)

findMaxRopeLength()

