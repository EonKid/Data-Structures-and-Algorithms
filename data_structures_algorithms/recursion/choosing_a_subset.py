"""
Given N things, how many different ways can you choose K of them?
• e.g. given a dorm of 60 people, how many different groups of 4 people can go together to Flicks?
• N-choose-K, written as C(n, k)
Number of subsets that include = C(n-1, k-1) + Number of subsets that don't include = C(n-1, k)


Simplest base case
• when no choices remain at all

"""


def choose_a_subset(n: int, k: int):
    if k == 0 or k == n:
        return 1
    return choose_a_subset(n-1, k) + choose_a_subset(n-1, k-1)


print("Choose 4 from 60:", choose_a_subset(60,4))