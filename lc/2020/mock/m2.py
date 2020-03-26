# @File: m2
# @Author: Kevin Huo
# @LastUpdate: 3/24/2020 10:14 PM

from typing import List

"""
https://leetcode-cn.com/problems/re-space-lcci/
"""


def respace(dictionary: List[str], sentence: str) -> int:
    """
    # todo 最后一个我的结果是10, 但是标准答案是9, 需要再排查...
    1 先将dictionary 根据首字母结构化城 dict类型 (即变量d)

    2 变量和参数解释
    d = {"a": [("apple", 5), {"always", 6}],
         "b": {"banana", 6}, {"book", 4}],
         ...
         "z": [("zoom", 4)]
    }

    p = pointer 指针的缩写
    char = 每个我准备检查的所有单词的首字母, 根据指针p变化而变化, 换句话说, p指到哪, char = sentence[p]
    matched = 当句子和字典的某词完全匹配时, 将这个词的长度, 累加到 matched 上.
    """
    # 1 初始化d
    d = dict()
    for i in dictionary:
        if i[0] not in d:
            d[i[0]] = []
        # (i, len(i)) = ("apple", 5)
        d[i[0]].append((i, len(i)))

    # 2 主函数开始
    p = 0
    matched = 0
    flag = len(sentence)
    while True:
        if p >= flag:
            break
        char = sentence[p]
        if char not in d:
            p += 1
            continue

        # 遍历d[char]
        words = d[char]
        # 这里排序后, 再写下面的循环就会简单. 否则还要维护一个 "max_matched_word_len", 找到所有匹配的词的最长项, 但排序后就不必了
        words.sort(key=lambda x: x[1], reverse=True)
        # has_matched_word 变量主要用来在一次循环的最后, 判断是否需要 p+=1, 如果为True, 说明p已经变过了, 就不用+1了, 为False则+1
        has_matched_word = False
        for w in words:
            # w = ("apple", 5)
            if sentence[p: p + w[1]] == w[0]:
                has_matched_word = True
                matched += w[1]
                # print("幸运!! p=%s, sentence[p: p + w[1]]=%s, w=%s, matched=%s" % (p, sentence[p: p + w[1]], w, matched))
                p += w[1]
                # 这里体现了 words.sort()的好处, 只要找到第一个匹配的词, 这个词必定是长度最长的, 所以后面的短词就不用看了. 直接结束循环
                break
        if not has_matched_word:
            # 如果当前指针指到的字母, 在字典中没有可以匹配的单词, 那么指针前进一位, 检查sentence中的下一个字母
            p += 1
    return flag - matched


def respace_dp(dictionary: List[str], sentence: str) -> int:
    """
    准备使用动态规划思路解答

    opt[i] = 对于sentence中的第i的字母, 如何选择才能使当前结果最优.

    比如:
    dictionary = ["helloiam", "hello", "iamyourbrother"]
    sentence = "helloiamyourbrother"

    对于以上示例, 如果我按照V1版本做, 那么流程如下:
    1. 将dictionary 根据首字母, 格式化成一个字典 d = {"h": ["helloiam", "hello"],
                                                    "i": ["iamyourbrother"]
                                                }
    2. 初始化1个变量, 叫做 matched = 0. 他代表"所有可以从字典中匹配到句子中某个单词" 的所有长度的累加之和.
    3. 用指针 p, 遍历sentence中的每一个字母:
        3.1 当指针指向sentence的第一个字母, 即"h", 我现在发现 d["h"] 有2个可选单词, 按照v1的逻辑, 我选择了最长的 "helloiam".
            # 那么当前 "剩余未识别的句子" 就变成了 "yourbrother", 然后我们将matched变量的值, 累加刚才从字典中识别到的单词 "helloiam" 单词的长度, 也就是8, 所以
              matched += 8
        3.2 由于 "helloiam" 整个单词已经被识别, 所以指针p直接跳到了第 8+1个字母, 也就是第9个字母 "y"上.
        3.3 然后, 程序会去d寻找是否有 "y" 开头的单词, 显然没有. >> 所以 "y" 就被程序认为成了1个 "未识别" 的字母. 指针p向前移动1.
        3.4 p会紧接着看 "y" 后面的字母, 也就是 "o", 显然字典d中也没有 "o"开头的单词, 那么 "0"也属于 "未识别", p向前移动1.
        ...
        3.5 p一直移动到最后一个字母 "r", 显然字典d中也没有 "r" 开头的字母, 所以最后一个字母也算是 "未识别的".
    4. 循环结束. 我们来总结一下, 整个虚幻过程中, 我们一共只有一个单词 "helloiam" 从字典中匹配到了句子里. 而且匹配长度是8.
    5. 因为该题的答案, 是 "没有被识别的字母的长度之和", 所以我们用 sentence 的总长度, 减去 "已识别的总长度", 就等于 "未识别的总长度", 即 res = len(sentence) - matched.
    6. 所以, 按照V1版本的算法, 最终结果是 res = len(sentence) - matched = 19 - 8 = 11

    ##########################################################
    但是实际上最好的答案是11吗???? 显然不是, 最好的答案应该是0. 为什么呢?
    问题出在上面的第3.1
    当我们从 2 个 "h" 开头的单词中做选择时, 如果我们不选择 "最长的 helloiam", 而是选择 "hello", 那么结果将变成:
        # matched += len("hello") = 5
        # 指针 p 跳到第 5+1 = 6个字母, 也就是 "i" 上.
    然后, 3.2 就变成了:
    从字典d中寻找 "i" 开头的单词, 我们看到有一个, 就是 "iamyourbrother", 所以这一步的答案就变成了:
        # matched += len("iamyourbrother"), 也就是 matched += 14 = 5 + 14 = 19
        # 指针 p 发现已经到sentence的末尾了, 没有更多字母可以判断了.
        # 循环结束, 当前答案 res = len(sentence) - matched = 19 -19 = 0
    # todo 这就是为什么V1错误的原因 -- "不能简单的在每次遇到单词时, 都选择最长的那个, 而是要做更多的判断. 而如何做更多的判断, 就是我这个v2版本要优化的地方."

    """
    pass


