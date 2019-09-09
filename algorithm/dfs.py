# -*- coding: utf-8 -*-

""" Input: adjacency matrix of graph G
            initial node i
    DFS, depth first search
    reversed pop order is a solution for topological sorting problem
"""

from typing import List

visited_nodes = set()
push_order, pop_order = [], []


def DFS(G: List[List[int]], i: int) -> None:
    # to make sure G is a square matrix
    for row in G:
        assert len(G) == len(row)

    global push_order, pop_order
    push_order, pop_order = [], []

    stack = []
    stack.append(i)
    push_order.append(i)
    while stack:
        k = stack.pop()
        visited_nodes.add(k)
        pop_order.append(k)
        print(k)
        for j in range(len(G)):
            if G[k][j] == 1 and k != j and j not in visited_nodes and j not in stack:
                # for nodes adjacent to k, that not visited nor in the stack
                stack.append(j)
                push_order.append(j)


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
            DFS(G, i)
            print("push order is", push_order)
            print("pop order is", pop_order)
