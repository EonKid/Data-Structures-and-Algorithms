
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = int(input())
query = []
for i in range(k):
    query.append(list(map(int, input().split())))
results = []


def bSearch_right(nums:[int], a: int):
    l = -1
    r = n
    while r > l + 1:
        m = l + (r - l) // 2
        if nums[m] < a:
            l = m
        else:
            r = m
    return r + 1


def bSearch_left(nums: [int], b: int):
    l = -1
    r = n
    while r > l + 1:
        m = l + (r-l) // 2
        if nums[m] <= b:
            l = m
        else:
            r = m
    return l + 1


for pair in query:
    a = pair[0]
    b = pair[1]
    l = bSearch_right(nums, a)
    r = bSearch_left(nums, b)
    print(r - l + 1)









