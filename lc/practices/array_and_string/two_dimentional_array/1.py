# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/12/2020 2:28 PM

from typing import List


class Solution:
    """
    https://leetcode-cn.com/explore/featured/card/array-and-string/199/introduction-to-2d-array/774/
    """
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        len_row = len(matrix)
        len_col = len(matrix[0])

        max_loop_count = len_row + len_col - 1
        # initial direction is "right up"
        direction = "right_up"
        while max_loop_count > 0:
            max_loop_count -= 1
        # todo
        return res

    def update_direction(self, curr_row, curr_col):
        """
        right_up: (curr_row > 0) and (curr_col < len(matrix[0]))
        left_down: (curr_row < len(matrix)) and (curr_col > 0)
        """
        return "right_up"


if __name__ == '__main__':
    # answer = [3, 0, 5]
    tests = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]
    t = tests[0]

    runner = Solution()
    r = runner.findDiagonalOrder(t)
    print(r)
