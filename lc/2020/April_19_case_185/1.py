# @File: 1.py
# @Author: Kevin Huo
# @Date: 2020/4/19


def reformat(s):
    # ord a-z = 97-122.   ord 1-9 = 48-57
    d = {"num": [], "char": []}
    for i in s:
        if ord(i) in range(97, 123):
            d["char"].append(i)
        elif ord(i) in range(48, 58):
            d["num"].append(i)
    ln = len(d["num"])
    lc = len(d["char"])
    if abs(lc - ln) > 1:
        return ""
    # 大的取
    res = ""
    if ln >= lc:
        # 先num
        while d["num"]:
            res += d["num"].pop()
            print("加了一个num, d[num]=%s, res=%s" % (d["num"], res))
            while d["char"]:

                res += d["char"].pop()
                print("加了一个char, d[char]=%s, res=%s" % (d["char"], res))
                break
    else:
        while d["char"]:
            res += d["char"].pop()
            while d["num"]:
                res += d["num"].pop()
                break
    return res


if __name__ == '__main__':
    tests = [
        "a0b1c2d"
    ]
    t = tests[0]
    r = reformat(t)
    print(r)