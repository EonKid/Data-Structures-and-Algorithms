"""
Find closest in array



"""

def find_maximum_closest(A: [int], x: int):
    l = -1
    r = len(A)

    while r > l + 1:
        m = (l + r) // 2
        if A[m] <= x:
            l = m
        else:
            r = m
    return l

A = [3,5,10,11,13,18,25,27,31]
x = 12
print("Find maximum left which closest to x = ", x)
closest_index = find_maximum_closest(A, x)
print(A[closest_index])


