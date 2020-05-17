# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/17/2020 12:47 AM

"""
https://leetcode-cn.com/contest/weekly-contest-189/problems/rearrange-words-in-a-sentence/

我在这里的学习方式是:
1 先用基本算法实现这个问题. 也就是 v1

2 然后根据基本方法中出现的问题，优化，得出结论：用哪种算法 / 数据结构能优化基本算法. 也就是 v2
"""


class Solution:
    def arrangeWords_v1(self, text: str) -> str:
        """
        已通过 leetcode 提交

        基本方法实现.
        1 将 text 转成数组 t_arr
        2 初始化一个字典 d.
            2.1 d = {1: ["a"], 2: ["of", "oh"], 3: ["yes", "top"], 4: ["good", "book"]}
            2.2 解释: key是单词长度, value 是数组，按text中出现顺序排列
        2 嵌套双层遍历.
            2.1 大循环遍历 t_arr 数组中的每一个单词 word.
            2.2 小循环是在每遇到一个 word 后, 将其放到 d[len(word)]中, 并比较自己和res中单词长度，将自己放在 res 数组的正确位置.

        """
        d = {}
        t_arr = text.split(" ")
        t_arr[0] = t_arr[0].lower()
        # print(t_arr)

        max_word_len = 0
        min_word_len = float("inf")
        # print(min_word_len > 1000000000000)
        t_arr_len = len(t_arr)
        for i in range(t_arr_len):
            word = t_arr[i]
            len_word = len(word)
            if len_word > max_word_len:
                max_word_len = len_word
            if len_word < min_word_len:
                min_word_len = len_word
            if len_word not in d:
                d[len_word] = []
            d[len_word].append(word)
        print(d)
        res = []
        print("min=%s, max=%s" % (min_word_len, max_word_len))
        for n in range(min_word_len, max_word_len + 1):
            if n in d:
                res.extend(d[n])
        res[0] = res[0].title()
        print(res)
        return " ".join(res)


if __name__ == '__main__':
    tests = [
        "Leetcode is cool haha",
        "Keep calm and code on"
    ]
    t = tests[1]

    runner = Solution()
    r = runner.arrangeWords_v1(t)
