# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 5/12/2020 2:06 PM

from typing import List


class Solution:
    """
    https://leetcode-cn.com/explore/featured/card/array-and-string/198/introduction-to-array/772/
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        raw_str = str((int("".join([str(x) for x in digits])) + 1))
        for i in raw_str:
            res.append(int(i))
        return res


if __name__ == '__main__':
    # answer = [[1, 2, 4], [4, 3, 2, 2]]
    tests = [
        [1, 2, 3],
        [4, 3, 2, 1]
    ]
    t = tests[0]

    runner = Solution()
    r = runner.plusOne(t)
    print(r)
