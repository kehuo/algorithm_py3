# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 12/6/2020 12:08 PM


class Solution:
    def interpret(self, command: str) -> str:
        """
        https://leetcode-cn.com/problems/goal-parser-interpretation/
        () 和 (al)的区别用 栈实现
        G 遇到就放入结果中
        """
        res = []
        if not command:
            return ""

        stack = []
        for i in command:
            if i == "G":
                res.append(i)
            elif i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) == 3:
                    res.extend("al")
                elif len(stack) == 1:
                    res.append("o")
                stack.clear()
            elif i in ["a", "l"]:
                stack.append(i)
        return "".join(res)
