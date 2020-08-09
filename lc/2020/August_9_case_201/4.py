# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 8/9/2020 10:29 AM


class Solution:
    """
    提交通过
    """
    def makeGood(self, s: str) -> str:

        # length = len(s)
        c = 0
        while len(s[c:]) >= 2:
            # print(s, c)
            x = s[c]
            y = s[c + 1]
            if abs(ord(x) - ord(y)) == 32:
                # print("x=%s, y=%s, s[:c]=%s, s[c+2:]=%s" % (x, y, s[:c], s[c+2:]))
                s = s[:c] + s[c + 2:]
                c = 0
                continue
            # print("current s[c:]=%s" % s[c:])
            if len(s[c:]) < 2:
                break
            c += 1
        return s