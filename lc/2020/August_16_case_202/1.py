# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 8/16/2020 1:07 PM

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        https://leetcode-cn.com/contest/weekly-contest-202/problems/three-consecutive-odds/
        提交已通过
        """
        res = False
        len_a = len(arr)
        if len_a <= 2:
            return res
        for i in range(len_a - 2):
            a, b, c = arr[i], arr[i + 1], arr[i + 2]
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                res = True
                break
        return res

