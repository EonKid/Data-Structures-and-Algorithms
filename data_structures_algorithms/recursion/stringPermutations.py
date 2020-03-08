"""
Want to enumerate all rearrangements: • ABCD permutes to DCBA, CABD, etc.
https://see.stanford.edu/materials/icspacs106b/Lecture09.pdf
"""


def string_permutations(current: str, remaining: str):
    if remaining == "":
        print(current)
    else:
        for i in range(0,len(remaining)):
            next_str = current + remaining[i]
            remaining_str = remaining[0:i] + remaining[i+1:]
            string_permutations(next_str, remaining_str)


data = "ABCD"
string_permutations("", data)