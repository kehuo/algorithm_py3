# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-03-29 18:21:15
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-03-29 18:47:04

''' quick select, find the element on target index (from low to high)
'''

from typing import List
from Partition import Lomuto


def QuickSelect(L: List[int], target_index: int) -> int:
    assert 0 <= target_index < len(L)

    index = -1
    low = 0
    high = len(L) - 1

    while index != target_index:
        index = Lomuto(L, low, high)
        if index < target_index:
            low = index + 1
        elif index > target_index:
            high = index - 1
    return L[index]


if __name__ == "__main__":
    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("origin list:", L)
    k = len(L) // 2
    median = QuickSelect(L, k)
    print("after select the median, the list now is", L)
    print("the median of the list is {}, index is {}".format(median, k))
