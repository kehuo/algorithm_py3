# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 11/15/2020 1:21 AM


"""
https://leetcode-cn.com/contest/weekly-contest-215
"""


class OrderedStream:
    """
    https://leetcode-cn.com/contest/weekly-contest-215/problems/design-an-ordered-stream/
    """
    def __init__(self, n: int):
        self.p = 1
        self.d = collections.defaultdict(str)

    def insert(self, id: int, value: str) -> List[str]:
        self.d[id] = value
        res = []
        if not self.d[self.p]:
            return res

        # 找到最长的从self.p开始的连续id串
        while True:
            if self.d[self.p]:
                res.append(self.d[self.p])
                self.p += 1
                continue
            break
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)