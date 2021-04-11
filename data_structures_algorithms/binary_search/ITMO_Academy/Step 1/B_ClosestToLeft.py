

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    for q in queries:
        l = -1
        r = n
        while r > l + 1:
            m = (l + r) // 2
            if nums[m] <= q:
                l = m
            else:
                r = m
        if l == -1:
            print("0")
        else:
            print(l + 1)



if __name__ == "__main__":
    main()