# Uses python3
import sys


def get_change(m):
    coins = [10, 5, 1]
    result = []
    for coin in coins:
        while m >= coin:
            m -= coin
            result.append(coin)
    return len(result)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
