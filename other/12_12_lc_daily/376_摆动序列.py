# @File: 376_摆动序列
# @Author: Kevin Huo
# @LastUpdate: 12/12/2020 10:54 AM


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        输入 [1] >> 输出 1

        我们的目标就是找到所有的 波峰(小-大-小) 和 波谷(大-小-大)
        1. k 代表线段斜率
            当前线段的斜率 currk = nums[i] - nums[i-1]
            下一条线段的斜率 nextk = nums[i+1] - nums[i]
        2. 对于每个 i, 判断2条线段的斜率:
            >> 如果 currk * nextk < 0, 则符合摆动要求(斜率1正1负, 乘积为负):
                res+=1
            >> 如果 currk * nextk >= 0, 则不符合摆动要求
            判断结束后 i += 1

        """
        n = len(nums)
        if n <= 1:
            return n
        if n == 2:
            return 1 if nums[0] == nums[1] else 2



if __name__ == '__main__':
    tests = [
        [51,226,208,165,202,286,190,212,219,271,36,245,20,238,238,89]
    ]
    t = tests[0]
    s = Solution()
    s.wiggleMaxLength(t)