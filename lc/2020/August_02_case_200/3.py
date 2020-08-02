# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 10:06 AM

from typing import List


class Solution:
    def check(self, grid) -> (bool, dict):
        """
        已经通过
        https://leetcode-cn.com/contest/weekly-contest-200/problems/minimum-swaps-to-arrange-a-binary-grid/

        对于长度为 n 的grid, d的长度是 n-1
        d = {
            从右到左连续2个0的索引: [1, 2],
            从右到左连续1个0的索引: [1, 2]
        }

        对于 grid = [
            [0, 0, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]

        d = {
            2: [1, 2],
            1: [1, 2]
        }

        返回: True, d
        """
        d = {}
        res = True

        # print(grid)
        length_g = len(grid)
        length_g_one = len(grid[0])

        not_valid_count = 0

        used = []
        for i in range(length_g):
            meet_one = False
            g = grid[i]
            for n in range(1, length_g_one):
                if length_g_one - n not in d:
                    d[length_g_one - n] = []
                if g[n:] == [0] * (length_g_one - n):
                    # print("g: %s, g[n:]=%s" % (g, g[n:]))
                    meet_one = True
                    if i not in used:
                        d[length_g_one - n].append(i)
                    if len(d[length_g_one - n]) == 1:
                        used.append(i)
            if meet_one is False:
                if not_valid_count == 0:
                    not_valid_count += 1
                    continue
                res = False
                break
        # print("end, d=%s" % d)
        if res is True:
            for k, v in d.items():
                if len(v) == 0:
                    res = False
                    break

        return res, d

    def filter_arr(self, raw, used):
        """
        从 raw 中减掉 used中的
        raw = [1, 2, 3, 4]
        used = [4, 5]
        res = [1, 2, 3]
        """
        return list(set(raw) - set(used))

    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        grid = [
            [0, 0, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]

        d = {
            2: [1, 2],
            1: [1, 2]
        }

        sorted_d = {2: [1], 1:[2]}

        """
        is_valid, d = self.check(grid)
        print(is_valid)
        # print(d)
        if is_valid is False:
            return -1

        sorted_d = {}
        used = []
        length_grid = len(grid) - 1
        for i in range(length_grid, 0, -1):
            # print(i)
            for k in d:
                if k == i:
                    sorted_d[k] = min(self.filter_arr(d[k], used))
                    used.append(sorted_d[k])
                    break
        # print("排序后的d: %s" % sorted_d)
        # 2个0的，移动到 len-1-n 行 = 3 - 1 - 2行
        # 1个0的，移动到 3 - 1-1=1行
        # 我在移动sorted_d[2]时, 要检查sorted_d 的 k, v中，所有v 比sorted_d[2] 小的值，并且全部+1
        # 一共循环 length - 1次. 比如3x3的矩阵，一共循环2次.
        count = len(sorted_d)
        res = 0
        while count > 0:
            curr_row = sorted_d[count]
            # 比如当前 1 0 0在第curr_row = 第1行，我要将他移动到第length_grid - 1 - count = 3-1-2=第0行，需要移动的步数 = 1-0 = 1步
            target_row = length_grid - count
            diff = abs(curr_row - target_row)
            res += diff
            # print("看连续%s个0, 当前在第%s行, 要移动到第%s行, 一共需要移动%s步, 当前总共移动了%s步" % (count, curr_row, target_row, diff, res))
            # 这里检查所有比 sorted_d[2] 的值小的项，并将其+1
            for k, v in sorted_d.items():
                if k == count:
                    continue
                if v < curr_row:
                    sorted_d[k] += 1

            # print("count=%s, sorted_d=%s" % (count, sorted_d))
            count -= 1
        return res

    def minSwaps_v2(self, grid: List[List[int]]) -> int:
        """
        ZL version
        虽然输入是2二维数组，但是，因为从题目可以看出这个问题是一维问题，所以该算法将二维grid压缩成一维rows 进行处理.

        该题需要有2部分:
        1 - 数据预处理
        2 - 核心算法
        """
        # 1 - 数据预处理，将二维数组grid 压缩成一维 rows
        rows = []
        for row in grid:
            cnt = 0
            for cell in row[::-1]:
                if cell == 0:
                    cnt += 1
                else:
                    break
            rows.append(cnt)

        # 2-  核心算法部分
        n = len(rows)
        shift = [0] * n
        now = 0
        required = n - 1
        ans = 0

        # print(rows,shift)
        while now < n:
            for i in range(n):
                if rows[i] >= required:
                    ans += i + shift[i] - now
                    rows[i] = -1
                    break
                else:
                    shift[i] += 1
            # 和for循环配合使用, 当一整个for循环都遍历完成，而且没有触发过break的话，则进入else
            else:
                return -1
            # print(rows,shift,ans)
            now += 1
            required -= 1
        return ans


if __name__ == '__main__':
    tests = [
        [[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0]]
    ]
