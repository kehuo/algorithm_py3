# @File: m5
# @Author: Kevin Huo
# @LastUpdate: 3/27/2020 6:27 PM

from typing import List
from collections import Counter


def hasGroupsSizeX(deck: List[int]) -> bool:
    """
    每日一题 -- 卡牌分组
    https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
    # todo 没做出来, 以后补上
    """
    res = False
    c = Counter(deck)
    print(c)

    can = True
    for one in range(2, len(deck) // 2):
        for k in c:
            print("c[k]=%s" % c[k])
            if c[k] % one != 0:
                print("%s != %s, 停滞循环" % (c[k], one))
                can = False
                break
        if can is True:
            res = True
            print("有最大公约数%s" % one)
            break
    return res


if __name__ == '__main__':
    # [True, False, True]
    tests = [
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1, 1, 1, 2, 2, 2, 3, 3],
        [1, 1]
    ]

    t = tests[2]
    has = hasGroupsSizeX(t)
    print(has)
