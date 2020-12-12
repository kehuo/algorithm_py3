# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 12/6/2020 12:08 PM

from typing import List
import collections


class Solution:
    """https://leetcode-cn.com/contest/weekly-contest-218/problems/minimum-incompatibility/"""
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = collections.Counter(nums)
        n = len(nums)
        if n & k != 0:
            return -1
        if d.most_common(1)[0][1] > k:
            return -1
        # todo 暂时没有思路
        pass
