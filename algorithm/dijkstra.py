# -*- coding: utf-8 -*-

from typing import List
from data_structure.heap import DeepMinHeap

inf = float("inf")


class DijkstraDeepMinHeap(DeepMinHeap):
    def prior(self, v1, v2):
        return v1[1] < v2[1]


def Dijkstra(G: List[List[int]], root: int) -> List[List[int]]:
    assert root < len(G)
    # (prop,weight,self)
    nodes = []
    N = len(G)
    h = DijkstraDeepMinHeap([])

    T = [None] * N
    for i in range(len(T)):
        T[i] = [inf] * N
        T[i][i] = 0
    for i in range(N):
        n = DijkstraDeepMinHeap.HeapNode((None, inf, i))
        nodes.append(n)
        h.push(n)
    h.modify(nodes[root], (root, 0, root))
    while len(h) > 0:
        node = h.pop()
        prop, dist, me = node.value[0], node.value[1], node.value[2]
        nodes[me] = None
        T[prop][me] = G[prop][me]
        T[me][prop] = G[me][prop]
        for j, weight in enumerate(G[me]):
            if weight == inf or j == me:
                continue
            if nodes[j] is not None and G[me][j] + dist < nodes[j].value[1]:
                h.modify(nodes[j], (me, G[me][j] + dist, nodes[j].value[2]))
    return T


def Dijkstra2(G: List[List[int]], root=int) -> List[List[int]]:
    # (prop,weight)
    assert root < len(G)
    N = len(G)
    T = [None] * N
    for i in range(len(T)):
        T[i] = [inf] * N
        T[i][i] = 0
    remain = {i: (None, inf) for i in range(N)}
    remain[root] = (root, 0)
    while remain:
        node = min(remain, key=lambda key: remain.get(key)[1])
        prop, dist = remain.pop(node)
        T[prop][node] = G[prop][node]
        T[node][prop] = G[node][prop]
        for j, weight in enumerate(G[node]):
            if weight == inf or j == node:
                continue
            if j in remain and G[node][j] + dist < remain[j][1]:
                remain[j] = (node, G[node][j] + dist)
    return T


if __name__ == "__main__":
    G = [[0, 3, inf, inf, 6, 5],
         [3, 0, 1, inf, inf, 4],
         [inf, 1, 0, 6, inf, 4],
         [inf, inf, 6, 0, 8, 5],
         [6, inf, inf, 8, 0, 2],
         [5, 4, 4, 5, 2, 0]]

    Ts = [Dijkstra(G, 0), Dijkstra2(G, 0)]
    for T in Ts:
        for row in T:
            print(row)
        print("-" * 20)
