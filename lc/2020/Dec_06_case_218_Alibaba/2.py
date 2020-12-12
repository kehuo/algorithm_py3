# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 12/6/2020 12:09 PM

from typing import List
import collections


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        https://leetcode-cn.com/problems/max-number-of-k-sum-pairs/
        1 统计每个数字出现的次数, 记录在d中
        2 对于d中的每个x, 计算 x对应的 y =k-x
            如果d[x]和d[y]都存在且都>0, 那么res+= x和y出现次数的较小值, 结束循环
        """
        s = sum(nums)
        if s <= k:
            return 0
        d = collections.Counter(nums)
        res = 0
        for x in d:
            # x = 数字, d[x]是该数字出现的次数
            y = k - x
            if x == y:
                tmp = d[x] // 2
            else:
                tmp = min(d[x], d[y])
            # print("d=%s, x=%s, y=%s, res=%s" % (d, x, y, res))
            if tmp > 0:
                res += tmp
                d[x] -= tmp
                d[y] -= tmp
        return res


