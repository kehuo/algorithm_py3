# -*- coding: utf-8 -*-

from typing import List
from partition import Hoare


def QuickSort(L: List[int], low: int, high: int) -> None:
    if low < high:
        index = Hoare(L, low, high)
        QuickSort(L, low, index - 1)
        QuickSort(L, index + 1, high)


if __name__ == "__main__":
    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("origin list:", L)
    QuickSort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [1, 2, 4, 7, 8, 9, 10, 12, 15]
    print("origin list:", L)
    QuickSort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [15, 12, 10, 9, 8, 7, 4, 2, 1]
    print("origin list:", L)
    QuickSort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    print("origin list:", L)
    QuickSort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)
