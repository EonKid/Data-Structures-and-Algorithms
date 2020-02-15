
# https://codeforces.com/problemset/problem/1145/A

n = int(input())
data = list(map(int, input().split()))

def thanos_sort(nums, n):
    if nums == sorted(nums):
        return n
    n = n // 2
    return max(thanos_sort(nums[:n], n), thanos_sort(nums[n:],n))

print(thanos_sort(data, n))