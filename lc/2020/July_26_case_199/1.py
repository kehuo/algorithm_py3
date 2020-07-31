# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 7/26/2020 10:30 AM


from typing import List


def restoreString(self, s: str, indices: List[int]) -> str:
    res = ""
    l = len(s)
    for i in range(l):
        for n in range(l):
            idx = indices[n]
            if idx == i:
                res += s[n]
                break
    return res


if __name__ == '__main__':
    tests = [
        ["codeleet", [4,5,6,7,0,2,1,3]]
    ]
    t = tests[0]

    r = restoreString(*t)
