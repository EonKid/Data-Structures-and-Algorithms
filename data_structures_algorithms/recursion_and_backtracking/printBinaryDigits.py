"""
Write a recursive function printAllBinary that accepts an integer number of digits and prints all binary numbers
that have exactly that many digits, in ascending order, one per line.

n = 2

Output: 00
        01
        10
        11
"""


def printAllBinary( digit: int):
    printAllBinaryHelper(digit, "")


def printAllBinaryHelper(digit: int, current_number: str):
    if digit == 0:
        print(current_number)
    else:
        printAllBinaryHelper(digit - 1, current_number + "0")
        printAllBinaryHelper(digit - 1, current_number + "1")

n = 2
print("Printing binary digits for n: ", n)
printAllBinary(n)


