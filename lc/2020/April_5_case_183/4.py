from typing import List
import time


def stoneGameIII(stoneValue: List[int]) -> str:
    def _opt(_self_score, _other_score, _start, _arr):
        """
        https://leetcode-cn.com/problems/stone-game-iii/solution/xian-shou-de-zhuan-hua-by-zuo-ni-ai-chi-de-tang-se/

        选择方案:
        在 _self_score 所有的3种可选方案中, 选择其中一个, 使得:
        (_self_score + 选中方案新增的 score) > max((_other_score + 另一个人3种方案的dense))

        流程
        ===========
        开始, start = 0
        假设 _arr = stoneValue[start:] = [1, 2, 3, -1, -2 ,-3, 7]
        假设 A 是 self, B 是 other
        sa = 0
        sb = 0
        start = 0

        diff = {"方案1": None, "方案2": None, "方案3": None}
        Alice的3种方案如下:

        1. A 选 _arr[0] --> sa = 0 + 1 = 1 --> start = 0 + 1 = 1:
            B 从 start=1 的索引开始选
            1.1 B 选 _arr[1] --> sb = sb + 2 = 0 + 2 = 2
            1.2 B 选 _arr[1] 和 _arr[2] --> sb = sb + (2 + 3) = 0 + 5 = 5
            1.3 B 选 _arr[1] 和 _arr[2] 和 _arr[3] --> sb = sb + (2 + 3 + -1) = 0 + 4 = 4
            ##########
            max(B) = 5 --> sa < max(B[方案1]) -->
            diff[方案1] = (sa - max(B[方案1])) = 1 - 5 = -4

        2. A 选 _arr[0] 和 _arr[1] --> sa = sa + (1 + 2) = 0 + 3 = 3 --> start = 0 + 2 = 2:
            2.1 B 选 _arr[2] --> sb = sb + 3 = 0 + 3 = 3
            2.2 B 选 _arr[1] 和 _arr[2] --> sb = sb + (3 + -1) = 0 + 2 = 2
            2.3 B 选 _arr[1] 和 _arr[2] 和 _arr[3] --> sb = sb + (3 + -1 + -2) = 0 + 0 = 0
            ##########
            max(B) = 3 --> sa == max(B[方案2])
            diff[方案2] = (sa - max(B[方案2])) = 3 - 3 = 0

        3. A 选 _arr[0] 和 _arr[1] 和 _arr[2] --> sa = sa + (1 + 2 + 3) = 0 + 6 = 6 --> start = 0 + 3 = 3:
            3.1 B 选 _arr[3] --> sb = sb + -1 = 0 + -1 = -1
            3.2 B 选 _arr[3] 和 _arr[4] --> sb = sb + (-1 + -2) = 0 + -3 = -3
            3.3 B 选 _arr[3] 和 _arr[4] 和 _arr[5] --> sb = sb + (-1 + -2 + -3) = 0 + -6 = -6
            ##########
            max(B) = -1 --> sa > max(B[方案3]) -->
            diff[方案3] = (sa - max(B[方案3])) = 3 - (-1) = 4

        比较 diff 字典中的3个结果, 选择最大的一个, 即 diff[方案3]:
        alice 选择 _arr[0] 和 _arr[1] 和 _arr[2] --> sa = 6 --> start = start + 3 = 0 + 3 = 3
        返回 sa = 6, start = 3
        """
        if len(_arr) == 1:
            return _self_score + _arr[0], _start + 1
        # _arr = _raw_arr[_start:]
        print("\n####进入opt函数,_start=%s, _arr=%s, self_score=%s, other_score=%s" % (_start, _arr, _self_score, _other_score))
        _opt_self_score = None
        _opt_self_start_idx = 0
        _max_diff = None

        # _end_self = _start + 1
        _end_self = 1
        _count_self = 0
        _max_other_list = []
        while True:
            _count_self += 1
            if _end_self > len(_arr) or _count_self > 3:
                print("break. _end_self=%s, _count_self=%s" % (_end_self, _count_self))
                break
            print("self循环开始, _end_self=%s, _arr[:_end_self]=%s, _count_self=%s, _opt_self_score=%s" % (
                _end_self, _arr[:_end_self], _count_self, _opt_self_score))
            _tmp_self_score = _self_score + sum(_arr[:_end_self])
            print("self方案%s 的 tmp_score=%s" % (_count_self, _tmp_self_score))

            # bob  从 arr[_end_self:_end_other] 中计算3种方案的 _tmp_other_score
            _end_other = _end_self + 1
            _count_other = 0
            _max_other = None

            while True:
                _count_other += 1
                if _end_other > len(_arr) or _count_other > 3:
                    print("    other break. _end_other=%s, _count_other=%s" % (_end_other, _count_other))
                    break

                _tmp_other_score = _other_score + sum(_arr[_end_self:_end_other])

                if _max_other is None:
                    _max_other = _tmp_other_score
                    _max_other_list.append(_max_other)
                    # print("   other第%s次方案, _max_other为none, 所以直接赋值, _max_other=%s" % (_count_other, _max_other))
                else:
                    if _max_other < _tmp_other_score:
                        _max_other = _tmp_other_score
                        _max_other_list.append(_max_other)
                print(
                    "    other方案%s 的_end_other=%s, _arr[_end_self:_end_other]=%s, tmp_other_score=%s + %s=%s, _max_other=%s" % (
                        _count_other, _end_other, _arr[_end_self:_end_other], _other_score, sum(_arr[_end_self:_end_other]), _tmp_other_score, _max_other
                    ))
                _end_other += 1

            if _count_other - 1 == 0:
                if _max_other is None:
                    _max_other = _max_other_list[-1]
            # B 的3种方案全部完成, 用sa - max(B), 结果写入 _max_diff
            print("    目前other %s 种方案全部完成. _max_other=%s, _tmp_self_score=%s" % (_count_other - 1, _max_other, _tmp_self_score))
            if _max_diff is None:
                _max_diff = _tmp_self_score - _max_other
                print("    在other的方案%s中, _max_diff=None, _tmp_self_score=%s, _max_other=%s, 直接赋值给_max_diff=%s" % (
                    _count_other - 1, _tmp_self_score, _max_other, _max_diff
                ))

                if _opt_self_score is None:
                    _opt_self_score = _tmp_self_score
                    _opt_self_start_idx = _end_self
                    print("    在other方案%s中, 直接将_tmp_self_score赋值给 _opt_self_score=%s" % (_count_other -1 , _opt_self_score))
            else:
                print("max_diff不为None, =%s" % _max_diff)
                if _max_diff < (_tmp_self_score - _max_other):
                    _old_max_diff = _max_diff
                    _max_diff = (_tmp_self_score - _max_other)
                    # 在更新 opt_self时, 一定要记录2个值, 1是score, 二是最优解对应的_end_self, 因为最后要更新并返回 _start值。
                    _opt_self_score = _tmp_self_score
                    _opt_self_start_idx = _end_self
                    print("    更新_max_diff中!!!旧max_diff=%s,  新_max_diff=%s, (_tmp_self_score - _max_other) = (%s - %s) = %s, _opt_self_score=%s" % (
                        _old_max_diff, _max_diff, _tmp_self_score, _max_other, (_tmp_self_score - _max_other), _opt_self_score
                    ))
            _end_self += 1
        _self_score = _opt_self_score if _opt_self_score is not None else _self_score
        _start += _opt_self_start_idx
        print("####opt函数结束, _opt_self_start_idx=%s, _self_score=%s, _other_score=%s, _start=%s" % (_opt_self_start_idx, _self_score, _other_score, _start))
        return _self_score, _start

    # 主函数
    sa = sb = 0
    start = 0
    while True:
        time.sleep(1)
        print("$$$$$$$$$$$$$$主循环开始, sa=%s, sb=%s, start=%s" % (sa, sb, start))
        if start >= len(stoneValue) - 1:
            break

        curr_array = stoneValue[start:]
        print(curr_array)
        sa, start = _opt(_self_score=sa, _other_score=sb, _start=start, _arr=curr_array)
        print("opt_Alice结束, sa=%s, start=%s, 下个人的arr=%s" % (sa, start, stoneValue[start:]))

        curr_array = stoneValue[start:]
        sb, start = _opt(_self_score=sb, _other_score=sa, _start=start, _arr=curr_array)
        print("Bob opt 结束, sb=%s, start=%s, 下个人的arr=%s" % (sb, start, stoneValue[start:]))
    if sa > sb:
        res = "Alice"
    elif sa < sb:
        res = "Bob"
    else:
        res = "Tie"
    print(res)
    return res