if __name__ == '__main__':
    # todo 答案 = [7, 17, 63, 7, 0, 9]

    tests = [
        [["looked", "just", "like", "her", "brother"], "jesslookedjustliketimherbrother"],

        [["jxnonurhhuanyuqahjy", "phrxu", "hjunypnyhajaaqhxduu"], "qahurhoharrdjxnonurhhuanyuqahjyppnha"],

        [["wccm", "wiw", "uwwiwcmiiiwmmwicuwu", "mw"],
         "iwiwwwmuiccwwwwwmumwwwmcciwwuiwcicwwuwicuiwciwmiwicwuwwmuimccwucuuim"],

        [["sssjjs", "hschjf", "hhh", "fhjchfcfshhfjhs", "sfh", "jsf", "cjschjfscscscsfjcjfcfcfh",
          "hccccjjfchcffjjshccsjscsc", "chcfjcsshjj", "jh", "h", "f", "s", "jcshs", "jfjssjhsscfc"],
         "sssjjssfshscfjjshsjjsjchffffs"],

        [["ouf", "uucuocucoouoffcpuuf", "pf", "o", "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuu", "cf",
          "cffooccccuoocpfupuucufoocpocucpuouofffpoupu", "opoffuoofpupcpfouoouufpcuocufo", "fopuupco",
          "upocfucuucfucofufu", "ufoccopopuouccupooc", "fffu", "uuopuccfocopooupooucfoufop", "occ", "ppfcuu", "o",
          "fpp", "o", "oououpuccuppuococcpoucccffcpcucoffupcoppoc", "ufc", "coupo", "ufuoufofopcpfoufoouppffofffuupfco",
          "focfcfcfcfpuouoccupfccfpcooup", "ffupfffccpffufuuo", "cufoupupppocou",
          "upopupopccffuofpcopouofpoffopcfcuooocppofofuuc", "oo", "pccc", "oupupcccppuuucuuouocu", "fuop",
          "ppuocfuppff", "focofooffpfcpcupupuuooufu", "uofupoocpf", "opufcuffopcpcfcufpcpufuupffpp", "f", "opffp",
          "fpccopc"],
         "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuufffufffufpccopc"],

        [["frrrbbrrbfrfqqbbbrb", "qr", "b", "rf", "qqbbbbfrqbrrqrffbrqqqbqqfqfrr", "r", "ffqq", "bffbqfqqbrrrf", "fq",
          "qfr", "fr", "rqrrbfbfq", "r", "f", "qbqbrbrbqfqbbbfbbbfbq", "bqqbbbqrbbrf", "f"],
         "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"],

        [["helloiam", "hello", "iamyourbrother"], "helloiamyourbrother"]
    ]
    t = tests[6]
    rc = respace(t[0], t[1].lstrip())
    print(rc)
