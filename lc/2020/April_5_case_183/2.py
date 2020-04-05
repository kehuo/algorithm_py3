def numSteps(s: str) -> int:
    """
    https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
    将二进制表示减到 1 的步骤数
    已通过
    """
    def add_(_sn):
        _s = str(_sn)
        _i = len(_s) - 1
        _idx_0 = 0
        while True:
            if _s[_i] == "1":
                _idx_0 += 1
                # print("i=%s, value=1, idx_0=%s" % (i, idx_0))
                _i -= 1

                if _i >= 0:
                    continue
                else:
                    _idx_0 = -1
                    break
            elif _s[_i] == "0":
                # print("i=%s, value=1, idx_0=%s" % (i, idx_0))
                break

        # 1111 这种没有0的情况
        if _idx_0 == -1:
            # print(10 ** (len(s)))
            return 10 ** (len(_s))
        # 加相对应的值
        # print("idx_0=%s" % idx_0)
        while _idx_0 > 0:
            if _idx_0 == 1:
                _sn += 9
                break
            else:
                _sn += 8 * (10 ** (_idx_0 - 1))
                _idx_0 -= 1
                continue
        # print(sn)

        return _sn
    res = 0

    sn = int(s)
    print(sn)
    while sn > 1:
        # s[-1] == 0 偶数; s[-1] == 1 等于奇数
        # res += 1
        if sn % 2 == 0:
            # 偶数, 需要除以2 (100 除以 2 = 10)
            print("sn=%s, 偶数, 除2得到%s, res+1=%s" % (sn,sn//10, res+1))
            sn //= 10
            res += 1
        elif sn % 2 == 1:
            # 奇数, 需要加 1 (101 + 1 = 110)
            old_sn = sn

            sn = add_(sn)
            print("sn=%s, 奇数, +1得到%s, res+1=%s" % (old_sn, sn, res + 1))
            res += 1

    return res


if __name__ == '__main__':
    tests = [
        "1101",
        "10",
        "1"
    ]

    t = tests[2]
    r = numSteps(t)
    print(r)
