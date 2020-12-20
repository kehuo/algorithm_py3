# @File: KMP
# @Author: Kevin Huo
# @LastUpdate: 12/15/2020 11:55 PM


def naive_str_matcher(s: str, template: str):
    """
    朴素字符串匹配
    找到s 中所有匹配 template 子字符串的起始索引
    因为 template 长度已知, 所以根据 开始索引+长度, 可以定位匹配的整个字符串
    """
    n = len(s)
    m = len(template)
    res = []
    for i in range(0, n-m+1):
        if s[i:i+m] == template:
            # 只记录匹配到的 起始索引 即可.
            res.append(i)
    return res


r = naive_str_matcher("aabbc", "ab")
print(r)
