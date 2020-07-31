# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 7/26/2020 10:30 AM


def minFlips(target: str) -> int:
    """
    https://leetcode-cn.com/contest/weekly-contest-199/problems/bulb-switcher-iv/
    """
    if len(target) == 1:
        return 0 if target[0] == 0 else 1

    res = 0
    c = 0
    length = len(target)
    for i in range(length):
        char = target[i]
        if char == "0":

            if c % 2 == 0:
                pass
            else:
                res += 1
                c += 1
        elif char == "1":
            if c % 2 == 0:
                res += 1
                c += 1

    return res


if __name__ == '__main__':
    # 答案 = [3, 0, 5]
    tests = [
        "10111", "00000", "001011101"
    ]
    t = tests[2]
    r = minFlips(t)
