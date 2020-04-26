# @File: 3.py
# @Author: Kevin Huo
# @Date: 2020/4/25



"""
https://leetcode-cn.com/contest/season/2020-spring/problems/xun-bao/
3. 寻宝
通过的用户数61
尝试过的用户数217
用户总通过次数61
用户总提交次数548
题目难度Hard
我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。

迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。

要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。

迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。

我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

示例 1：

输入： ["S#O", "M..", "M.T"]

输出：16

解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。 图片.gif

示例 2：

输入： ["S#O", "M.#", "M.T"]

输出：-1

解释：我们无法搬到石头触发机关

示例 3：

输入： ["S#O", "M.T", "M.."]

输出：17

解释：注意终点也是可以通行的。

限制：

1 <= maze.length <= 100
1 <= maze[i].length <= 100
maze[i].length == maze[j].length
S 和 T 有且只有一个
0 <= M的数量 <= 16
0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。
"""

import functools
from typing import List
import collections
import itertools


def minimalSteps(maze: List[str]) -> int:
    mm = len(maze)
    nn = len(maze[0])

    @functools.lru_cache(None)
    def dis(a, b):
        nonlocal mm, nn, maze
        tx, ty = b
        q = collections.deque()
        q.append(a)
        ret = -1
        visited = set()
        while q:
            ret += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                if x == tx and y == ty:
                    # print('dis',a,b,ret)
                    return ret
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if i < 0 or i >= mm or j < 0 or j >= nn:
                        continue
                    if maze[i][j] == '#':
                        continue
                    elif (i, j) not in visited:
                        visited.add((i, j))
                        q.append((i, j))
        return float('inf')

    S = T = None
    M = []
    O = []
    for i, row in enumerate(maze):
        for j, ch in enumerate(row):
            if maze[i][j] == 'S':
                S = (i, j)
            elif maze[i][j] == 'T':
                T = (i, j)
            elif maze[i][j] == 'M':
                M.append((i, j))
            elif maze[i][j] == 'O':
                O.append((i, j))

    @functools.lru_cache(None)
    def dispair(a, b):
        ret = float('inf')
        for o in O:
            ret = min(ret, dis(*sorted([a, o])) + dis(*sorted([b, o])))
        # print('dispair',a,b,ret)
        return ret

    # print(M)
    if len(M) == 0:
        ans = dispair(*sorted([S, T]))
        return ans if ans < float('inf') else -1

    ans = float('inf')
    for choice in itertools.permutations(M):
        tmp = 0
        now = S
        for m in choice:
            tmp += dispair(*sorted([now, m]))
            now = m
        tmp += dis(*sorted)