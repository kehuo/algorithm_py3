# @File: two
# @Author: Kevin Huo
# @LastUpdate: 3/22/2020 12:42 AM


import json


def sumFourDivisors(nums):
    """
    https://leetcode-cn.com/problems/four-divisors/
    """
    def _cal(bignum):
        # 21 // 2 = 10
        _res = []
        _half_idx = bignum // 2
        for _n in range(2, _half_idx + 1):
            if len(_res) > 2:
                _res = []
                break
            if _n in _res:
                continue
            if bignum % _n == 0:
                shang = bignum // _n
                if _n != shang:
                    _res.append(_n)
                    _res.append(shang)

        return _res

    res = 0
    d = {}
    for i in range(len(nums)):
        n = nums[i]
        if n < 6:
            print("%s too less" % n)
            # 1/ 2/ 3/ 4/ 5 are all unavailable
            d[i] = []
            continue
        possible_res = _cal(n)

        if len(possible_res) == 2:
            res += (n + 1)
            res += sum(possible_res)
            print("n=%s, possible_Res=%s, res=%s" % (n, possible_res, res))
    return res


def sumFourDivisors_v2(nums):
    print("题目开始====================")
    res = 0

    for n in nums:
        if n < 6:
            continue

        BINGO = False
        end = n // 2
        n_sum = 0
        visited = []
        for i in range(2, end):
            if n % i == 0:
                if i == n // i:
                    continue

                if not BINGO:
                    BINGO = True
                    shang = n // i
                    n_sum += sum([1, n, i, shang])

                    visited.extend([i, shang])
                else:
                    if i in visited:
                        continue
                    # 虽然能除尽, 但是之前已经找到因数(在visited里)了, 所以当前n的因数>4, 排除在外
                    break
            if i == end - 1:
                if BINGO:
                    res += n_sum
    return res


def sumFourDivisors_v3(nums):
    """
    quotient = 商
    reminder = 余数

    21 // 2 = 10
    """
    # print("题目开始====================")
    res = 0

    for n in nums:
        if n < 6:
            continue

        BINGO = False
        n_sum = 0
        visited = []
        i = 2
        # print("\n当前n=%s, res=%s" % (n, res))
        while True:
            # print("当前i=%s, n=%s, BINGO=%s, n_sum=%s" % (i, n, BINGO, n_sum))
            if i > n // 2 - 1:
                # 对于 7, 11 这种质数, 这个判断是必要的
                # print("i >= n // 2 = %s, 退出while" % (n//2))
                break

            if n % i != 0:
                i += 1
                continue

            if BINGO:
                if i in visited:
                    i += 1
                    continue
                # print("遇到一个可以整除的i=%s, 但是已有因数%s, 所以退出while" % (i, visited))
                n_sum = 0
                break

            BINGO = True
            shang = n // i
            if shang == i:
                i += 1
                continue
            visited.extend([i, shang])

            n_sum += sum([1, i, shang, n])

            n = n // i
            i += 1
            # print("bingo! 增加后的i=%s, 除以i之后后的n=%s, shang=%s, n_sum=%s" % (i, n, shang, n_sum))

        # 跳出while 循环后, 累加 n_sum
        res += n_sum
    return res


if __name__ == '__main__':
    # [32, 0, 45, 10932]
    with open("./test_data/q2.json", "r", encoding="utf-8") as f:
        tests = json.load(f)

    length = len(tests)
    s = 4
    e = 5
    for j in range(s, e):
        r = sumFourDivisors_v3(tests[j])
        print("结果", r)

