
# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 10/25/2020 10:22 AM

from typing import List


class Solution:
    """
    Pass
    https://leetcode-cn.com/contest/weekly-contest-212/problems/slowest-key/
    """
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = dict()
        for i in range(0, len(keysPressed)):
            k = keysPressed[i]
            if i == 0:
                d[k] = releaseTimes[i]
                continue
            if k not in d:
                d[k] = releaseTimes[i] - releaseTimes[i - 1]
                continue
            d[k] = max(d[k], releaseTimes[i] - releaseTimes[i - 1])
        arr = list([i, d[i]] for i in d)
        max_val = max([i[1] for i in arr])

        arr.sort(key=lambda x: x[1], reverse=True)
        # print(max_val, arr)
        char = arr[0][0]
        for i in arr:
            if i[1] == max_val and ord(i[0]) > ord(char):
                char = i[0]
        return char
