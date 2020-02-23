def three_v1(num):
    """暴力法 - 答案目前是正确的, 但是输入 797442477 会超时"""
    min_abs = None
    res = None

    n1 = num + 1
    n2 = num + 2
    end = (num//2) + 2
    for i in range(1, end):
        if res is not None:
            if i in res:
                break
        # num+1 可以整除
        if n1 % i == 0:
            tmp1 = n1 // i
            curr_abs1 = tmp1 - i
            if curr_abs1 == 0:
                res = [i, tmp1]
                break
            # 和 min_abs 比较
            if min_abs is None:
                res = [i, tmp1]
                min_abs = curr_abs1
            else:
                if min_abs > curr_abs1:
                    min_abs = curr_abs1
                    res = [i, tmp1]
        if n2 % i == 0:
            tmp2 = n2 // i
            curr_abs2 = tmp2 - i
            if curr_abs2 == 0:
                res = [i, tmp2]
                break
            # 和 min_abs 比较
            if min_abs is None:
                res = [i, tmp2]
                min_abs = curr_abs2
            else:
                if min_abs > curr_abs2:
                    min_abs = curr_abs2
                    res = [i, tmp2]
    return res


if __name__ == '__main__':
    number = 797442477
    # num = 170967091 >> res = [10754, 15898]
    # num = 797442477 >> res = [14, 56960177]
    print(three_v1(number))
