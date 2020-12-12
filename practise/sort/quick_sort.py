# @File: quick_sort
# @Author: Kevin Huo
# @LastUpdate: 12/11/2020 12:53 AM


def quick_sort(A):
    quick_sort_helper(A, 0, len(A) - 1)


def quick_sort_helper(A, p, r):
    """完全按照算法导论实现"""
    if p < r:
        q = partition(A, p, r)
        quick_sort_helper(A, p, q - 1)
        quick_sort_helper(A, q + 1, r)


def partition(A, p, r):
    """递归地分区 + 原地排序 (inplace sort)
    x 是分区地主元 pivot
    注意，主元地取值有很多种方式, 中间值法, 随机法等等, 这里取最右边值, 简单而且是算法导论地默认使用方法.
    """
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def main():
    arr = [5, 6, 7, 2, 2, 10, 9, 4]
    quick_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
