# -*- coding: utf-8 -*-

from typing import List
from data_structure.union_find import QuickUnion2

inf = float("inf")


def Kruskal(G: List[List[int]]) -> List[List[int]]:
    # (start,end,weight)
    edges = []
    N = len(G)
    T = [None] * N
    for i in range(len(T)):
        T[i] = [inf] * N
        T[i][i] = 0
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if G[i][j] != inf:
                edges.append((i, j, G[i][j]))
    edges.sort(key=lambda edge: edge[2])
    uf = QuickUnion2(N)
    for e in edges:
        start, end, weight = e
        if uf.find(start) != uf.find(end):
            T[start][end] = weight
            T[end][start] = weight
            uf.union(start, end)
        if len(uf) == 1:
            break
    return T


if __name__ == "__main__":
    G = [[0, 3, inf, inf, 6, 5],
         [3, 0, 1, inf, inf, 4],
         [inf, 1, 0, 6, inf, 4],
         [inf, inf, 6, 0, 8, 5],
         [6, inf, inf, 8, 0, 2],
         [5, 4, 4, 5, 2, 0]]

    Ts = [Kruskal(G)]
    for T in Ts:
        for row in T:
            print(row)
        print("-" * 20)
