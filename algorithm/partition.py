# -*- coding: utf-8 -*-

from typing import List


def Lomuto(L: List[int], low: int, high: int) -> int:
    assert low >= 0
    assert high < len(L)

    pivot = L[low]
    edge = low
    for i in range(low, high + 1):
        if L[i] < pivot:
            edge += 1
            L[edge], L[i] = L[i], L[edge]
    L[low], L[edge] = L[edge], L[low]
    return edge


def Hoare(L: List[int], low: int, high: int) -> int:
    """ pivot = L[low]
        i = low
        j = hight + 1
        repeat
            repeat i += 1 until L[i] >= pivot
            repeat j -= 1 until L[j] <= pivot
            swap(L[i],L[j])
        until i >= j
        swap(L[i],L[j])
        swap(L[low],L[j])
        return j
    """
    assert low >= 0
    assert high < len(L)

    pivot = L[low]
    i = low
    j = high + 1

    while True:
        while True:
            i += 1
            if L[i] >= pivot or i >= high:
                break
        while True:
            j -= 1
            if L[j] <= pivot:
                break
        L[i], L[j] = L[j], L[i]
        if i >= j:
            break

    L[i], L[j] = L[j], L[i]  # undo last swap
    L[low], L[j] = L[j], L[low]

    return j


if __name__ == "__main__":
    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("origin list:", L)
    index = Lomuto(L, 0, len(L) - 1)
    print("after Lomuto partition, element of index={} is located:".format(index), L)

    print("-" * 10)

    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("origin list:", L)
    index = Hoare(L, 0, len(L) - 1)
    print("after Hoare partition, element of index={} is located:".format(index), L)
