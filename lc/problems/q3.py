# @File: q3
# @Author: Kevin Huo
# @LastUpdate: 3/26/2020 10:36 PM


def lengthOfLongestSubstring(s: str) -> int:
    """
    leetcode 题库第3题 - 无重复字符的最长子串
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

    输入 "abcabcbb"
    输出 3 ("abc")

    # todo 这个题 "dvdf" 发现比较难, 逻辑还需要大幅度修改, 先放着
    """
    max_len = 0
    curr = 0
    visited = []
    for i in s:
        if i not in visited:
            curr += 1
            visited.append(i)
            print("i=%s, curr=%s" % (i, curr))
        else:
            print("%s在, curr=%s" % (i, curr))
            if max_len < curr:
                max_len = curr
            curr = 1
            visited = [i]
    print(curr, max_len)
    return max(max_len, curr)


if __name__ == '__main__':
    # [3, 1, 3, 2, 3]
    tests = ["abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf"]
    r = lengthOfLongestSubstring(tests[4])
    print(r)
