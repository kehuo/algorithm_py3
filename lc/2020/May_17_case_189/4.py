# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/17/2020 12:47 AM

"""
https://leetcode-cn.com/contest/weekly-contest-189/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
"""

from typing import List
from itertools import combinations
from math import sqrt, atan2, sin, cos

# 这段小程序用来计算当 points 长度为 100 时, 如果我们按照 3 作为每一个情况的规模， 那么一共有多少个子问题
# 计算结果是 161700 种情况.
# a = combinations(range(100), 3)
# arr = []
# for i in a:
#     arr.append(i)
# print(len(arr))


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        """
        注意，这道题如果用 2点 + r 的方式固定一个圆，当points 长度为 100 时，一共有 100万种情况。
        这样都能通过 leetcode 提交
        所以我猜我的 3点固定一个圆的做法 也可以。（一共16 - 17 万种情况）

        以下是查看大神答案的地方
        https://leetcode-cn.com/contest/weekly-contest-189/ranking/

        该题虽然我暂未实现，但我的思路如下:
        1 根据数学原理，3个点可以唯一确定一个圆。
        2 所以，问题分2种情况考虑:
            2.1 points 长度 < 3
                # 1 若 points 只有1个点, 那直接返回1 即可。因为这个点肯定包含在半径为 r (r>0) 的一个圆中.
                # 2 若 points 只有2个点，也简单，计算2点之间距离(即直径)是否 <= 2*r.
                    >> 如果 <= 2*r 那么返回2 也就是说2个点都能落在靶上
                    >> 如果 > 2*r 那么返回 1 说明只有其中一个点能落在靶上
            2.2 points 长度 >= 3
                #1 若 ==3, 则有2个步骤:
                    #1.1 根据3个点，计算出这个圆，以及圆的半径。
                    #1.2 将上面步骤计算出的圆半径，和题目输入的 r 比较.
                        >> 若 计算出的圆半径 < r, 则返回3，说明3个点都能落在靶上
                        >> 若 计算出的圆半径 >= r, 则要两两求距离.
                            ## 若其中任意两点间的距离 <= 2*r, 则返回 2
                            ## 若 A-B / A-C / B-C 距离都 > 2*r, 那只能返回 1

                #2 最难的部分, 是 points 长度 > 3 时:
                #todo 比如有 A B C D 4个点, 需要求出:
                    A B C 3点计算出的圆中最多包含几个点 value1
                    A B D ... value2
                    A C D ... value3
                    B C D ... value4
                    一共4种圆，4种结果, 求 max(value1, value2, value3, value4)

                    所以，看起来像 "最优解问题"，可能要用到动态规划.
                    但是，有个大问题，就是 "当points中给的点太多时，要考虑的情况呈指数级的速度增长, 比如：
                    当给定 4 个点时, 只需要考虑4种情况，但是
                    当给定 5 个点时，就需要考虑以下 10 种情况
                    ABC / ABD / ABE / ACD / ACE / ADE / BCD / BCE / BDE / CDE
                    通过 itertools.combinations 我们可以计算得出，当 points 达到最大长度 100 时, 一共有
                    161700 个子问题需要考虑.

                    所以，由于这个问题，导致可能无法用上面分析的动态规划解答。因为，当points太长时，子问题太多.
        """
        p_len = len(points)
        # 只有 1 个点的情况
        if p_len == 1:
            return 1
        # 2 个点的情况
        if p_len == 2:
            # 若 A = [-2, 0], B = [0, 2], 则2点间距离的平方 = (-2-0)^^2 + (0-2)^^2 = 4 + 4 = 8
            distance_square = (points[0][0] - points[1][0]) ** 2 + (points[0][1] + points[1][1]) ** 2
            return 2 if distance_square <= 4*r**2 else 1
        # todo p_len >= 3

    def numPoints_v2(self, p: List[List[int]], r: int) -> int:
        """
        放弃上面的方法，用 v2 可以通过

        双层循环循环两个点，已知两个点和半径，找到圆心画一个圆，然后再循环整个数组找到在圆里的

        所以一共3层循环
        """
        res = 1

        def dis(pi, pj):
            return sqrt((pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2)

        def center(pi, pj):
            mid = ((pi[0] + pj[0]) / 2, (pi[1] + pj[1]) / 2)

            angle = atan2(pi[0] - pj[0], pj[1] - pi[1])

            # print(pi, pj)
            d = sqrt(r ** 2 - dis(pi, mid) ** 2)

            return mid[0] + d * cos(angle), mid[1] + d * sin(angle)

        n = len(p)
        for i in range(n):
            for j in range(i + 1, n):
                if dis(p[i], p[j]) > r * 2:
                    continue

                c = center(p[i], p[j])
                cur = 0
                for k in range(n):
                    if dis(c, p[k]) <= r + 10 ** (-7):
                        cur += 1

                # print(cur)
                res = max(res, cur)
        return res


if __name__ == '__main__':
    tests = [
        [[[-2, 0], [0, 2]], 2]
    ]
    t = tests[0]

    runner = Solution()
    rr = runner.numPoints(*t)
    # print(rr)
