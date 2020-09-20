# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 9/20/2020 10:25 AM


"""
https://leetcode-cn.com/contest/weekly-contest-207/problems/maximum-non-negative-product-in-a-matrix/
因为有负数 所以不能用动态规划

"""

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        lenRow = len(grid)
        lenCol = len(grid[0])
        dp = []
        for _ in range(lenRow):
            dp.append([1] * lenCol)
        dp[0][0] = grid[0][0]

        for i in range(lenRow):
            curr_row = dp[i]
            up_row = dp[i - 1] if i > 0 else []

            for j in range(lenCol):
                left_val = curr_row[j - 1] if j > 0 else None
                up_val = up_row[j] if up_row else None

                # calculate dp[i][j] based on dp[i-1][j] and dp[i][j-1]
                curr_grid = grid[i][j]
                if left_val is None:
                    # special - first col
                    dp[i][j] = curr_grid * up_val if up_val else dp[i][j]
                    continue

                if up_val is None:
                    # special - first row
                    dp[i][j] = curr_grid * left_val if left_val else dp[i][j]
                    continue

                dp[i][j] = max(curr_grid * left_val, curr_grid * up_val)

        return dp[lenRow - 1][lenCol - 1]