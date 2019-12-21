# Uses python3
import sys


def take_ratio_sorted_key(element):
    return element[2]


def get_optimal_value(capacity, weights, values):
    value = 0.
    values_weights_ratio = []
    for i in range(len(weights)):
        w_i = weights[i]
        v_i = values[i]
        ratio = v_i / w_i
        data = (v_i, w_i, ratio)
        values_weights_ratio.append(data)
    values_weights_ratio.sort(reverse=True, key=take_ratio_sorted_key)
    for i in range(len(values_weights_ratio)):
        if capacity == 0:
            return value
        data = values_weights_ratio[i]
        v_i = data[0]
        w_i = data[1]
        ratio = (v_i / w_i)
        a = min(w_i, capacity)
        value = value + (a * ratio)
        w_i = w_i - a
        capacity = capacity - a
        data = (v_i, w_i, ratio)
        values_weights_ratio[i] = data

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
    # 3 50 60 20 100 50 120 30
