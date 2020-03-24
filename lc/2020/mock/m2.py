# @File: m2
# @Author: Kevin Huo
# @LastUpdate: 3/24/2020 10:14 PM

from typing import List
import time


def respace(dictionary: List[str], sentence: str) -> int:
    """
    https://leetcode-cn.com/problems/re-space-lcci/

    1 先将dictionary 根据首字母结构化城 dict类型
    ord("a") = 97
    ord("z") = 122

    2 遍历文章 sentence. While True循环, 用2个索引s, e 指向当前搜索的单词开头和结尾.
        2.1 对于每一个字母 sentence[s], 令char = sentence[s], 搜索d, 是否有 d[char]
            2.1.1 若有, 则 s 不变, 令 words = d[char], 遍历所有以 char 为首字母的 word, 看是否有完全匹配的.
                2.1.1.1 对于每个word, 定义一个 delta 变量, 取值范围是 1 <= delta < len(word):
                    2.1.1.1.1 如果从word[1] 直到word[-1] 全部满足 sentence[s + delta] == word[delta], 则说明 "整个 word
                              都包含在 sentence 中, 这个word是 一个在sentence中的完整词", 那么 s = delta + 1, e = s + 1,
                              继续下一轮 while 循环. ，
                    2.1.1.1.2 如果在 delta 从 1 ~ len(word) -1 的过程中, 任何时刻, 发现 sentence[s + delta] != word[delta],
                              则说明这个 word 不存在于 sentence. 这时还有一个判断:
                              2.1.1.1.2.1 若当前word是 d[sentence[s]] 的最后一个word, 那么 s += 1, e = s + 1, res += 1, 并
                                          进行下一轮 while 循环
                              2.1.1.1.2.2 若当前 word 不是最后一个word, 那 delta = 1, 开始遍历下一个word
    """
    d = dict()
    for i in dictionary:
        if i[0] not in d:
            d[i[0]] = []
        d[i[0]].append(i)
    print(d)
    s = 0
    e = 1
    res = 0
    while True:
        time.sleep(1)

        if s == len(sentence) or e == len(sentence):
            break

        char = sentence[s]
        print("s=%s, e=%s, char=%s,  len(sentence)=%s" % (s, e, char, len(sentence)))
        if char not in d:
            print("char=%s 不存在于d中:%s, res+1 =  %s, 直接下一轮while" % (char, list(d.keys()), res+1))
            res += 1
            s += 1
            e += 1
            continue

        # 遍历首字母相同的所有词汇, 找到其中一个
        words = d[sentence[s]]
        if len(words) == 0:
            s += 1
            e = s + 1
            continue
        print("对于首字母char=%s, d中有可以检查的单词: %s" % (char, words))
        for w in enumerate(words):
            print("正在检查第%s个单词%s" % (w[0]+1, w[1]))
            delta = 1
            word_end_idx = len(w[1])
            word = w[1]
            # 遍历一个word的所有字母
            while delta < word_end_idx:
                if sentence[s + delta] == word[delta]:
                    delta += 1
                    continue
                # 已经是d[char]的最后一个word, 没有更多单词可以检查了
                if w[0] == len(words) - 1:
                    s += 1
                    e = s + 1
                    res += 1
                print("%s 不等于 %s, 该单词%s 不合法" % (sentence[s + delta], word[delta], word))
                break
            else:
                # delta 顺利到达word末尾, 全部相同, 符合2.1.1.1.1
                s = delta + 1
                e = s + 1
                # 这个break是为了结束  for w in enumerate(words) 循环, 因为已经找到正确word, 所以不再d[char]中继续找了.
                break

    return res


if __name__ == '__main__':
    tests = [
        [["looked", "just", "like", "her", "brother"], "jesslookedjustliketimherbrother"]
    ]
    t = tests[0]
    rc = respace(*t)
    print(rc)
