# @File: 1.py
# @Author: Kevin Huo
# @Date: 2020/4/25

from typing import List
from collections import Counter
import functools

"""
https://leetcode-cn.com/contest/season/2020-spring/problems/qi-wang-ge-shu-tong-ji/
1. 期望个数统计
通过的用户数980
尝试过的用户数1300
用户总通过次数1010
用户总提交次数2028
题目难度Easy
某互联网公司一年一度的春招开始了，一共有 n 名面试者入选。每名面试者都会提交一份简历，公司会根据提供的简历资料产生一个预估的能力值，数值越大代表越有可能通过面试。

小 A 和小 B 负责审核面试者，他们均有所有面试者的简历，并且将各自根据面试者能力值从大到小的顺序浏览。由于简历事先被打乱过，能力值相同的简历的出现顺序是从它们的全排列中等可能地取一个。现在给定 n 名面试者的能力值 scores，设 X 代表小 A 和小 B 的浏览顺序中出现在同一位置的简历数，求 X 的期望。

提示：离散的非负随机变量的期望计算公式为 1。在本题中，由于 X 的取值为 0 到 n 之间，期望计算公式可以是 2。

示例 1：

输入：scores = [1,2,3]

输出：3

解释：由于面试者能力值互不相同，小 A 和小 B 的浏览顺序一定是相同的。X的期望是 3 。

示例 2：

输入：scores = [1,1]

输出：1

解释：设两位面试者的编号为 0, 1。由于他们的能力值都是 1，小 A 和小 B 的浏览顺序都为从全排列 [[0,1],[1,0]] 中等可能地取一个。如果小 A 和小 B 的浏览顺序都是 [0,1] 或者 [1,0] ，那么出现在同一位置的简历数为 2 ，否则是 0 。所以 X 的期望是 (2+0+2+0) * 1/4 = 1

示例 3：

输入：scores = [1,1,2]

输出：2

限制：

1 <= scores.length <= 10^5
0 <= scores[i] <= 10^6
"""


def expectNumber(scores: List[int]) -> int:
    """
    d = {c中某项长度: {匹配长度: 一共几次}}
    d = {1: {1: 1},
         2: {0: 1, 1: 1},
         3: {0: 2, 1: 3, 2: 1}
    }
    """

    c = Counter(scores)
    d = {}

    son = 1
    total_raw = 1
    for one in c:
        tmp = 0
        total_raw *= (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(c[one])

        # 求某个固定甲
        # c[one] = 2, one=1
        if c[one] in d:
            curr = d[c[one]]
            for key, val in curr.items():
                # key=一共匹配了几个简历, 即X, val = 有多少次
                tmp += key * val

            son *= tmp
        # 计算后存入d
        else:
            pass

    son *= total_raw
    mother = total_raw * total_raw
    return son // mother


if __name__ == '__main__':
    tests = [
        [1, 1, 2, 2, 3]
    ]
    t = tests[0]
    r = expectNumber(t)
