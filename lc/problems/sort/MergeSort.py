# @File: MergeSort
# @Author: Kevin Huo
# @LastUpdate: 11/7/2020 8:57 PM

from typing import List


class MergeSorter(object):
    """
    合并算法
    参考 <数据结构 (Python 语言描述)> 第3章 3.5节 更快的排序中的 "合并排序" 实现.

    1. 该算法利用的递归, 用分治法突破 O(n^^2)的瓶颈.
    2. 以下是该算法的非正式概括：
        2.1 计算一个列表的中间位置, 并且递归地排序其左边的和右边的子数组 (分治)
        2.2 将2个排好序的子数组， 合并为一个更大的排好序的子数组.
        2.3 当子数组不能再划分时 (子数组长度为1), 停止此过程.

    3. 有3个函数在顶层的设计中互相协作:
        3.1 merge_sort: 用户调用的函数
        3.2 merge_sort_helper: 一个辅助函数, 它隐藏了递归调用所需要的额外参数.
        3.3 merge: 实现合并过程的函数.
    """
    def merge_sort(self, arr):
        """
        该函数作为对外可调用的api, 实现合并排序.
        具体的内部实现, 将和其他2个内部函数 merge_sort_helper 和 merge 共同实现.

        参数:
        raw: 输入的待排序的初始数组.
        copy_buffer: 在合并时会用到的一个临时数组.
        """
        # 我们的合并排序的区间, 从 [0, len(raw)] 整个区间开始
        copy_buffer = [0] * len(arr)
        self.__merge_sort_helper(arr, copy_buffer, low_idx=0, high_idx=len(arr) - 1)
        return arr

    def __merge_sort_helper(self, arr, copy_buffer, low_idx, high_idx):
        """
        ** private method **
        arr: 输入的未排序数组
        copy_buffer: 合并时可能用到的临时数组
        low_idx / high_idx: 待归并数组的2个索引, 分别代表左右边界 (包含)
        mid: 待合并数组的中间索引
        """
        if low_idx < high_idx:
            mid = (low_idx + high_idx) // 2
            # 对左子数组继续递归地拆分成 左/右 子数组
            self.__merge_sort_helper(arr, copy_buffer, low_idx, mid)
            # 对右子数组继续递归地拆分成 左/右 子数组
            self.__merge_sort_helper(arr, copy_buffer, mid+1, high_idx)
            # 当拆到不能继续拆时 （子数组长度为1）, 将2个子数组进行合并
            self.__merge(arr, copy_buffer, low_idx=low_idx, mid=mid, high_idx=high_idx)

    def __merge(self, arr, copy_buffer, low_idx, mid, high_idx):
        """
        *** private method ***
        """
        # 首先, 初始化2个指针, 分别指向左子数组 和 右子数组 的第一个元素
        lidx = low_idx
        ridx = mid + 1

        # 然后, 遍历左右2个子数组, 比较left_arr[lidx] 和 right_arr[ridx]. 将较小的一个放入 self.copy_buffer 中.
        # 遍历一次 (lox_idx, high_idx + 1), 将比较后较小的值填入 copy_buffer[i]即可.
        for i in range(low_idx, high_idx+1):
            # 如果左子数组提前结束, 到达的有边界mid, 则将右子数组剩下的部分拼接到后面即可.
            if lidx > mid:
                copy_buffer[i] = arr[ridx]
                ridx += 1
                continue
            # 和上面类似, 如果右子数组提前结束, 到达的有边界high_idx, 则将左子数组剩下的部分拼接到后面即可.
            if ridx > high_idx:
                copy_buffer[i] = arr[lidx]
                lidx += 1
                continue

            # 下面就是正常比较大小, 并将较小值放入buffer中, 然后将这个子数组的索引往前移一格.
            if arr[lidx] < arr[ridx]:
                # 左边小, 从左子数组取出当前项, 放入buffer, 并将 lidx 向右移动一格.
                copy_buffer[i] = arr[lidx]
                lidx += 1
            else:
                # 右边小, 从右子数组取出当前项, 放入buffer, 并将 ridx 向右移动一格.
                copy_buffer[i] = arr[ridx]
                ridx += 1

        # 整个遍历完以后, self.copy_buffer中 [low_idx, high_idx] (2边都包含)部分已经排序. 将其放入arr中.
        for i in range(low_idx, high_idx+1):
            arr[i] = copy_buffer[i]


if __name__ == '__main__':
    tests = [
        [4, 1, 7, 6, 5, 3, 8, 2],
        [2]
    ]
    t = tests[1]
    m = MergeSorter()
    sorted_arr = m.merge_sort(t)
    print(sorted_arr)

