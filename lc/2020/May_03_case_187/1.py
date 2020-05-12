# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/3/2020 10:23 AM

from typing import List


def destCity(paths: List[List[str]]) -> str:
    s = []
    e = []
    for i in paths:
        one = i[0]
        two = i[1]
        if one not in s:
            s.append(one)
        if two not in e:
            e.append(two)
    print("s: %s" % s)
    print("e: %s" % e)
    for r in e:
        if r not in s:
            return r


if __name__ == '__main__':
    tests = [
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
        [["B", "C"], ["D", "B"], ["C", "A"]]
    ]
    t = tests[1]
    rr = destCity(t)
    print(rr)
