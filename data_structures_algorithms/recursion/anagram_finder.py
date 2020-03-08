"""
Stored data: ['tca', 'cta', 'cat', 'tac', 'atc', 'act']

"""

L = ['tca', 'cta', 'cat', 'tac', 'atc', 'act']


def is_anagram(s: str, rest: str) -> bool:
    if rest == "":
        return s in L #base case
    else:
        for i in range(0, len(rest)):
            if is_anagram(s+rest[i], rest[0:i] + rest[i+1:]):
                return True
    return False


data = "tac"
print("Is anagram: ", is_anagram("",data))
