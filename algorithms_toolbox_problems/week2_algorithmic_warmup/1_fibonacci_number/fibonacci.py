# Uses python3
def calc_fib(n):
    first = 0
    second = 1
    if n <= 1:
        return n
    for i in range(n-1):
        first, second = second, first+second
    return second

n = int(input())
print(calc_fib(n))
