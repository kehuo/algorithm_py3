# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 11/22/2020 10:12 AM


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        https://leetcode-cn.com/contest/weekly-contest-216/problems/smallest-string-with-a-given-numeric-value/
        倒着生成
        n = 5, k = 73
        res = "aaszz"

        从后往前:
        n=5, k=73>26 , 而且 73-26=47>(n-1) 那么res最后一位 = z
        处理完后 n=4, 剩余k=73-26 = 47

        47>26, 且47-26=21>(4-1), 那么res倒数第二位也是z
        处理完后 n=3, 剩余k=21, res="zz"

        n=3, 21-(3-1)-19==0, 所以res倒数第三位=字典序19的字母，也就是s
        处理完后 n=2, 剩余k=2, res="szz"

        n=2, 2-(2-1)-1==0, 所以res倒数第二位=字典序1的字母，即a
        处理完后 n=1, 剩余k=1, res="aszz"
        """
        d = dict(zip(range(1, 27), [chr(i) for i in range(97, 123)]))
        arr = collections.deque()
        while n > 0:
            # 当前位置最大可能的字母 = 当前k - (当前n-1) 后能达到的大字母
            # tmp = 73-4 = 69 如果大于26, 则直接减去26, 否则减去剩下的值.
            tmp = k - (n - 1)
            need_to_minus = 26 if tmp >= 26 else tmp
            curr_char = d[need_to_minus]
            arr.appendleft(curr_char)

            # 减完后 curr_max_char = 73 - 26 = 47
            k -= need_to_minus
            n -= 1
        # print(arr)
        return "".join(arr)
