# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 4/26/2020 7:20 PM

from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    """
    https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/

    todo 有时间在做 -- 这个题不能用以下思路做, 是错的.
    1 定义 dp 数组, 并定义dp中的每一项代表什么.
        1.1 首先定义 dp 的维度 --> 一维数组
        1.2 dp数组的长度 --> 等于k
        1.3 dp中每一项, 是一个长度为 3 的子数组 [left_idx, right_idx, current_score], dp[i]代表"第i+1次拿牌后获取最大分数时, 当前的左指针和右指针的位置", 如:
            cardPoints =  [1,2,3,4,5,6,1], k = 3, 那么:
            dp = [[None, 6, 1], [None, 5, 7], [None, 4, 12]]
            那么 dp[0] = [None, 6, 1] 代表: 第1次拿牌后, 左指针在None处(没指向任何值), 右指针直到最右边的1(代表这次拿了这张牌), 当前总分=1
        1.3 dp[k-1] 代表 "拿到第k张牌后, 能获得的最大分数"
        1.4 最终返回 dp[k-1]

    2 找到 dp 当前项和 前/后一项的关系:
        拿到第 i 张牌时的最大分数, 等于 "第i-1次从左边拿" 和 "第i-1次从右边拿" 的分数的较大者, 即:


    3 找到所有基准值(初始值比如 dp[0], dp[1] 这种)
    """
    len_cardPoints = len(cardPoints)
    dp = [[-1, len_cardPoints, -1]] * k
    print(dp)

    for i in range(k):
        pass

    return dp[-1][2]


if __name__ == '__main__':
    tests = [
        {"cardPoints": [1, 2, 3, 4, 5, 6, 1], "k": 3}
    ]
    t = tests[0]
    r = maxScore(**t)

