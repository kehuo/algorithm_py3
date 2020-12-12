# @File: counting_sort
# @Author: Kevin Huo
# @LastUpdate: 12/11/2020 1:30 AM


def counting_sort(A):
    """完全按照算法导论实现
    默认A数组中所有项的取值都在闭区间 [0,k] 内.
    假设k=10
    """
    B = [None] * len(A)
    k = 10
    return counting_sort_helper(A, B, k)


def counting_sort_helper(A, B, k):
    C = [0 for _ in range(0, k + 1)]
    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    j = len(A) - 1
    while j >= 0:
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
        j -= 1
    return B


def main():
    arr = [5, 2, 6, 7, 2, 4, 6, 8]
    res = counting_sort(arr)
    print(res)


if __name__ == '__main__':
    main()
