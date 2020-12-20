# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 12/20/2020 10:25 AM


"""https://leetcode-cn.com/contest/weekly-contest-220"""


class Solution:
    """https://leetcode-cn.com/contest/weekly-contest-220/problems/reformat-phone-number/
    通过
    """
    def reformatNumber(self, number: str) -> str:
        arr = []
        for i in number:
            if i == " " or i == "-":
                continue
            arr.append(i)
        n = len(arr)
        c = n // 3
        last = n % 3
        res = []
        if last == 1:
            c -= 1
        # print("arr=%s, n=%s, c=%s, last=%s" % (arr, n, c, last))
        s = 0
        while s < c:
            tmp = "".join(arr[s * 3:(s + 1) * 3])
            res.append(tmp)
            s += 1
        if last == 2:
            res.append("".join(arr[n - 2:]))
        if last == 1:
            res.append("".join(arr[n - 4:n - 2]))
            res.append("".join(arr[n - 2:]))
        res = "-".join(res)
        return res[:-1] if res[-1] == "-" else res




