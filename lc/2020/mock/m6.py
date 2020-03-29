# @File: m6
# @Author: Kevin Huo
# @LastUpdate: 3/28/2020 12:17 AM

from typing import List


def minimumLengthEncoding(words: List[str]) -> int:
    """
    3/28/2020
    每日一题 - 单词的压缩编码
    https://leetcode-cn.com/problems/short-encoding-of-words/

    题目描述
    =========
    给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A
    例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
    对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
    那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

    示例
    =======
    输入: words = ["time", "me", "bell"]
    输出: 10
    说明: S = "time#bell#" ， indexes = [0, 2, 5]

    思路
    =======
    从开始维护一个 indexes 数组, 记录 List 中每一个单词的开始索引.
    从开始就维护一个字典d, 每写入一个单词前 和写入一个单词后, 都会对d做几件事.
    1. 写入一个单词前:
        1.1 检查自己的 首字母 是否在 d.keys()中.
            a. 若在, 在 d["首字母"] 这个数组中查询是否有自己.
                a.1 若有, 则不用写入自己, 只需要 indexes.append() 这个匹配到的单词的索引, 直接continue, 下一轮循环
                a.2 若没有, 写入自己, 并在写入后, 对 d 做几件事:
                    A. 遍历自己的每一个字母, 并查看: 以这个当前字母为首字母的 子单词 是否存在于d中.
                        A.1 若存在, 那么什么都不干, continue, 检查当前单词的下一个字母.
                        A.2 若不存在, 将这个字母为首字母的 子单词 写入 d[当前字母], 并 continue, 下一个循环
            b. 若不在, 则做这件事:
                b.1 创建 d[首字母] = []
                b.2 indexes.append(当前S的长度), 其中 "当前S的长度就是 当前单词开始的索引"
                b.1 遍历自己的每一个字母, 并查看: 以这个当前字母为首字母的 子单词 是否存在于d中.
                    b.1.1 若存在, 那么什么都不干, continue, 检查当前单词的下一个字母.
                    b.1.2 若不存在, 将这个字母为首字母的 子单词 写入 d[当前字母], 并 continue, 下一个循环

    变量示例
    ===========
    d = {"t": [("time", 0)],
         "i": [("ime", 1)],
         "m": [("me", 2)],
         "e": [("e", 3), ("ell", 6)],

         "b": [("bell", 5)],
         "l": [("ll", 7), ("l", 8)]
    }

    模拟过程
    =========
    当 w = "time": (初始化 curr_idx = None, write_self = True)
        1. d = {}
        2. 没有 d["t"]
        3. 将 "time" 写入 S >> S = "time#" >> curr_idx = len(S) + 0 = 0 + 0 = 0 >> 并 write_self = True
        4. indexes.append( curr_idx )
        5. 如果 write_self == True >> 遍历 "t" / "i", "m", "e", 分别用这4个字母检查d
            5.1 d["t"] 不存在 >> d["t"] = [] >>  d["t"].append( ("time", len(S) + 0) )
            5.2 d["i"] 不存在 >> d["i"] = [] >> d["i"].append( ("ime", len(S) + 1) )
            5.3 d["m"] 不存在 >> d["m"] = [] >> d["m"].append( ("me", len(S) + 2) )
            5.4 d["e"] 不存在 >> d["e"] = [] >> d["e"].append( ("e", len(S) + 3 )
        # 当前 S = "time#", indexes = [0]

    当 w = "me": (初始化 curr_idx = None, write_self == False)
        1. d = {"t": [], "i": [], "m": [ ("me", 2) ], "e": []}
        2. 有 d["m"] >> 遍历 d["m"] >> d["m"] 中有 "me" >> curr_idx = d["m"]["me"][1] = 2
        3. 不用将 "me" 写入 S
        4. indexes.append( curr_idx ) >> indexes = [0, 2]
        5. 如果 write_self == False >> 不需要遍历 "me" 的每一个字母, 直接continue

        # 当前 S = "time#", indexes = [0, 2]

    当 w = "bell" (初始化 curr_idx = None, write_self = True)
        1. d = {"t": [], "i": [], "m": [], "e": []}
        2. 没有 d["b"]
        3. 将 "bell" 写入 S >> S = "time#bell#" >> curr_idx = len(S) + 0 = 5 + 0 = 5
        4. indexes.append( curr_idx ) >> indexes = [0, 2, 5]
        5. 遍历 "b" / "e" / "l" / "l", 分别用这4个字母检查 d (当前len(S) = 5)
            5.1 d["b"] 不存在 >> d["b"] = [] >>  d["b"].append( ("time", len(S) + 0) )
            5.2 d["e"] 存在 >> d["e"]["ell"] 不存在 >> d["e"].append( ("ell", len(S) + 1) )
            5.3 d["l"] 不存在 >> d["l"] = [] >> d["l"].append( ("ll", len(S) + 2) )
            5.4 d["l"] 存在 >> d["l"]["l"] 不存在 >> d["l"].append( ("l", len(S) + 3) )


    """
    S = ""
    indexes = []
    d = dict()

    for one in enumerate(words):
        w = one[1]
        start = w[0]
        curr_idx = None
        # print("idx=%s, w=%s" % (idx, w))
        # 1 - 2
        if start not in d:
            # 3
            S += w
            S += "#"
            curr_idx = len(S)
            # 4
            indexes.append(curr_idx)

            # 5
            for char in enumerate(w):
                # print("char[0]=%s, char[1]=%s" % (char[0], char[1]))
                if char[1] not in d:
                    d[char[1]] = []
                sub_w = w[char[0]:]
                if sub_w not in [m[0] for m in d[char[1]]]:
                    # sub_w = "time" / "ime" / "me" / "e"
                    # print("%s不在d[%s]中, 当前该字母索引=%s" % (sub_w, char[1], len(S) - len(w) - 1 + char[0]))
                    d[char[1]].append((sub_w, len(S) - len(w) -1 + char[0]))
                else:
                    # todo 假如输入数组 = ["me", "time"], 那么我需要在遇到"time"后, 把 "me" 从 S 中删掉
                    for item in d[char[1]]:
                        # item = ("me", 2)
                        if sub_w == item[0]:
                            # delete_one = ("me", 2)
                            delete_one = item
                            break
                    for word in words:
                        if word == sub_w:
                            # todo 从 S 中把 word 删掉 (但是这样的话, 所有S的索引都得更新, 感觉太麻烦, 准备直接放弃该版本)
                            pass
        else:
            if w not in [m[0] for m in d[start]]:
                S += w
                S += "#"
                curr_idx = len(S)

                indexes.append(curr_idx)

                for char in enumerate(w):
                    if char[1] not in d:
                        d[char[1]] = []
                    sub_w = w[char[0]:]
                    if sub_w not in [m[0] for m in d[char[1]]]:
                        d[char[1]].append((sub_w, len(S) - len(w) -1 + char[0]))
                continue
            for possible in d[start]:
                if w == possible:
                    # possible = ("me", 2), curr_idx = 2
                    curr_idx = possible[1]
                    indexes.append(curr_idx)
                    break
    # print(d)
    # print(S)
    return len(S)


if __name__ == '__main__':
    # answer = [10, 2, 9, 5]
    # todo 如果输入是 ["me", "time"], 那么用v1版本会很麻烦, 甚至根本无法实现, 由于这种输入的原因, 准备写 v2 版本.
    tests = [
        ["time", "me", "bell"],
        ["t"],
        ["time", "me", "ell", "time"],
        ["me", "time"]
    ]
    t = tests[-1]
    res = minimumLengthEncoding(t)
    print(res)
