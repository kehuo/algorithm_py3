# @File: four
# @Author: Kevin Huo
# @LastUpdate: 3/15/2020 10:29 AM


def func(m, n):
    """
    C 下面=m, 上面=n
    """
    res, fenmu = None, None

    loop_end = n
    for i in range(0, loop_end):
        if i == 0:
            res = m
            fenmu = n
        else:
            res *= m
            fenmu *= n
        m -= 1
        n -= 1
    return res // fenmu


def maxPerformance(n, speed, efficiency, k):
    """
    https://leetcode-cn.com/problems/maximum-performance-of-a-team/

    思路:
    1. 将 speed 和 efficiency 2个表合并到一起 total, 方便后续操作.
    2. 从 total 中计算出: 只有1个工程师时, 效率值最高的那个男子
    3. 记录以下几个变量:
        我们定义 p = A x B, 其中
        p = 题目中定义的团队表现值 performance
        A = 已经被选择的工程师的 speed 之和, 即p的第一个乘法因子
        B = 已经被选择的工程师的 效率最低的值, 即p的第二个乘法因子
        curr_max_p = 当前已经选择的工程师的团队表现值

        total = [(speed[0], efficiency[0]), (speed[1], efficiency[1]), ... (speed[n-1], efficiency[n-1])]
        res = 一个列表, 将已经选中的工程师, 从total中pop出来, 并放入res

    4. 流程:
        4.1 遍历一个 while True 循环, 当 len(res) == k 时停止循环
        4.2 在每次循环时, 遍历total中的每一项:
            4.2-a tmp_A = A + 当前工程师的speed
            4.2-b tmp_B = min(B, 当前工程师的efficiency)
            4.2-c tmp_p = tmp_A * tmp_B
            4.2-d 判断 tmp_p 是否大于 curr_max_p:
                若大于, 则做以下事:
                    <1> 将当前工程师从 total 中pop出来, 放入res
                    <2> 将 tmp_A 的值累加到 A 上面, 即 A += tmp_A
                    <3> 将 tmp_B 赋值给 B, 即 B = tmp_B
                    <4> 将 tmp_p 的值赋给 curr_max_p, 即 curr_max_p = tmp_p
                    <5> continue, 下一轮while循环
                若小于等于:
                    直接continue 下一轮循环
    """
    A = 0
    B = 0
    curr_max_p = 0
    max_individual_p = None

    res = []
    total = []
    for i in range(n):
        total.append((speed[i], efficiency[i]))
        if i == 0:
            max_individual_p = {"p": speed[i] * efficiency[i],
                                "i": i,
                                "speed": speed[i],
                                "efficiency": efficiency[i]}
        else:
            tmp = speed[i] * efficiency[i]
            if max_individual_p["p"] < tmp:
                max_individual_p["p"] = tmp
                max_individual_p["i"] = i
                max_individual_p["speed"] = speed[i]
                max_individual_p["efficiency"] = efficiency[i]
    # todo 这里需要修改, 最后一个测试用例证明 -- 第一个选p最大的工程师并没有卵用, 需要逐个比较.
    first_engineer = total.pop(max_individual_p["i"])
    res.append(first_engineer)

    A = max_individual_p["speed"]
    B = max_individual_p["efficiency"]
    curr_max_p = max_individual_p["p"]
    still_has_better_engineer = True
    while len(res) < k:
        if still_has_better_engineer is False:
            break
        print("\n循环开始, total=%s" % total)
        print("res=%s, p=%s, A=%s, B=%s" % (res, curr_max_p, A, B))
        while len(total) > 0:
            larger_curr_loop = []
            for idx in range(len(total)):
                one = total[idx]
                tmp_A = A + one[0]
                tmp_B = min(B, one[1])
                tmp_p = tmp_A * tmp_B

                if tmp_p > curr_max_p:
                    print("先放入 larger_curr_loop, tmpA=%s, tmpB=%s, tmp_p=%s" % (tmp_A, tmp_B, tmp_p))
                    larger_curr_loop.append(
                        {"tmp_A": tmp_A,
                         "tmp_B": tmp_B,
                         "tmp_p": tmp_p,
                         "one": one}
                    )

            # 如果larger_curr_loop不为空, 则选出 larger_curr_loop 中最大的一项, 放入 res, 并从 total中移除
            if len(larger_curr_loop) > 0:
                best_engineer = max(larger_curr_loop, key=lambda x: x["tmp_p"])

                print(best_engineer)
                res.append(best_engineer["one"])
                total.remove(best_engineer["one"])

                A = best_engineer["tmp_A"]
                B = best_engineer["tmp_B"]
                curr_max_p = best_engineer["tmp_p"]
            else:
                still_has_better_engineer = False
            break
    print("最后\n res=%s, p=%s, A=%s, B=%s" % (res, curr_max_p, A, B))
    return curr_max_p


if __name__ == '__main__':
    tests = [
        {"n": 6, "speed": [2, 10, 3, 1, 5, 8], "efficiency": [5, 4, 3, 9, 7, 2], "k": 2},
        {"n": 6, "speed": [2, 10, 3, 1, 5, 8], "efficiency": [5, 4, 3, 9, 7, 2], "k": 3},
        {"n": 3, "speed": [2, 8, 2], "efficiency": [2, 7, 1], "k": 2},
        {"n": 6, "speed": [10, 5, 1, 7, 4, 2], "efficiency": [2, 1, 1, 1, 7, 3], "k": 6}
    ]

    all_res = []
    for test in tests:
        print("测试###############Start###################")
        p = maxPerformance(**test)
        all_res.append(p)
        print("测试结束 ################################\n")
    # 正确答案: 60, 68, 56, 32
    print(all_res)
