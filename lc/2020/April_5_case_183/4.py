from typing import List


def stoneGameIII(stoneValue: List[int]) -> str:
    """
    https://leetcode-cn.com/problems/stone-game-iii/
    提交leetcode已经通过 700ms 用时
    ============

    动态规划思路

    根据<算法导论>第15章, 动态规划有2种方式:
    1 自底向上的动态规划
    2 自顶向下, 但是带 "备忘"功能的 动态规划.

    传统的 "递归" 解法, 就是自顶向下. 但是递归方式不带备忘, 但是动态规划是 "带备忘的", 可以避免大量的重复计算.
    "关于自顶向下带备忘的动态规划", 详情可以参考该项目下 算法导论/第四部分/ 目录下第15章 section.py 的 memoized 函数.

    这个题就打算采用 "自顶向下的带备忘的动态规划"

    思路, 用 dp 数组, 记录 每个可选的子数组的最优解. 对于一个数组 stoneValue:
    假设 n 代表数组的长度, 即 n = len(stoneValue)
    所以, stoneValue[n-1] 就是 stoneValue 数组的最后一项, 即 stoneValue[-1]
    1. (动态规划的基准情况) 如果子数组只有 stoneValue 的最后一项, 那么你只能选它, 所以 dp[n-1] = stoneValue[-1]

    2. 对于其他的 i:
    在写出递推公式之前, 我先定义 d[i] 代表 "从 stoneValue 数组的第 i 项 到最后一项 的子数组中, 的最优解."

    所以, 当 i = n-1 时, dp[i] = dp[n-1] = stoneValue[-1]
    当 0 <= i < n-1 时, dp[i] = sum{i, n} - min{dp[i + 1], dp[i + 2], dp[i + 3]}
    本题的目标 -- 判断 dp[0] 和 (sum(stoneValue) - dp[0]) 的大小. (因为题目说明Alice 必须先拿, 所以 dp[0] = Alice)
    """
    n = len(stoneValue)

    # n + 3的原因, 是避免 dp[i+1], dp[i+2] 和 dp[i+3] 的 IndexError
    dp = [0] * (n + 3)
    current_sum = 0
    for i in range(n-1, -1, -1):
        current_sum += stoneValue[i]
        dp[i] = current_sum - min(dp[i + 1], dp[i + 2], dp[i + 3])

    # score_Alice = dp[0]
    # score_Bob = sum(stoneValue) - dp[0]
    score_Alice = dp[0]
    score_Bob = current_sum - dp[0]
    if score_Alice == score_Bob:
        return "Tie"
    elif score_Alice > score_Bob:
        return "Alice"
    elif score_Alice < score_Bob:
        return "Bob"


def stoneGameIII_v2(stoneValue: List[int]) -> str:
    n = len(stoneValue)
    # dp[i]:在stoneValue[i:]的情况下，我先拿，我能赢对方多少分
    dp = [-float('inf')] * n
    dp += [0] * 3
    for i in range(n-1, -1, -1):
        for j in [1, 2, 3]:
            dp[i] = max(dp[i], sum(stoneValue[i:i+j])-dp[i+j])
    if dp[0] > 0:
        return 'Alice'
    elif dp[0] < 0:
        return 'Bob'
    else:
        return 'Tie'


if __name__ == '__main__':
    # 2020/4/5 注释 - v2版本用动态规划
    # answer = ["Bob", "Tie", "Alice", "Tie"]
    tests = [
        [1, 2, 3, 7],
        [1, 2, 3, 6],
        [1, 2, 3, -1, -2, -3, 7],
        [-1, -2, -3]
    ]
    # dp数组:
    # [
    #   [6, 12, 10, 7],
    #   [6, 11, 9, 6]
    # ]
    t = tests[3]
    r = stoneGameIII(t)
