"""
https://see.stanford.edu/materials/icspacs106b/Lecture08.pdf
Given N things, how many different ways can you choose K of them?
• e.g. given a dorm of 60 people, how many different groups of 4 people can go together to Flicks?
• N-choose-K, written as C(n, k)
Number of subsets that include = C(n-1, k-1) + Number of subsets that don't include = C(n-1, k)


Simplest base case
• when no choices remain at all

"""

def choose_a_subset_iterative(n, k):
    cache = [[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(n+1):
        cache[i][i] = 1
    result = []
    result.append([cache[0][0]])
    for i in range(1, n+1):
        data = []
        data.append(cache[i][0])
        for j in range(1, i+1):
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
            data.append(cache[i][j])
        result.append(data)
    print(result)
    return cache[n][k]



def choose_a_subset(n: int, k: int):
    if k == 0 or k == n:
        return 1
    return choose_a_subset(n-1, k) + choose_a_subset(n-1, k-1)


print("Choose 4 from 60:", choose_a_subset(5,5))
print("Choose 4 from 60:", choose_a_subset_iterative(5,4))