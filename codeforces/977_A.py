"""
Wrong Subtraction
https://codeforces.com/problemset/problem/977/A

"""
data = list(map(int, input().split()))
n = data[0]
k = data[1]

class Solution:

    def wrong_subtraction(self,number : int, k: int):
        for i in range(0, k):
            if number % 10 == 0:
                number //= 10
            else:
                number -= 1
        return number

sol = Solution()
print(sol.wrong_subtraction(n,k))

