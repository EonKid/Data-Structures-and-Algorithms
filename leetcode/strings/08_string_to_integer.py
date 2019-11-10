#!/bin/python3
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str: str) -> int:
        result = 0
        is_negative_integer = False
        prev_char = None
        is_integer_found = False
        for c in str:
            if c == '-' and not is_integer_found:
                is_negative_integer = True
            if c == '.':
                break
            if (c == '-' and prev_char == '+') or c == '+' and prev_char == '-' or (c == '-' and prev_char == '-') or (c == '+' and prev_char == '+') :
                break
            ascii_c = ord(c)

            if 48 <= ascii_c <= 57:
                result = result * 10 + ascii_c - ord('0')
                is_integer_found = True
            elif is_integer_found and not 48 <= ascii_c <= 57:
                break
            elif 97 <= ascii_c <= 122 or (ascii_c == 32 and is_integer_found) or (prev_char == '-' and c == ' ') or (prev_char == '+' and c == ' '):
                break

            prev_char = c
        if is_negative_integer:
            result = -1 * result
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1

        return result


sol = Solution()
print(sol.myAtoi("4455dfgdfgdf"))

print(ord(' '))
