import math

w, h, n = map(int, input().split())


def is_good(x: int) -> int:
    return ( math.floor((x / w)) * math.floor((x / h))) >= n


def pack_rectangles():
    if w == 0 and h == 0:
        print(0)
        return
    l = 0 # bad
    r = 1 # good
    while not is_good(r):
        r *= 2
    while r > l + 1:
        m = (l + r) // 2
        if is_good(m):
            r = m
        else:
            l = m
    print(r)


pack_rectangles()



