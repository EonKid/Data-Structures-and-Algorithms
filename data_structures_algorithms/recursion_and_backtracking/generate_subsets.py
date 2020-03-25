"""
Enumerate all subsets of input • "abc" has subsets "a", "b", "ab", "ac", ...
• Order doesn't matter, "ab" is same as "ba"
https://see.stanford.edu/materials/icspacs106b/Lecture10.pdf
"""


def generate_all_subsets(s: str, rest_str: str):
    if rest_str == "":
        print(s)
    else:
        generate_all_subsets(s+rest_str[0], rest_str[1:])
        generate_all_subsets(s, rest_str[1:])


generate_all_subsets("", "123")