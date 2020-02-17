from typing import List
from data_structure.heap import DeepMinHeap

inf = float("inf")


class PrimDeepMinHeap(DeepMinHeap):
    """Greedy Algorithm, a solution for minimum spanning tree problem
       imput: a graph
       output: a tree
    """
    def prior(self, v1, v2):
        return v1[1] < v2[1]


def Prim(G: List[List[int]]) -> List[List[int]]:
    # (prop,weight,self)
    nodes = []
    N = len(G)
    h = PrimDeepMinHeap([])

    T = [None] * N
    for i in range(len(T)):
        T[i] = [inf] * N
        T[i][i] = 0
    for i in range(N):
        n = PrimDeepMinHeap.HeapNode((None, inf, i))
        nodes.append(n)
        h.push(n)
    h.modify(nodes[0], (0, 0, 0))
    while len(h) > 0:
        node = h.pop()
        prop, dist, me = node.value[0], node.value[1], node.value[2]
        nodes[me] = None
        T[prop][me] = dist
        T[me][prop] = dist
        for j, weight in enumerate(G[me]):
            if weight == inf or j == me:
                continue
            if nodes[j] is not None and G[me][j] < nodes[j].value[1]:
                h.modify(nodes[j], (me, G[me][j], nodes[j].value[2]))
    return T


def Prim2(G: List[List[int]]) -> List[List[int]]:
    N = len(G)
    T = [None] * N
    for i in range(len(T)):
        T[i] = [inf] * N
        T[i][i] = 0
    remain = {i: (None, inf) for i in range(N)}
    remain[0] = (0, 0)
    while remain:
        node = min(remain, key=lambda key: remain.get(key)[1])
        prop, dist = remain.pop(node)
        T[prop][node] = dist
        T[node][prop] = dist
        for j, weight in enumerate(G[node]):
            if weight == inf or j == node:
                continue
            if j in remain and G[node][j] < remain[j][1]:
                remain[j] = (node, G[node][j])
    return T


if __name__ == "__main__":
    G = [[0, 3, inf, inf, 6, 5],
         [3, 0, 1, inf, inf, 4],
         [inf, 1, 0, 6, inf, 4],
         [inf, inf, 6, 0, 8, 5],
         [6, inf, inf, 8, 0, 2],
         [5, 4, 4, 5, 2, 0]]

    Ts = [Prim(G), Prim2(G)]
    for T in Ts:
        for row in T:
            print(row)
        print("-" * 20)
