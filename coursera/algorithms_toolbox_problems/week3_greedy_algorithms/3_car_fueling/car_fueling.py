# python3


def compute_min_refills(distance, tank, stops):
    current_refill = 0
    num_refill = 0
    stops.insert(0, 0)
    stops.append(distance)
    n = len(stops)

    while current_refill < n - 1:
        last_refill = current_refill
        while stops[current_refill + 1] - stops[last_refill] <= tank:
            current_refill += 1
            if current_refill == n - 1:
                break
        if current_refill == last_refill:
            return -1
        if current_refill < n - 1:
            num_refill += 1
    return num_refill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))
    # 10 3 4 1 2 5 9