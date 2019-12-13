# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    if n == 0: return 0
    numbers.sort()
    a = numbers[n-1]
    b = numbers[n-2]
    max_product = a * b
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
