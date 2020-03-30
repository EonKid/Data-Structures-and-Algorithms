"""

Time complexity: O(max(x, y)) --> O(n)
Space complexity: O(n)
"""

class Solution:

    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)

sol = Solution()
print("Enter a: ")
a = int(input())
print("Enter b: ")
b = int(input())
print("GCD: ",sol.gcd(a,b))