def stoneGameIII_dp(stoneValue: List[int]) -> str:
    """
    动态规划思路

    根据<算法导论>第15章, 动态规划有2种方式:
    1 自底向上的动态规划
    2 自顶向下, 但是带 "备忘"功能的 动态规划.

    传统的 "递归" 解法, 就是自顶向下. 但是递归方式不带备忘, 但是动态规划是 "带备忘的", 可以避免大量的重复计算.
    "关于自顶向下带备忘的动态规划", 详情可以参考该项目下 算法导论/第四部分/ 目录下第15章 section.py 的 memoized 函数.

    这个题就打算采用 "自顶向下的带备忘的动态规划"

    思路, 用 dp 数组, 记录 每个可选的子数组的最优解. 对于一个数组 stoneValue:
    假设 n 代表数组的长度, 即 n = len(stoneValue)
    所以, stoneValue[n-1] 就是 stoneValue 数组的最后一项, 即 stoneValue[-1]
    1. (动态规划的基准情况) 如果子数组只有 stoneValue 的最后一项, 那么你只能选它, 所以 dp[n-1] = stoneValue[-1]

    2. 对于其他的 i:
    在写出递推公式之前, 我先定义 d[i] 代表 "从 stoneValue 数组的第 i 项 到最后一项 的子数组中, 的最优解."

    所以, 当 i = n-1 时, dp[i] = dp[n-1] = stoneValue[-1]
    当 0 <= i < n-1 时, dp[i] = sum{i, n} - min{dp[i + 1], dp[i + 2], dp[i + 3]}
    本题的目标 -- 判断 dp[0] 和 (sum(stoneValue) - dp[0]) 的大小. (因为题目说明Alice 必须先拿, 所以 dp[0] = Alice)
    """
    n = len(stoneValue)

    # n + 3的原因, 是避免 dp[i+2] 和 dp[i+2] 的 IndexError
    dp = [0] * (n + 3)
    current_sum = 0
    for i in range(n-1, -1, -1):
        # 倒序
        current_sum += stoneValue[i]
        if i == n - 1:
            dp[i] = stoneValue[-1]
            continue

    # 由于比赛规定Alice必须先拿, 所以 dp[0] 肯定是 Alice, 所以 Bob的分数 = 总分 - Alice的分数 = sum(stoneValue) - dp[0]
    # 即 score_Alice = dp[0]
    # score_Bob = sum(stoneValue) - dp[0]
    score_Alice = dp[0]
    score_Bob = current_sum - dp[0]
    print(dp)
    if score_Alice == score_Bob:
        print("tie")
        return "Tie"
    elif score_Alice > score_Bob:
        print("alice")
        return "Alice"
    elif score_Alice < score_Bob:
        print("bob")
        return "Bob"


if __name__ == '__main__':
    # todo 对于测试用例 [-1, -2, -3] 来说, 我的v1版本函数逻辑其实是错的, 需要完全重写, 这道题我的v1思路, 是错的.
    # 2020/4/5 注释 - v2版本用动态规划, 提交leetcode已经通过 700ms 用时
    # answer = ["Bob", "Tie", "Alice", "Tie"]
    tests = [
        [1, 2, 3, 7],
        [1, 2, 3, 6],
        [1, 2, 3, -1, -2, -3, 7],
        [-1, -2, -3]
    ]
    # dp数组:
    # [
    #   [6, 12, 10, 7],
    #   [6, 11, 9, 6]
    # ]
    t = tests[3]
    r = stoneGameIII_dp(t)
