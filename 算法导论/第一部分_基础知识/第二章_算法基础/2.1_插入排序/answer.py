# @File: answer.py
# @Author: Kevin Huo
# @LastUpdate: 2/26/2020 11:29 PM


def insertion_sort(arr):
    """
    # 注意, 伪代码中的数组索引是从1开始的, 但是python中是从0开始的, 写代码时注意索引的正确性.
    一般伪代码中的 A[1] 就是实际代码的 arr[0]

    Insertion-Sort(A)
    1. for j = 2 to A.length
    2.     key = A[j]
    3.     # insert A[j] into the sorted sequence A[1, ..., j-1]
    4.     i = j - 1
    5.     while i > 0 and A[i] > key:
    6.         A[i + 1] = A[i]
    7.         i = i - 1
    8.     A[i + 1] = key
    """
    for j in range(1, len(arr)):
        key = arr[j]
        # insert arr[j] into the sorted sequence arr[0] ~ arr[j-1]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == '__main__':
    tests = [
        [5, 2, 4, 6, 1, 3],
        [7, 9, 6, 4, 5]
    ]

    for one in tests:
        print(insertion_sort(one))
