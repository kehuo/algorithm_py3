# @File: 62
# @Author: Kevin Huo
# @LastUpdate: 4/26/2020 7:16 PM


def uniquePaths(m: int, n: int) -> int:
    """
    https://leetcode-cn.com/problems/unique-paths/submissions/

    教程: 知乎
    https://www.zhihu.com/question/23995189/answer/1094101149

    1 定义 dp 二维数组中每一项的含义 -- dp[i][j] 代表机器人走到 (i, j) 时, 一共有多少种不同路径

    2 定义 当前和之前的关系: 因为机器人智能往 右 或者 下 走. 所以, 对于 (i, j), 机器人只有可能
    从 左边(i, j-1) 或者 上边(i-1, j) 处走过来. 所以,
    dp[i][j] == dp[i][j-1] + dp[i-1][j], 代表:
    机器人走到 (i, j) 拥有的路线总数 = 从左边(i, j-1)过来的所有路线总数 + 从上边(i-1, j)过来的所有路线总数

    3 定义基准值 (对于mxn的网格, 贴着网格左边和上边的这2条边上的值, 就是基准值), 因为：
    只要机器人贴着左边的墙, 那么 j 始终等于 0. 那么他只可能从上边走过来, 而不能从左边走过来(因为自己已经是最左边了), 所以
    对于任何 d[i为任意][j=0]:
    dp[0, 1, 2, ..., m-1][0] = 1
    dp[0][0, 1, 2, ..., n-1] = 1

    至此, 3个重要步骤全部定义完毕. 那么 dp[m-1][n-1] 就是我要求的结果, 即根据步骤1的定义:
    dp[m-1][n-1] 就是 "机器人走到第 (m-1, n-1) 这个格子时, 一共有多少种走法"
    """
    # 先创建2维数组
    dp = [[0 for _one in range(n)] for _row in range(m)]
    dp[0] = [1] * n
    for _row in dp:
        _row[0] = 1

    # step 2 -- 根据步骤2定义的规则, 从第二行第2列开始(1, 1), 填充 dp 数组
    for i in range(1, m):
        row = dp[i]
        for j in range(1, n):
            # one  = 左边 + 上边
            one = row[j - 1] + dp[i - 1][j]
            dp[i][j] = one
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # 答案 = [28, 3]
    tests = [
        [7, 3],
        [3, 2]
    ]
    t = tests[1]
    r = uniquePaths(*t)
    print(r)
