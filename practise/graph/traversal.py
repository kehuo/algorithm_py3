# @File: dfs_adj_matrix
# @Author: Kevin Huo
# @LastUpdate: 12/11/2020 2:12 AM


def dfs(matrix):
    """邻接矩阵 + 深度优先搜索 实现图遍历
    """
    stack = [0]
    visited = set()
    visited.add(0)
    while stack:
        curr = stack.pop()
        # do something
        print(curr)
        for i, adj in enumerate(matrix[curr]):
            if adj and i not in visited:
                visited.add(i)
                stack.append(i)


from collections import deque


def bfs(linkedlist):
    """bfs + 邻接链表实现"""
    q = deque([0])
    visited = set()
    visited.add(0)
    while q:
        curr = q.popleft()
        # do something
        print(curr)
        for i in linkedlist[curr]:
            if i not in visited:
                q.append(i)
                visited.add(i)


def lot(linklist):
    """广度优先搜索 + 邻接链表 按层遍历"""
    q = deque([0])
    lvl = 0
    visited = set()
    visited.add(0)
    while q:
        lvl += 1
        len_q = len(q)
        print("current level = %s" % lvl)
        for _ in range(len_q):
            curr = q.popleft()
            print(curr)
            for i in linklist[curr]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)


def main():
    G = [
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
    ]
    print("dfs + 邻接矩阵:")
    dfs(G)

    LinkList = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4, 6],
        6: [5]
    }
    print("bfs + 邻接链表:")
    bfs(LinkList)

    print("bfs + 邻接链表 + 按层遍历: ")
    lot(LinkList)


if __name__ == '__main__':
    main()
