from typing import List
from algorithm.partition import hoare


def quick_sort(L: List[int], low: int, high: int) -> None:
    if low < high:
        index = hoare(L, low, high)
        quick_sort(L, low, index - 1)
        quick_sort(L, index + 1, high)


if __name__ == "__main__":
    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("origin list:", L)
    quick_sort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [1, 2, 4, 7, 8, 9, 10, 12, 15]
    print("origin list:", L)
    quick_sort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [15, 12, 10, 9, 8, 7, 4, 2, 1]
    print("origin list:", L)
    quick_sort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)

    L = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    print("origin list:", L)
    quick_sort(L, 0, len(L) - 1)
    print("after quick sort, the list is:", L)
