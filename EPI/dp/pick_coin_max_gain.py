"""
Two players take turns at choosing one coin each—they can only choose from the two coins at the ends of the line.
 The game ends when all the coins have been picked up. The player whose coins have the higher total value wins.
  A player cannot pass his turn.

Design an efficient algorithm for computing the maximum total value for the starting
player in the pick-up-coins game.

Explanation:
https://youtu.be/h7WI98qKkN0

"""


class Solution:

    dp = {}

    def pick_up_coin_for_max_gain(self, l, r, coins):
        """
        Time complexity: O(n*n)
        Space complexity: O(n)

        :param l:
        :type l:
        :param r:
        :type r:
        :param coins:
        :type coins:
        :return:
        :rtype:
        """
        if l > r:
            return 0
        if (l, r) in self.dp:
            return self.dp[l,r]
        a = coins[l] + min(
            self.pick_up_coin_for_max_gain(l+2, r, coins),
            self.pick_up_coin_for_max_gain(l+1, r - 1, coins)
        )

        b = coins[r] + min(
            self.pick_up_coin_for_max_gain(l, r - 2, coins),
            self.pick_up_coin_for_max_gain(l + 1, r - 1, coins)
        )

        profits = max(a, b)
        self.dp[l, r] = profits
        return self.dp[l, r]


coins = [20, 30, 2, 2, 2, 10]

sol = Solution()
print("PICK UP COINS FOR MAXIMUM GAIN, Profits: ", sol.pick_up_coin_for_max_gain(0, len(coins) - 1, coins))