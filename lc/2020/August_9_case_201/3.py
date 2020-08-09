# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 8/9/2020 10:29 AM


from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List, target: int) -> int:
        """
        2020-8-9 暂未通过 leetcode 测试
        5471. 和为目标值的最大数目不重叠非空子数组数目
        https://leetcode-cn.com/contest/weekly-contest-201/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
        1 - d字典存储所有计算结果，不论是否等于 target
        2 - 从 d 中找到所有等于 target 的结果，放入 arr
            d[start] = [[sum, is_equal_target], [sum, is_equal_target], ...]
            d[start][x] 在 nums 中的索引  = start + x

        3 - 从 arr 中得到最终结果
            arr = [[start_idx, end_idx], [start_idx, end_idx], ...]

        数据结构示例:
        nums = [-1,3,5,1,4,2,-9]
        target = 6
        d = {
            0: [[-1, False], [2, False], [7, False], [8, False], [12, False], [14, False], [5, False]],
            1: [[3, False], [8, False], [9, False], [13, False], [15, False], [6, True]],
            2: [[5, False], [6, True], [10, False], [12, False], [3, False]],
            3: [[1, False], [5, False], [7, False], [-2, False]],
            4: [[4, False], [6, True], [-3, False]],
            5: [[2, False], [-7, False]],
            6: [[-9, False]]
        }

        arr = [[1, 6], [2, 3], [4, 5]]

        todo - 根据 arr, 数量不重复的子数组的最大数量
        求解方法似乎和 176竞赛第三题 - 最大会议数量有相似之处，但又不是完全一样。可以稍微借鉴一下思路：
        https://leetcode-cn.com/submissions/detail/48055193/

        比如 arr 中:
        [1,6] 和 [2,3]重复
        [1,6] 和 [4,5]也重复
        但是 [2,3]和[4,5]不重复

        所以 [2,3] 和 [4, 5] 就是2个符合要求的子数组，所以最大数量是2，这道题最终的答案就是2.
        """

        # step - 1 求d
        d = {}
        len_n = len(nums)
        for i in range(len_n):
            if i - 1 in d:
                # 用前一行的数据计算当前行
                # 比如 nums = [1, 3, 5, 7, 9]
                # 若 nums[1:3] = [3, 5], 则 sum(nums[1:3]) = 3+5=8
                # 那么, sum(nums[2:3]) = 8-3 = 5
                d[i] = list(map(lambda x: [x[0] - nums[i - 1], (x[0] - nums[i - 1]) == target], d[i - 1][1:]))
                if i == len_n - 1:
                    break
                continue
            if i not in d:
                d[i] = list(map(lambda x: [sum(nums[i:x]), sum(nums[i:x]) == target], range(i + 1, len_n + 1)))
        # print(d)

        # step 2 - 求arr
        arr = []
        for k, v in d.items():
            # arr[0] = [start, end, sum]
            len_v = len(v)
            for idx in range(len_v):
                one = v[idx]
                # one = [sum, is_equal]
                if one[1] is True:
                    # match = [start, end]
                    match = [k, k + idx]
                    arr.append(match)
        print(arr)

        # todo step 3 - 根据res求最终的res

        return 0
