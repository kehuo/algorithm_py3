# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 4/26/2020 7:20 PM

from collections import Counter


def maxScore(s: str) -> int:
    """
    今天周日值班, 没参加这次周日赛, 是下班后晚上自己掐时间做的
    leetcode  已通过
    https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/
    """
    res = 0
    len_s = len(s)
    for i in range(len_s - 1):
        left, right = Counter(s[:i + 1]), Counter(s[i + 1:])
        score = left["0"] + right["1"]
        if score > res:
            res = score
    return res


if __name__ == '__main__':
    # answer = [5, 3]
    tests = [
        "00111",
        "1111"
    ]
    t = tests[1]
    r = maxScore(t)
    print(r)


