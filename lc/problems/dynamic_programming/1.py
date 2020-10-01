# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 10/1/2020 10:55 AM


class Solution:
    def is_yellow(self, j):
        return 1 if j == "y" else 0

    def is_red(self, j):
        return 1 if j == "r" else 0

    def minimumOperations(self, leaves: str) -> int:
        """
        已提交通过.
        https://leetcode-cn.com/problems/UlBDOe/

        answer:
        https://leetcode-cn.com/problems/UlBDOe/solution/qiu-xie-shou-cang-ji-by-leetcode-solution/

        dp 是一个 N x 3 的2维数组, 即:
        dp = [
            [a, b, c],
            [d, e, f],
            ...
        ]
        用 dp[i][j] 表示对于第 0 片到第 i 片叶子进行调整操作，并且第 i 片叶子处于状态 j 时的最小操作次数
        注意, j 的取值只能是 0 或 1 或 2.
        j=0 代表左边的红叶
        j=1 代表中间黄叶
        j=2 代表右边红叶
        """
        n = len(leaves)
        dp = []
        dp = [[n+1, n+1, n+1] for _ in range(n)]
        dp[0][0] = self.is_yellow(leaves[0])
        for i in range(1, n):
            now = leaves[i]
            dp[i][0] = dp[i-1][0] + self.is_yellow(now)
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + self.is_red(now)
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + self.is_yellow(now)

        print(dp)
        print(dp[n-1][2])
        return dp[n-1][2]


if __name__ == '__main__':
    # ans = [2, 0]
    tests = [
        "rrryyyrryyyrr",
        "ryr"
    ]
    t = tests[1]
    s = Solution()
    s.minimumOperations(t)

