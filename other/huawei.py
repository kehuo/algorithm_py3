# @File: huawei
# @Author: Kevin Huo
# @LastUpdate: 5/21/2020 6:52 PM


# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


import sys


def func(n, ch):
    """
    huawei interview test
    
    """
    res = 0
    n = None
    ch = None
    raw_input = sys.stdin.readline().strip().split()
    # print()
    try:
        n = int(raw_input[0])
        ch = str(raw_input[1])
    except Exception as e:
        res = -1

    if n is None:
        res = -1

    if n < 1:
        res = -1

    if ch not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        res = -1
    else:
        # print("real n = %s, type = %s, real ch=%s, type(ch)=%s " % (n,type(n), ch, type(ch)))
        # ch = 1~9
        for i in range(1, n+1):
            str_n = str(i)
            for char in str_n:
                if ch == char:
                    # print("char in str_n=%s" % str_n)
                    res += 1

    return res


if __name__ == '__main__':
    tests = [
        [12, 1]
    ]
    r = func(*tests[0])
    print(r)
