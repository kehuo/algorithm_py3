from typing import List
from math import ceil


def binary_search(A: List[int], K: int) -> int:
    """ binary search
        input A as a increasing list, K is what to find
        return the index if found, else, return -1
        we only consider candidates between left and right(inclusive), so left and right are the bound of consideration.
        we always loop by condition of left<right, and check the result again to see if it's what expected.
        we always consider three conditions, got, smaller, larger.
    """

    if not A:
        return -1

    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] == K:  # Got
            return mid
        elif A[mid] < K:  # Smaller
            left = mid + 1
        elif A[mid] > K:  # Larger
            right = mid - 1

    if left == right and A[left] == K:
        return left
    else:
        return -1


def binary_search_lower_bound(A: List[int], K: int) -> int:
    """ find lower bound
        A=[1,2,3,3,3,4], K=3
        return 2
    """
    if not A:
        return -1

    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] == K:
            right = mid
        elif A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid - 1

    if left == right and A[left] == K:
        return left
    else:
        return -1


def binary_search_upper_bound(A: List[int], K: int) -> int:
    """ find upper bound
        A=[1,2,3,3,3,4], K=3
        return 4
    """
    if not A:
        return -1

    left = 0
    right = len(A) - 1
    while left < right:
        mid = ceil((left + right) / 2)  # Note we need to use ceil for upper bound
        if A[mid] == K:
            left = mid
        elif A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid - 1

    if left == right and A[left] == K:
        return left
    else:
        return -1


def binary_search_lower_pos(A: List[int], K: int) -> int:
    """ find i to insert K s.t. A[i-1]<K<=A[i+1]
    """
    if A is None:
        return -1
    elif A == []:
        return 0

    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] == K:
            right = mid
        elif A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid

    assert left == right
    return left


def binary_search_upper_pos(A: List[int], K: int) -> int:
    """ find i to insert K s.t. A[i-1]<=K<A[i+1]
    """
    if A is None:
        return -1
    elif not A:
        return 0

    left = 0
    right = len(A)  # Note, this position is also considerable
    while left < right:
        mid = (left + right) // 2
        if A[mid] == K:
            left = mid + 1
        elif A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid

    assert left == right
    return left


if __name__ == '__main__':
    A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 1, 85, 93, 98]
    print(f'find 31: {binary_search(A, 31)}')
    print(f'find 3: {binary_search(A, 3)}')
    print(f'find 98: {binary_search(A, 98)}')
    print(f'find 50: {binary_search(A, 50)}')
    print(f'find 1: {binary_search(A, 1)}')
    print(f'find 100: {binary_search(A, 100)}')

    print('-' * 20)
    print('find bound')

    B = [1] * 3
    print('B:', B)
    C = [0] + B + [2]
    print('C:', C)

    print('find lower bound of 1 in B: {}'.format(binary_search_lower_bound(B, 1)))
    print('find lower bound of 1 in C: {}'.format(binary_search_lower_bound(C, 1)))
    print('find lower bound of 1 in [1]: {}'.format(binary_search_lower_bound([1], 1)))
    print('find lower bound of 3 in B: {}'.format(binary_search_lower_bound(B, 3)))
    print('find lower bound of 3 in C: {}'.format(binary_search_lower_bound(C, 3)))
    print('find lower bound of 3 in [1]: {}'.format(binary_search_lower_bound([1], 3)))
    print('find lower bound of -1 in B: {}'.format(binary_search_lower_bound(B, -1)))
    print('find lower bound of -1 in C: {}'.format(binary_search_lower_bound(C, -1)))
    print('find lower bound of -1 in [1]: {}'.format(binary_search_lower_bound([1], -1)))
    print('find lower bound of 1 in []: {}'.format(binary_search_lower_bound([], 1)))

    print('-' * 20)

    print('find upper bound of 1 in B: {}'.format(binary_search_upper_bound(B, 1)))
    print('find upper bound of 1 in C: {}'.format(binary_search_upper_bound(C, 1)))
    print('find upper bound of 1 in [1]: {}'.format(binary_search_upper_bound([1], 1)))
    print('find upper bound of 3 in B: {}'.format(binary_search_upper_bound(B, 3)))
    print('find upper bound of 3 in C: {}'.format(binary_search_upper_bound(C, 3)))
    print('find upper bound of 3 in [1]: {}'.format(binary_search_upper_bound([1], 3)))
    print('find upper bound of -1 in B: {}'.format(binary_search_upper_bound(B, -1)))
    print('find upper bound of -1 in C: {}'.format(binary_search_upper_bound(C, -1)))
    print('find upper bound of -1 in [1]: {}'.format(binary_search_upper_bound([1], -1)))
    print('find upper bound of 1 in []: {}'.format(binary_search_upper_bound([], 1)))

    print('-' * 20)

    print('find insert index of 1 in B: {}'.format(binary_search_lower_pos(B, 1)))
    print('find insert index of 1 in C: {}'.format(binary_search_lower_pos(C, 1)))
    print('find insert index of 1 in [1]: {}'.format(binary_search_lower_pos([1], 1)))
    print('find insert index of 3 in B: {}'.format(binary_search_lower_pos(B, 3)))
    print('find insert index of 3 in C: {}'.format(binary_search_lower_pos(C, 3)))
    print('find insert index of 3 in [1]: {}'.format(binary_search_lower_pos([1], 3)))
    print('find insert index of -1 in B: {}'.format(binary_search_lower_pos(B, -1)))
    print('find insert index of -1 in C: {}'.format(binary_search_lower_pos(C, -1)))
    print('find insert index of -1 in [1]: {}'.format(binary_search_lower_pos([1], -1)))
    print('find insert index of 1 in []: {}'.format(binary_search_lower_pos([], 1)))

    print('-' * 20)

    print('find insert index of 1 in B: {}'.format(binary_search_upper_pos(B, 1)))
    print('find insert index of 1 in C: {}'.format(binary_search_upper_pos(C, 1)))
    print('find insert index of 1 in [1]: {}'.format(binary_search_upper_pos([1], 1)))
    print('find insert index of 3 in B: {}'.format(binary_search_upper_pos(B, 3)))
    print('find insert index of 3 in C: {}'.format(binary_search_upper_pos(C, 3)))
    print('find insert index of 3 in [1]: {}'.format(binary_search_upper_pos([1], 3)))
    print('find insert index of -1 in B: {}'.format(binary_search_upper_pos(B, -1)))
    print('find insert index of -1 in C: {}'.format(binary_search_upper_pos(C, -1)))
    print('find insert index of -1 in [1]: {}'.format(binary_search_upper_pos([1], -1)))
    print('find insert index of 1 in []: {}'.format(binary_search_upper_pos([], 1)))