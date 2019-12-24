# Uses python3
import sys

def get_majority_element(a, left, right):
    a.sort()
    prev = a[0]
    n = len(a)
    current_count = 1
    for i in range(1, n):
        if prev == a[i]:
            current_count += 1
            if current_count > n // 2:
                return 1
        else:
            current_count = 1
        prev = a[i]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
