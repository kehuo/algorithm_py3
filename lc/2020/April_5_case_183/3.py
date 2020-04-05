import time


def longestDiverseString(a: int, b: int, c: int) -> str:
    """
    已经提交 leetcode 并通过.
    """
    res = ""

    t = [["a", a], ["b", b], ["c", c]]

    print(t)
    while True:
        # time.sleep(1)
        t.sort(key=lambda x: x[1], reverse=True)
        print("大循环开始, t=%s, res=%s" % (t, res))
        old_res = res
        # bingo = None
        if len(res) < 2:
            for each in t:
                if each[1] <= 0:
                    t.remove(each)
                    # print("%s用光了, 当前t=%s" % (each, t))
            # 从 d中挑剩下最多的, 放入 res
            bingo = t[0][0]
            res += bingo
            t[0][1] -= 1
            continue
        else:
            # 需要检查是否 快乐 "aaa", "bbb"
            # res="abc", len(res) = 3, res[-1] = "c", res[-2] == "b"
            start = 0
            while True:
                print("\n循环开始, start=%s, res=%s t=%s" % (start, res, t))
                # time.sleep(1)

                for each in t:
                    if each[1] <= 0:
                        t.remove(each)
                        print("%s用光了, 当前t=%s" % (each, t))

                if start == len(t):
                    print("end")
                    break

                t.sort(key=lambda x: x[1], reverse=True)
                curr_t = t[start:]
                bingo = curr_t[0][0]
                print("t[start:] = %s, bingo=%s" % (t[start:], bingo))
                if (res[-1] == bingo) and (res[-2] == bingo):
                    # 快乐, 不行
                    print("有快乐, res=%s, bingo=%s" % (res, bingo))
                    start += 1
                    continue
                else:
                    res += bingo
                    t[start:][0][1] -= 1
                    start = 0
                    continue

        if res == old_res:
            break
    print(res, len(res))
    return res


if __name__ == '__main__':
    # answer = ["ccaccbcc", "aabbc", "aabaa", "aabbaaccbbac"]
    tests = [
        [1, 1, 7],
        [2, 2, 1],
        [7, 1, 0],
        [5, 4, 3]
    ]
    test = tests[0]
    r = longestDiverseString(*test)