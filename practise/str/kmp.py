# @File: kmp
# @Author: Kevin Huo
# @LastUpdate: 12/16/2020 12:02 AM


from typing import List


def compute_prefix_func(template: str):
    m = len(template)
    res = [None] * (m-1)
    res[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and template[k+1] != template[q]:
            k = res[k]
        if template[k+1] == template[q]:
            k += 1
        res[q] = k
    return res


def kmp(s: str, template: str) -> List:
    """
    tmp 算法 字符串模式匹配
    """
    n = len(s)
    m = len(template)
    pre = compute_prefix_func(template)
    res = []
    q = 0
    for i in range(n):
        while q>0 and template[q+1] != s[i]:
            q = pre[q]
        if template[q+1] == s[i]:
            q += 1
        if q == m:
            res.append(i-m)
    return res


T = "aabbaaba"
P = "abba"
r = kmp(T, P)
print(r)

