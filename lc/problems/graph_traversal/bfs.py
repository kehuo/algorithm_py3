# @File: bfs
# @Author: Kevin Huo
# @LastUpdate: 11/12/2020 11:32 PM

import collections


def bfs(lists_arr):
    """
    lists_arr: 以二维数组表示的有向图
    [[1,2], [2,3], [3,4], [4,1], [1,5]]
    """
    def arr2dict(arr):
        """
        输入 [[1,2], [2,3], [3,4], [4,1], [1,5]]
        输出 {1: [2, 5], 2: [3], 3: [4], 4: [1]}
        """
        d = collections.defaultdict(list)
        start = float("inf")
        for v in arr:
            start = min(start, v[0])
            d[v[0]].append(v[1])
        return d, start

    lists, root = arr2dict(lists_arr)
    q = collections.deque([root])
    visited = set()
    visited.add(root)
    while q:
        curr = q.popleft()
        # do something
        print(curr)
        for i in lists[curr]:
            if i not in visited:
                visited.add(i)
                q.append(i)
            else:
                print("%s visited, edge=[%s, %s]" % (i, curr, i))


if __name__ == '__main__':
    # [2,3] , [4, 1], [3, 1]
    tests = [
        [[1,2], [1,3], [2,3]],
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
        [[5, 2], [5, 1], [3, 1], [3, 4], [3, 5]]
    ]
    t = tests[2]
    bfs(t)
