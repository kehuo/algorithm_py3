# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 10:05 AM

from collections import deque
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        https://leetcode-cn.com/contest/weekly-contest-200/problems/find-the-winner-of-an-array-game/
        d = {num: win_count}
        length = 7
        """
        q = deque(arr)
        res = -1
        d = {}
        length = len(arr) - 1
        while length > 0:
            left, right = q[0], q[1]
            if left not in d:
                d[left] = 0
            if right not in d:
                d[right] = 0
            if left > right:
                larger = q.popleft()
                smaller = q.popleft()
                q.appendleft(larger)
                q.append(smaller)
                d[left] += 1
                if d[left] >= k:
                    # res = a
                    break

            elif left < right:
                smaller = q.popleft()
                q.append(smaller)
                d[right] += 1
                if d[right] >= k:
                    break
            length -= 1
            # print("count: ", length, a, b, arr,  d)
        return max(d.keys())


if __name__ == '__main__':
    tests = [

    ]
    # t = tests[0]