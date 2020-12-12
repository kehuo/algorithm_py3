# @File: radix_sort
# @Author: Kevin Huo
# @LastUpdate: 11/28/2020 1:49 AM


"""基数排序"""
from typing import List
import itertools


class Solution:
    def maximumGap_demical(self, nums: List[int]) -> int:
        """十进制基数排序"""
        def radix_sort(numbers):
            # 0 to 2147483647 因为左边这个最大的10进制数（2147483647）一共10位, 所以pos的取值范围是0到10
            for pos in range(10):
                res = [[] for _ in range(10)]
                divisor = 10 ** pos
                for n in numbers:
                    digit = n // divisor % 10
                    res[digit].append(n)
                numbers = itertools.chain.from_iterable(res)
            return numbers

        nums = list(radix_sort(nums))
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        return ans

    def maximumGap_binary(self, nums: List[int]) -> int:
        """二进制基数排序
        itertools.chain.from_iterable(['ABC', 'DEF']) --> A B C D E F

        a>>b:
        把a的二进制表示，向右移动b位
        4 >> 1 后等于 10进制的2
        因为 4 的二进制 = 11
        全部右移1位后，变成二进制的 1， 也就是10进制的2
        """
        def radix_sort(numbers):
            # 0 to 1<<32
            for pos in range(32):
                res = [[] for _ in range(2)]
                mask = 1 << pos
                for n in numbers:
                    digit = int((n & mask) > 0)
                    res[digit].append(n)
                numbers = itertools.chain.from_iterable(res)
            return numbers

        nums = list(radix_sort(nums))
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        return ans



