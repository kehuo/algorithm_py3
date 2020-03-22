# @File: two
# @Author: Kevin Huo
# @LastUpdate: 3/22/2020 12:42 AM


def sumFourDivisors(nums):
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


if __name__ == '__main__':
    # test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # todo 会超时
    test = [24]
    summary = sumFourDivisors(test)
    print(summary)
