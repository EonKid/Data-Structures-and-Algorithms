# Uses python3
import sys

def get_change(m):
    T = dict()
    T[0] = 0
    coins = [2, 4, 8]
    for m in range(1, m+1):
        T[m] = float('inf')
        for coin in coins:
            if m >= coin:
                T[m] = min(T[m], T[m-coin] + 1)
    return T[m]

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
