# @File: 1.py
# @Author: Kevin Huo
# @Date: 2020/4/12

from typing import List

def stringMatching(words: List[str]) -> List[str]:
    res = []

    chang = len(words)
    for i in range(0, chang):
        m = words[i]
        for j in range(chang):
            n = words[j]
            if i == j:
                continue
            if (m in n):
                if m not in res:
                    res.append(m)
            elif (n in m):
                if n not in res:
                    res.append(n)
    print(res)
    return res


if __name__ == '__main__':
    tests = [
        ["mass", "as", "hero", "superhero"]
    ]

    t = tests[0]
    r = stringMatching(t)
