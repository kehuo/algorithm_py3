# @File: 3.py
# @Author: Kevin Huo
# @Date: 2020/9/13

import  heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/contest/weekly-contest-206/problems/min-cost-to-connect-all-points/
        """
        n = len(points)
        # 注意, 这里 h[1] 的数据类型必须是元组tuple, 因为后面调用 set.add() 方法时，不允许add list类型，只允许add tuple/int/str等数据类型.
        h = [(0, tuple(points[0]))]
        visited = set()

        res = 0
        while h and len(visited) < n:
            cost, (x, y) = heapq.heappop(h)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += cost
            for i, j in points:
                if (i, j) not in visited:
                    curr_cost = abs(i - x) + abs(j - y)
                    heapq.heappush(h, (curr_cost, (i, j)))

        return res
