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
    """答案正确, 时间会超时"""
    # print("题目开始====================")
    res = 0

    for k in range(len(nums)):
        n = nums[k]
        # print("第%s个n=%s开始了===================\n" % (k+1, n))
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
                    # print("bingo! i=%s, n=%s, shang=%s, n_sum=%s" % (i, n, shang, n_sum))
                else:
                    if i in visited:
                        continue
                    # print("可惜! 遇到一个可以整除的i=%s, 但是已有因数%s, 所以退出while" % (i, visited))
                    # 虽然能除尽, 但是之前已经找到因数(在visited里)了, 所以当前n的因数>4, 排除在外
                    break
            if i == end - 1:
                if BINGO:
                    res += n_sum
                    # print("恭喜! 当前n=%s有4个因数%s, 可以加到res中. 总结-----------当前n_sum=%s, res=%s" % (n, visited, n_sum, res))
    return res


def sumFourDivisors_v3(nums):
    """
    答案正确, 会在这个测试数据超时:
    [17595,45408,24290,47096,69315,76769,25160,29966, ...]
    quotient = 商
    reminder = 余数

    21 // 2 = 10

    这个版本比v2最主要的区别在于, 我会在每一次得到一个被i整除的时刻, 将循环的最大的右边边界max_limit缩小, 缩小的方式是 max_limit = max_limit // i
    比如 100, 我的初始边界是 100//2 - 1 = 50 - 1 = 49.
    当他遇到i=2可以整除时, 我会把最大边界缩小到 49 // 2 = 24, 这样原本i要遍历到49才能结束循环, 但是由于这里缩小了边界, 只需要遍历到24就可以结束循环了。遍历的数据量整整缩小了一倍.
    """
    # print("题目开始====================")
    res = 0

    for n in nums:
        # print("第%s个新的n=%s开始了=========================\n" % (k+1, n))
        if n < 6:
            continue

        BINGO = False
        n_sum = 0
        visited = []
        i = 2
        max_limit = n // 2 - 1
        while True:
            # print("当前i=%s, n=%s, BINGO=%s, n_sum=%s" % (i, n, BINGO, n_sum))
            if i > max_limit:
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

            max_limit = n // i
            i += 1
            # print("bingo! i=%s, 除以i之后后的n=%s, shang=%s, n_sum=%s" % (i-1, n, shang, n_sum))

        # 跳出while 循环后, 累加 n_sum
        res += n_sum
        # print("\n循环结束! 总结 --- 结束的的i=%s, 除以当前i后的n=%s, res=%s, visited=%s" % (i-1, n, res, visited))
    return res


if __name__ == '__main__':
    # 正确答案 = [32, 0, 45, 10932, 6777290, 135341358, 249058074]
    with open("./test_data/q2.json", "r", encoding="utf-8") as f:
        tests = json.load(f)

    length = len(tests)
    s = 6
    e = 7
    for j in range(s, e):
        r = sumFourDivisors_v2(tests[j])
        print("结果=%s, 数据集长度%s" % (r, len(tests[j])))


