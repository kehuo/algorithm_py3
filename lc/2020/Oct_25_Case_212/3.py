# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 10/25/2020 10:22 AM

from typing import  List


class Solution:
    """
    回溯法
    todo - 下面的dp 代码, 暂时不删, 以后补上正确解法
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_row = len(heights)
        len_col = len(heights[0])
        dp = [[float("inf") for _ in range(len_col)] for _ in range(len_row)]
        dp[0][0] = 0
        print(dp)

        # dp[i][j] 代表走到 heights[i][j] 时最小体力消耗的值. 它等于:
        # min(上面, 下面, 左面, 右面), 即:
        # 上 = dp[i-1][j]
        # 下 = dp[i+1][j]
        # 左 = dp[i][j-1]
        # 右 = dp[i][j+1]
        # dp[i][j] = min(dp[i-1][j], dp[i+1][j], dp[i][j-1], dp[i][j+1])
        i = 0
        j = 0
        while (i != len_row - 1) and (j != len_col - 1):
            # if i>0 可以检查上 / if i<len_row 可以检查下
            # if j>0 可以检查左 / if j<len_col 可以检查右
            pass

        return 1


if __name__ == '__main__':
    tests = [
        [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    ]
    t = tests[0]
    s = Solution()
    s.minimumEffortPath(t)
