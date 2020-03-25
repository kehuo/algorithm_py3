# @File: m2
# @Author: Kevin Huo
# @LastUpdate: 3/24/2020 10:14 PM

from typing import List


def respace(dictionary: List[str], sentence: str) -> int:
    """
    https://leetcode-cn.com/problems/re-space-lcci/

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


if __name__ == '__main__':
    # todo 答案 = [7, 17, 63, 7, 0, 9]
    # todo 最后一个我的结果是10, 但是标准答案是9, 需要再排查...
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
         "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"]
    ]
    t = tests[5]
    rc = respace(t[0], t[1].lstrip())
    print(rc)
