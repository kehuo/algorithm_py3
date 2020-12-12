# @File: binary_search
# @Author: Kevin Huo
# @LastUpdate: 12/11/2020 1:48 AM


def binary_search_unique(arr, x, left=None, right=None):
    """保证arr每一项都是唯一的"""
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_left_insertion(arr, x, left=None, right=None):
    """这种算法可以允许 arr 中有重复元素
    该算法的作用在于将x插入到arr的适当位置, 同时保持arr有序.
    当遇到和x重复的元素时, 在该元素左侧插入

    该算法在实现上和上面的unique算法有4处区别
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    # 和unique算法的区别 1: 这里是<, 而不是"小于等于"
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == x:
            # 区别2: 遇到重复元素则继续往左边找
            right = mid
        elif arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            # 区别3: right=mid 而不是mid-1
            right = mid
    # 区别4: 最后返回left 而不是 -1
    return left


def binary_search_right_insertion(arr, x, left=None, right=None):
    """
    允许arr内的元素重复
    如果x和某元素重复, 那么将x插入到最右边, 同时保证arr插入后仍然有序
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == x:
            # 因为是向右插入, 所以遇到重复元素后继续在右侧搜索
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid
    return left


def main():
    A = [2, 3, 6, 8, 9, 11, 25, 66]
    x = 11
    print("唯一算法: ", binary_search_unique(A, x))

    B = [2, 2, 3, 3, 4, 4, 5, 6, 7]
    y = 3
    print("左侧插入搜索: ", binary_search_left_insertion(B, y))
    print("右侧插入搜索: ", binary_search_right_insertion(B, y))


if __name__ == '__main__':
    main()
