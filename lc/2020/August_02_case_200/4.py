# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 10:06 AM

from typing import List


class Solution(object):
    """
    https://leetcode-cn.com/problems/get-the-maximum-score/
    lc没通过，答案有错，需要继续改进
    """
    def cal_common_points(self, nums1, nums2):
        """
        计算2个数组所有的共同点
        nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]

        res = [(value, nums1_idx, nums2_idx)]
        res = [(4, 1, 0), (8, 3, 2)]
        """
        res = []
        len_1, len_2 = len(nums1), len(nums2)
        for i in range(len_1):
            c1 = nums1[i]
            for j in range(len_2):
                c2 = nums2[j]
                if c1 == c2:
                    tmp = (c1, i, j)
                    res.append(tmp)
        return res

    def visit_arr(self, start, other, commons, start_idx=1):
        """
        start_arr: 起始数组比如 nums1
        other_arr: 另一个数组比如 nums2
        commons: cal_common_points 函数返回的结果，包含所有共同点.
        start_idx = 1 or 2
        返回 最大分数

        分数分为3部分:
        s1 = 遇到第一个共同点之前的总分数
        s2 = 共同点期间的动态规划计算的分数
        s3 = 最后一个共同点后的分数

        score = s1 + s2 + s3

        比如 nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]

        数据结构如下
        ###########################
           2
           4(共同点1)
         5   6
           8(共同点2, 最后一个共同点)
         10 9
        ###########################

        commons = [(value, start_idx, other_idx)]
        commons = [(4, 1, 0), (8, 3, 2)]

        假设这次 start = nums1, 则
        s1 = sum(start[:commons[0][1]])
           = sum(start[:1])
           = sum([2])
           = 2

        s2 = sum([x[0] for x in commons]) + max(sum(start[1+1:3]), sum(other[0+1:3]))
           = sum([4, 8]) + max(sum([5]), sum([6]))
           = 12 + max(5, 6)
           = 12 + 6
           = 18

        s3 = max(sum(start[3+1:]), sum([sum(other[2+1:])]))
           = max(sum([10]), sum([9]))
           = max([10, 9])
           = 10

        s = sum(s1, s2, s3) = 28
        """
        other_idx = 1 if start_idx == 2 else 2
        s1 = sum(start[:commons[0][start_idx]])
        len_commons = len(commons)

        s2 = sum([x[0] for x in commons])
        for i in range(len_commons - 1):
            curr = commons[i]
            next_c = commons[i+1]
            s2 += max(sum(start[curr[start_idx]+1:next_c[start_idx]]), sum(other[curr[other_idx]+1:next_c[other_idx]]))

        last_c = commons[-1]
        s3 = max(sum(start[last_c[start_idx] + 1:]), sum([sum(other[last_c[other_idx] + 1:])]))

        score = s1 + s2 + s3
        # print(s1, s2, s3, score)
        return score

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/get-the-maximum-score/

        可能会用到动态规划的思路

        输入：nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
        输出：30
        解释：合法路径包括：
        [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],（从 nums1 开始遍历）
        [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]  （从 nums2 开始遍历）
        最大得分为上图中的绿色路径 [2,4,6,8,10] 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/get-the-maximum-score
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        print("n1=%s" % nums1)
        print("n2=%s" % nums2)
        commons = self.cal_common_points(nums1, nums2)
        print("commons: %s" % commons)
        if len(commons) == 0:
            res = max(sum(nums1), sum(nums2))
        else:
            nums1_max_score = self.visit_arr(nums1, nums2, commons)
            nums2_max_score = self.visit_arr(nums2, nums1, commons, start_idx=2)
            res = max(nums1_max_score, nums2_max_score)
        print(res)
        return res % (10^9 + 7)


if __name__ == '__main__':
    # 正确答案 = [30, 109, 40, 61]
    tests = [
        [[2, 4, 5, 8, 10], [4, 6, 8, 9]],
        [[1,3,5,7,9], [3, 5,100]],
        [[1,2,3,4,5], [6,7,8,9,10]],
        [[1,4,5,8,9,11,19], [2,3,4,11,12]]
    ]
    t = tests[3]
    solution = Solution()
    solution.maxSum(*t)
