"""
Want to enumerate all rearrangements: • ABCD permutes to DCBA, CABD, etc.
https://see.stanford.edu/materials/icspacs106b/Lecture09.pdf
"""


def string_permutations_iterative(s: str):
    pList = []
    pList.append(s[0])
    for i in range(1, len(s)):
        j = len(pList) - 1
        while j >= 0:
            tempStr = pList.pop(j)
            for k in range(0, len(tempStr)+1):
                temp = tempStr[0:k] + s[i] + tempStr[k:]
                pList.append(temp)
            j -= 1
    #print(pList)


def string_permutations(current: str, remaining: str):
    if remaining == "":
        print(current)
    else:
        for i in range(0,len(remaining)):
            next_str = current + remaining[i]
            remaining_str = remaining[0:i] + remaining[i+1:]
            string_permutations(next_str, remaining_str)


data = "()()()"
string_permutations("", data)
string_permutations_iterative(data)