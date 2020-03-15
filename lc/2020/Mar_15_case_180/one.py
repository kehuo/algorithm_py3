# @File: one
# @Author: Kevin Huo
# @LastUpdate: 3/15/2020 10:28 AM


def lucky_numbers(matrix):
    """
    已通过 -- 48ms / 13.6MB
    https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix
    给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

    幸运数是指矩阵中满足同时下列两个条件的元素：

    在同一行的所有元素中最小
    在同一列的所有元素中最大
     

    示例 1：

    输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
    输出：[15]
    解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
    示例 2：

    输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    输出：[12]
    解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
    示例 3：

    输入：matrix = [[7,8],[1,2]]
    输出：[7]
     

    提示：
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5
    矩阵中的所有元素都是不同的
    """
    res = []

    for m in matrix:
        curr_min = min(m)
        # 先找出这一行行中最小项
        for idx in range(len(m)):
            num = m[idx]
            if num > curr_min:
                continue
            # 若 num 也是当前列中的最大项, 则放入 res
            max_col = max([c[idx] for c in matrix])
            if num == max_col:
                res.append(num)
    return res
