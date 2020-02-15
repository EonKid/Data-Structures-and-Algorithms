# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    last_index = 0
    for i, next in enumerate(text):
        last_index = i + 1
        if next in "([{":
            opening_brackets_stack.append({"position":last_index, "char": next})
        if next in ")]}":
           if len(opening_brackets_stack) == 0:
               opening_brackets_stack.append({"position":last_index, "char": next})
               break
           if are_matching(opening_brackets_stack[-1]["char"], next):
               opening_brackets_stack.pop()
           else:
               opening_brackets_stack.append({"position": last_index, "char": next})
               break

    if len(opening_brackets_stack) == 0:
        return "Success"
    return opening_brackets_stack[-1]["position"]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
