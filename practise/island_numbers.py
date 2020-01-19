def num_islands(grid):
    """
    2020-01-19 未完成 - 研究中
    leetcode - 队列及广度优先搜索
    https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/872/
    """
    res = 0
    if len(grid) == 0:
        return res
    if len(grid[0]) == 0:
        return res

    island_queue = []
    for i in range(len(grid)):

        for j in range(len(grid[i])):
            curr = grid[i][j]
            if curr == "0":
                continue

            # 第一行只看左
            if i == 0:
                if j == 0:
                    # 第一个直接入栈
                    island_queue.append(curr)
                    continue
                if grid[i][j-1] == "1":
                    island_queue.append(curr)

            # 左 ！= 1 且 右 ！= 1
            if (grid[i][j-1] != "1") and (grid[i-1][j] != "1"):
                res += 1
                island_queue = list()
                island_queue.append(curr)

    print(res)
    return res


def main():
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    nums = num_islands(test_grid)


if __name__ == '__main__':
    main()