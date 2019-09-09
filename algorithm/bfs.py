# -*- coding: utf-8 -*-

""" Input: adjacency matrix of graph G
            initial node i
    BFS, breadth first search
"""

from typing import List

visited_nodes = set()
queue_order = []


def BFS(G: List[List[int]], i: int) -> None:
    # to make sure G is a square matrix
    for row in G:
        assert len(G) == len(row)

    global queue_order
    queue_order = []

    queue = []
    queue.append(i)
    while queue:
        k = queue.pop(0)
        visited_nodes.add(k)
        queue_order.append(k)
        print(k)
        for j in range(len(G)):
            if G[k][j] == 1 and k != j and j not in visited_nodes and j not in queue:
                # for nodes adjacent to k, that not visited nor in the queue
                queue.append(j)


if __name__ == "__main__":
    """
    0-1  4-5
    |    |
    2-3  6
    """
    G = [[1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 1]]
    trees = 0
    for i in range(len(G)):
        if i not in visited_nodes:
            trees += 1
            print("tree number {} start".format(trees))
            BFS(G, i)
            print("queue order is", queue_order)
