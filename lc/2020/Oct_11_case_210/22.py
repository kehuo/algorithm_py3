# @File: 22
# @Author: Kevin Huo
# @LastUpdate: 10/11/2020 7:13 PM


from collections import defaultdict
from typing import List


class Solution(object):
    """
    通过提交
    https://leetcode-cn.com/contest/weekly-contest-210/problems/maximal-network-rank/
    """
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(set)
        for u, v in roads:
            d[u].add(v)
            d[v].add(u)

        if len(d) == 0:
            return 0
        order = [[k, d[k]] for k in d]
        order.sort(key=lambda x: len(x[1]), reverse=True)

        city1 = len(order[0][1])
        city2 = len(order[1][1])
        res = city1 + city2 - 1
        for i, a in enumerate(order):
            # 这个判断仅仅是对 i > 0 写的, 因为i=0时, 其实a=order[0], 就是自己比自己，肯定是相等，不会触发这个if判断
            if len(a[1]) < city1:
                return res
            # 以下的循环, 对所有order中的项写的，包括第一项. 因为如果第一项没有触发上面的if, 就要触发下面这个循环
            for j in range(i+1, len(order)):
                b = order[j]
                if len(b[1]) < city2:
                    break
                if b[0] not in a[1]:
                    return res + 1
        return res


if __name__ == '__main__':
    tests = [
        [5, [[2, 3], [0, 3], [0, 4], [4, 1]]]
    ]
    t = tests[0]

    s = Solution()
    s.maximalNetworkRank(*t)
