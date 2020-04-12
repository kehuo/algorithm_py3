# @File: 3.py
# @Author: Kevin Huo
# @Date: 2020/4/12

from typing import List


def entityParser(text: str) -> str:
    """
    https://leetcode-cn.com/problems/html-entity-parser/

    # 用栈stack 实现 遇到 & 入栈, 遇到; 出栈 (这是大概的思路)
    """
    special_map = {"quot": "\"",
                   "apos": "'",
                   "amp": "&",
                   "gt": ">",
                   "lt": "<",
                   "frasl": "/"
                   }

    # stack["&"] = [前面是否有&, 这个&的索引(若没有默认为None)]
    stack = {"&": [False, None], "w": ""}
    res = ""

    lt = len(text)
    for i in range(lt):
        c = text[i]

        if c == "&":
            if stack["&"][0] is True:
                print("c=&, stack[&] is True")
                sub_str = "&" + stack["w"]
                res += sub_str
            else:
                stack["&"] = [True, i]
                continue

        # 遇到不是 & 的字符
        else:
            # 最普通的字符, stack中没有&, 不需要做任何判断
            if stack["&"][0] is False:
                res += c
                continue

            # 遇到分号, 需要判断是否开始转义
            if c == ";":
                # 举例: stack["w"] ="amp", sub_str = "&"
                if stack["w"] in special_map.keys():
                    sub_str = special_map[stack["w"]]
                    res += sub_str
                    # 清空stack
                    stack = {"&": [False, None], "w": ""}
                    continue

                # text = "&aaaaa;" (这种应该不会发生, 但是理论上确实有这种text的情况)
                # 如果真有这种情况, 那么 "&aaaaa;" 已经不可能再匹配到任何一个需要转换的字符, 所以也需要清空stack
                else:
                    sub_str = "&" + stack["w"] + ";"
                    res += sub_str
                    # 清空stack
                    stack = {"&": [False, None], "w": ""}
                    continue
            else:
                # c既不是&也不是分号, 但是 stack中有 &, 所以需要判断是否清空 stack
                # 假如 text = "&amkevin", 那么遇到k的时候, 就要清空stack了
                curr_str = stack["w"] + c
                # 如果是, 那么继续保持stack
                can_meet = False
                for special_one in special_map:
                    if curr_str == special_one[:len(curr_str)]:
                        # 将c放入stack["w"]
                        stack["w"] += c
                        can_meet = True
                        # 退出这个检查的小循环
                        break
                    else:
                        continue
                if can_meet is False:
                    # 清空stack, 写入res
                    sub_str = "&" + stack["w"] + c
                    res += sub_str
                    stack = {"&": [False, None], "w": ""}
    print(res)
    return res


if __name__ == '__main__':
    tests = [
        "&amp; is an HTML entity but &ambassador; is not.",
        "and I quote: &quot;...&quot;",
        "Stay home! Practice on Leetcode :)",
        "x &gt; y &amp;&amp; x &lt; y is always false",
        "leetcode.com&frasl;problemset&frasl;all"
    ]
    t = tests[4]
    r = entityParser(t)
