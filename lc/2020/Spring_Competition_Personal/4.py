# @File: 4.py
# @Author: Kevin Huo
# @Date: 2020/4/18

from typing import List


def minJump(jump: List[int]) -> int:
    res = 0
    N = len(jump)

    opts = []
    # 求每一个 i 的最小步数
    for i in range(0, N):
        curr_idx = i
        curr_opt = 0
        while (curr_idx + jump[curr_idx]) < N:
            curr_opt += 1
            # 先往左
            if curr_idx > 0:
                curr_opt += min(opts[:i])
                continue
            # 再往右
            curr_idx += 1
        # 若curr_idx 能跳出去, 则准备写入 opts, 并计算下一个i




        opts.append(curr_opt)
    return res