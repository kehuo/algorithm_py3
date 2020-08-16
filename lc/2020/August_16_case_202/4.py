# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 8/16/2020 1:07 PM


class Solution:
    """
    https://leetcode-cn.com/contest/weekly-contest-202/problems/minimum-number-of-days-to-eat-n-oranges/
    有空用动态规划实现 - 可以实现但是提交可能会超时
    """

    def minDays(self, n: int) -> int:
        pass


if __name__ == '__main__':
    tests = [10, 6, 1, 56, 2, 16, 99999999, 182]
    # 答案 = [4, 3, 1, 6, 2, 5, 33, 8]
    t = tests[6]
    s = Solution()
    r = s.minDays(t)

    print(r)
