# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 12/6/2020 12:08 PM



class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/
        直接掉包, 用最原始的方式
        注意, 如果令 a = bin(10), 那么 a = "0b1010", 所以, 在拼接字符串之前需要先把 "0b" 去掉, 也就是 a[2:]
        """
        if n == 1:
            return 1
        bin_str = []
        for i in range(1, n+1):
            tmp_bin = bin(i)
            bin_str.append(tmp_bin[2:])
        total_str = "".join(bin_str)
        return int(total_str, 2) % (10**9 + 7)
