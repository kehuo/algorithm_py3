# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 10/25/2020 5:28 PM

from typing import List


class Solution(object):
    def longestMountain(self, A: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/longest-mountain-in-array/

        官方题解
        https://leetcode-cn.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode-sol/
        """
        n = len(A)
        if n == 0:
            return 0

        left = [0] * n
        for i in range(1, n):
            left[i] = left[i-1] + 1 if A[i - 1] < A[i] else 0

        right = [0] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + 1 if A[i + 1] < A[i] else 0

        res = 0
        for i in range(n):
            if left[i]>0 and right[i] > 0:
                res = max(res, left[i]+right[i]+1)
        print(res)
        return res


if __name__ == '__main__':
    tests =[
        [2, 1, 4, 7, 3, 2, 5]
    ]
    t = tests[0]
    s = Solution()
    s.longestMountain(t)
