# @File: m3
# @Author: Kevin Huo
# @LastUpdate: 3/26/2020 8:22 PM


from typing import List

def numRookCaptures(self, board: List[List[str]]) -> int:
    """https://leetcode-cn.com/problems/available-captures-for-rook/
    由于棋盘大小固定 8x8, 所以基本可以忽略复杂度太高导致超时的问题

    1. 遍历棋盘, 找到唯一的 白色车 R. 找到后记录R的行列值 pr 和 pc, 终止循环 (pr = point row, pc = point col 的简写)
    2. 分别看 白车的 上/下/左/右, 并实时更新res值.
    3. 上下左右都看完以后, 返回结果.
    """
    res = 0
    has_R = False

    for i in range(8):
        row = board[i]
        for j in range(8):
            if row[j] == "R":
                pr, pc = i, j
                has_R = True
                break
        if has_R:
            break
    # up
    for idx in range(pr - 1, -1, -1):
        chess = board[idx][pc]
        if chess == "B":
            break
        if chess == "p":
            res += 1
            break

    # down
    for idx in range(pr + 1, 8):
        chess = board[idx][pc]
        if chess == "B":
            break
        if chess == "p":
            res += 1
            break

    # left
    for idx in range(pc - 1, -1, -1):
        chess = board[pr][idx]
        if chess == "B":
            break
        if chess == "p":
            res += 1
            break

    # right
    for idx in range(pc + 1, 8):
        chess = board[pr][idx]
        if chess == "B":
            break
        if chess == "p":
            res += 1
            break
    return res
