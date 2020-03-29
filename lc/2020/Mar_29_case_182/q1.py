# @File: q1
# @Author: Kevin Huo
# @LastUpdate: 3/29/2020 7:53 PM

from typing import List
from collections import Counter


def findLucky(arr: List[int]) -> int:
    """
    已经在leetcode 提交并通过

    找出数组中的幸运数
    https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/
    """
    c = Counter(arr)
    array = [i for i in c if c[i] == i]

    if len(array) == 0:
        return -1
    array.sort()

    return array[-1]


if __name__ == '__main__':
    tests = [
        [2, 2, 3, 4, 4, 4, 4],
        [1, 2, 2, 3, 3, 3],
        [2, 2, 2, 3, 3],
        [5],
        [7, 7, 7, 7, 7, 7, 7]
    ]
    t = tests[0]
    r = findLucky(t)
    print(r)
