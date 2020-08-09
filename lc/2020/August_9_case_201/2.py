# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 8/9/2020 10:29 AM


class Solution:
    def mymap(self, single):
        return "1" if single == "0" else "0"

    def cal_invert(self, x):
        """
        x : str
        input = "011"
        output = "100"
        """
        arr = []
        for i in x:
            arr.append(i)
        res = list(map(self.mymap, arr))
        return "".join(res)

    def findKthBit(self, n: int, k: int) -> str:
        if n == 0:
            return "0"
        s = "0"
        for _ in range(n - 1):
            old_s = s
            s += "1"
            s += self.cal_invert(old_s)[::-1]
        return s[k - 1]