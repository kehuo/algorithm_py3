# @File: 2.py
# @Author: Kevin Huo
# @Date: 2020/4/18

from typing import List


def numWays(n: int, relation: List[List[int]], k: int) -> int:
    """bfs"""
    class Node(object):
        def __init__(self, value, dest, parent_layer):
            # [1, 4]: value=1, dest=4, layer = self.parent_layer+1
            self.value = value
            self.dest = dest
            self.parent_layer = parent_layer
            self.layer = parent_layer + 1

    d = {}
    for i in relation:
        key, val = i[0], i[1]
        if key not in d:
            d[key] = [val]
        else:
            d[key].append(val)

    q = []
    for one in d[0]:
        node = Node(value=0, dest=one, parent_layer=0)

    curr_path = [0]

    res = []
    while q:
        now = q.pop(-1)
        curr_path.append(now)

        if len(d[now]) == 0:
            res.append(curr_path)
            curr_path.pop(-1)
            continue
        for n in d[now]:
            q.append(n)

