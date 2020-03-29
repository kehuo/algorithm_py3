# @File: 第1节
# @Author: Kevin Huo
# @LastUpdate: 3/28/2020 3:23 PM


"""15.1 节 - 钢条切割问题
1. rec函数 - 自顶向下的递归方法 (很差的方法, 指数级的时间复杂度, 列出来只是为了引出动态规划)
2. 动态规划的2种等价实现:
    2.1 memoized 函数 - 带备忘的 "自顶向下" 法 - (top-down with memoization)
    2.2 bottom_top 函数 - 自底向上法 (bottom-up method)

"""


def rec(p, n):
    """
    自顶向下 - 递归 - CUT-ROD
    该程序每当 n 增加 1, 运行时间可能就要增加 1 倍. 时间复杂度非常高.
    对于 n = 40, 可能要运行 1 个小时才能得到结果

    p: 价格数组
    n: 钢条初始长度

    CUT-ROD(p, n)
    1 if n == 0
    2     return 0
    3 q = -1
    4 for i = to n
    5     q = max(q, p[i] + CUT-ROD(p, n-i))
    6 return q
    """
    if n == 0:
        return 0

    q = -1
    for i in range(0, n):
        q = max(q, p[i] + rec(p, n-i-1))
    return q


def memoized(p, n):
    """
    这里的 memoized 并没有拼写错误, 他是 memo 这个单词的延伸, memo的意思是 "备忘"

    MEMOIZED-CUT-ROD(p, n)
    1 let r[0, 1, ..., n] be a new array
    2 for i = 0 to n
    3   r[i] = -1
    4 return MEMOIZED-CUT-ROD-AUX(p, n, r)

    其中 MEMOIZED-CUT-ROD-AUX 函数定义如下
    MEMOIZED-CUT-ROD-AUX(p, n, r)
    1 if r[n] >= 0
    2     return r[n]
    3 if n == 0
    4     q = 0
    5 else q = -1
    6 for i = 1 to n
    7     q = max(q, p[i] + MEMOIZED-CUT-ROD-AUX(p, n-i, r))
    8 r[n] = q
    9 return q
    """
    r = [-1] * (n + 1)

    def memoized_aux(_p, _n, _r):
        if _r[_n] >= 0:
            return _r[_n]
        if _n == 0:
            _q = 0
        else:
            _q = -1
        for _i in range(0, _n):
            # 这传入的第2个参数是 n-i-1, 而不是伪代码中的n-i, 是因为伪代码的数组索引是从1到n, 而python数组索引是从0到n-1, 所以相比伪代码, 要整体减1
            _q = max(_q, p[_i] + memoized_aux(_p, _n-_i-1, _r))
        _r[_n] = _q
        return _q
    return memoized_aux(p, n, r)


def bottom_top(p, n):
    """
    自底向上法 - 比memoized更简单

    BOTTOM-UP-METHOD(p, n)
    1 let r[0, 1, ..., n] be a new array
    2 r[0] = 0
    3 for j = 1 to n
    4     q = -1
    5     for idx = 1 to j
    6         q = max(q, p[idx] + r[j-idx])
    7    r[j] = q
    8 return r[n]

    一定要注意 python 和 伪代码 在数组索引上的相互转换.
    伪代码中, 数组开始索引是 1
    python中, 数组开始索引是 0
    """
    r = [-1] * (n + 1)
    r[0] = 0

    end = n + 1
    for j in range(1, end):
        q = -1
        for idx in range(0, j):
            # 在这里, q代表"不切的话, 整条长度的价格"
            # p[idx] 表示切的话, 切完后的右半部分, r[j - idx - 1]代表左半部分
            q = max(q, p[idx] + r[j - idx - 1])
        r[j] = q
        print("循环结束r[%s]=%s" % (j, r[j]))
    return r[n]


if __name__ == '__main__':
    tests = [
        [[1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 8]
    ]
    t = tests[0]
    # opt = rec(*t)
    # opt = memoized(*t)
    opt = bottom_top(*t)
    print(opt)
