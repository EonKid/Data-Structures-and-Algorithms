"""
17.10 COUNT THE NUMBER OF MOVES TO CLIMB STAIRS
You are climbing stairs. You can advance 1 to k steps at a time. Your destination is
exactly n steps up.
Write a program which takes as inputs n and k and returns the number of ways in which you can get to your destination. For example, if n = 4 and k = 2, there are five ways in which to get to the destination:
• four single stair advances,
• two single stair advances followed by a double stair advance,
• a single stair advance followed by a double stair advance followed by a single
stair advance,
• a double stair advance followed by two single stairs advances, and • two double stair advances.

"""


class Solution:

    memo = {}

    def count_number_moves_to_climb_stairs(self, n: int, k: int):
        """
        Time complexity: O(k*n)
        Space complexity: O(n)
        :param n:
        :type n:
        :param k:
        :type k:
        :return:
        :rtype:
        """
        if n <= 1:
            return 1
        if n not in self.memo:
            self.memo[n] = 0
            for step in range(1, k + 1):
                if n - step >= 0:
                    self.memo[n] += self.count_number_moves_to_climb_stairs(n - step, k)
        return self.memo[n]


sol = Solution()
print("COUNT THE NUMBER OF MOVES TO CLIMB STAIRS: ", sol.count_number_moves_to_climb_stairs(4, 2))

