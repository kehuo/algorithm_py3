# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 11/11/2020 10:34 PM


import collections


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """dp"""
        def min_step(raw, curr_idx, target_idx):
            """
            输入:
            一个字符串 raw, 和一个目标索引target_idx, 还有一个当前的索引位置curr_idx.
            返回:
            顺时针和 逆时针需要步数的较小值:
            巧妙地方法:
            你将 raw 看成一个圈, 那么这个圈地周长就是 len(raw), 那么我们可以将这个圆圈分成2段:
            A段是 从curr_idx顺时针转到target_idx的距离, 我们用 abs(curr_idx-target_idx) 表示.
            那么显而易见, B段的长度就等于 len(raw) - A短的长度.
            返回A和B的较短距离即可》
            """
            n = len(raw)
            fwd_steps = abs(curr_idx - target_idx)
            back_steps = n - fwd_steps
            return min(fwd_steps, back_steps)

        nk = len(key)
        nr = len(ring)
        dp = [[int(float("inf"))] * nr for _ in range(nk)]
        # 1 先统计rings 中 每一个key[i]出现的索引位置. 可以大量减少dp的计算量.
        # todo 这里统计的时候可以不用考虑key, 将所有ring的值的索引都写入stat, 这种做法在key长度较大时，能节省很多时间.
        # 因为你Key每多一个字符, 就多一次ring的遍历, 还是非常值得优化的.
        stat = collections.defaultdict(list)
        for k in key:
            for i in range(nr):
                if ring[i] == k:
                    stat[k].append(i)
        # 2 再初始化dp[0]中所有的值.
        for kidx in stat[key[0]]:
            # 假设key="gd", ring="godding", 那么: stat[key[0]] = stat["g"] = [0, 6]
            # 分别在ring中逆时针/顺时针旋转, 选择较小的值作为行走的步数, 再加 "按下按钮的1"
            dp[0][kidx] = min_step(ring, 0, kidx) + 1
        # 3 在闭区间[1, nk-1] 中遍历, 利用状态转移方程计算dp中的值.
        for i in range(1, nk):
            # 对于 ring中 所有 key[i] 这个字符的索引, 也就是 stat[key[i]], 我们求上一个字符转移到这个字符需要的最少步数.
            # prev_indexes = stat[key[i-1]] = stat["g"] = [0, 6]
            prev_indexes = stat[key[i-1]]
            for j in stat[key[i]]:
                dp[i][j] = min([dp[i-1][x]+min_step(ring, x, j)+1 for x in prev_indexes])

        return min(dp[nk-1])

