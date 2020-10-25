# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 10/25/2020 10:22 AM

from typing import List


class Solution:
    """
    Pass
    https://leetcode-cn.com/contest/weekly-contest-212/problems/arithmetic-subarrays/
    """
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        check = []
        for i in range(len(l)):
            curr = nums[l[i]:r[i]+1]
            curr.sort()
            is_dengcha = True
            idx = len(curr) - 1
            # print("i=%s, curr=%s" % (i, curr))
            if idx < 2:
                check.append(is_dengcha)
                continue
            while idx > 1:
                # print("loop, idx=%s" % idx)
                if curr[idx] - curr[idx-1] != curr[idx-1] - curr[idx-2]:
                    is_dengcha = False
                    break
                idx-=1
            check.append(is_dengcha)
        return check
