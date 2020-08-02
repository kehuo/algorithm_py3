
# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 10:05 AM

from typing import List

class Solution:
    """
    https://leetcode-cn.com/contest/weekly-contest-200/problems/count-good-triplets/
    """
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        length = len(arr)
        for i in range(length - 2):
            n1 = arr[i]
            for j in range(i + 1, length - 1):
                n2 = arr[j]
                for k in range(j + 1, length):
                    n3 = arr[k]
                    # print(n1, n2, n3)
                    if (abs(n1 - n2) <= a) and (abs(n2 - n3) <= b) and (abs(n1 - n3) <= c):
                        res += 1
        return res
