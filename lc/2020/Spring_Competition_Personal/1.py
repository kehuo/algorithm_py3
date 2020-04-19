# @File: 1.py
# @Author: Kevin Huo
# @Date: 2020/4/18


def s(arr, sort_key_idx):
    # start = arr[0]
    # end = arr[-1]
    # idx = 0
    #
    # arr.sort(key=lambda x: x[idx])
    # while (start[-1] > end[-1]) and (idx < len(start) - 1):
    #     idx += 1
    #     arr.sort(key=lambda x: x[idx])
    arr.sort(key=lambda x: x[sort_key_idx])
    return arr


a = [[8, 1, 14], [9, 17, 12], [15, 10, 7], [2, 11, 3]]
print(s(a, 0))
print(s(a, 1))
print(s(a, 2))
