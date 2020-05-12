# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/12/2020 1:20 PM

from typing import List


class Solution(object):
    """
    https://leetcode-cn.com/explore/featured/card/array-and-string/198/introduction-to-array/770/

    已通过
    """
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length in [0, 1]:
            return -1

        res = []
        left = 0
        right = sum(nums[1:])
        for i in range(length):
            n = nums[i]
            # print("i=%s, n=%s, left=%s, right=%s" % (i, n, left, right))
            if left == right:
                res.append(i)
            left += n
            try:
                right -= nums[i+1]
            except IndexError:
                right = 0

        return -1 if len(res) == 0 else res[0]


if __name__ == '__main__':
    # answer = [3, 0, 5]
    tests = [
        [1, 7, 3, 6, 5, 6],
        [-1, -1, -1, 0, 1, 1],
        [-1, -1, 0, 1, 1, 0]
    ]
    t = tests[0]

    runner = Solution()
    r = runner.pivotIndex(t)
    print(r)
