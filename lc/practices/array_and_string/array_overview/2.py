# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 5/12/2020 2:05 PM


from collections import Counter
from typing import List


class Solution:
    """
    https://leetcode-cn.com/explore/featured/card/array-and-string/198/introduction-to-array/771/
    """
    def dominantIndex(self, nums: List[int]) -> int:
        largest_val = max(nums)
        c = Counter(nums)

        if c[largest_val] > 1:
            return -1

        length = len(nums)
        for i in range(length):
            n = nums[i]
            if n == largest_val:
                largest_idx = i
                continue
            if 2 * n > largest_val:
                largest_idx = -1
                break
        return largest_idx


if __name__ == '__main__':
    # answer =
    tests = [
        [3, 6, 1, 0],
        [1, 2, 3, 4]
    ]
    t = tests[0]

    runner = Solution()
    r = runner.dominantIndex(t)
    print(r)
