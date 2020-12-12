# @File: merge_sort
# @Author: Kevin Huo
# @LastUpdate: 11/28/2020 2:06 AM


def merge_sort(arr):
    """归并排序, 也是原地排序, 不需要返回arr"""
    copy_buffer = [None] * len(arr)
    merge_sort_helper(arr, copy_buffer, 0, len(arr) - 1)


def merge_sort_helper(arr, copy_buffer, low, high):
    """递归地跳出条件是 low >= high """
    if low < high:
        mid = (low + high) // 2
        merge_sort_helper(arr, copy_buffer, low, mid)
        merge_sort_helper(arr, copy_buffer, mid + 1, high)
        merge_core(arr, copy_buffer, low, mid, high)


def merge_core(arr, copy_buffer, low, mid, high):
    """
    核心函数, 合并2个子数组
    sublist1 = arr[low : mid+1]
    sublist2 = arr[mid+1: high+1]
    """
    i1 = low
    i2 = mid + 1
    for i in range(low, high + 1):
        # 如果sublist 1 已经排完, 只剩sublist 2, 那直接依次将sublist 2 拼接到copy_buffer后面即可.
        if i1 > mid:
            copy_buffer[i] = arr[i2]
            i2 += 1
        elif i2 > high:
            copy_buffer[i] = arr[i1]
            i1 += 1
        # 如果2个子数组都还有剩余数字, 那么比较大小, 将较小值放入buffer
        elif arr[i1] < arr[i2]:
            copy_buffer[i] = arr[i1]
            i1 += 1
        else:
            copy_buffer[i] = arr[i2]
            i2 += 1
    # 全部归并完成后, 将copy_buffer的值更新到arr中
    for i in range(low, high + 1):
        arr[i] = copy_buffer[i]


def main():
    A = [5, 4, 6, 2, 7, 2, 6, 2, 1, 6, 7]
    merge_sort(A)
    print(A)


if __name__ == '__main__':
    main()
