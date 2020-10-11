# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 10/11/2020 10:22 AM


class Solution:
    """
    Pass
    https://leetcode-cn.com/contest/weekly-contest-210/problems/maximum-nesting-depth-of-the-parentheses/
    """
    def maxDepth(self, s: str) -> int:
        res = 0
        curr_depth = 0
        stack = list()
        for c in s:
            if c == "(":
                stack.append(c)
                curr_depth += 1
                res = max(res, curr_depth)
            elif c == ")":
                stack.pop()
                curr_depth -= 1
        return res