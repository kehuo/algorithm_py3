
# @File: 2.py
# @Author: Kevin Huo
# @Date: 2020/4/12

from typing import List


def processQueries(queries: List[int], m: int) -> List[int]:
    # arr.index(n) 是n在arr中的索引
    length = len(queries)
    P = list(range(1, m + 1))

    res = []
    for i in range(length):
        q = queries[i]

        q_idx = P.index(q)
        res.append(q_idx)
        p_left, p_mid, p_right = P[:q_idx], [P[q_idx]], P[q_idx + 1:]
        # 将其排列为 mid + left + right
        P = p_mid + p_left + p_right
    return res


if __name__ == '__main__':
    tests = [
        [[3,1,2,1], 5]
    ]
    t = tests[0]
    r = processQueries(*t)
