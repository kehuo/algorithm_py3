# @File: 4.py
# @Author: Kevin Huo
# @Date: 2020/4/25
"""
https://leetcode-cn.com/contest/season/2020-spring/problems/qie-fen-shu-zu/
4. 切分数组
通过的用户数70
尝试过的用户数585
用户总通过次数70
用户总提交次数1878
题目难度Hard
给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。

示例 1：

输入：nums = [2,3,3,2,3,3]

输出：2

解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。

示例 2：

输入：nums = [2,3,5,7]

输出：4

解释：只有一种可行的切割：[2], [3], [5], [7]

限制：

1 <= nums.length <= 10^5
2 <= nums[i] <= 10^6
"""
from typing import List


def splitArray(self, nums: List[int]) -> int:
    dp = [len(nums) for _ in range(len(nums))]

    for i in range(len(dp)):
        dp[i] = dp[i - 1] + 1 if (i - 1 >= 0) else 1
        for j in range(i):
            if (self.gcd(max(nums[i], nums[j]), min(nums[i], nums[j])) > 1):
                dp[i] = min(dp[i], dp[j - 1] + 1 if (j - 1 >= 0) else 1)
    return dp[-1]


def gcd(num1, num2):
    """分解质因数"""
    while (num1 % num2 > 0):
        tmp = num2
        num2 = num1 % num2
        num1 = tmp
    return num2