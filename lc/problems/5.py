# @File: q5
# @Author: Kevin Huo
# @LastUpdate: 3/26/2020 11:29 PM


def longestPalindrome(s: str) -> str:
    """
    https://leetcode-cn.com/problems/longest-palindromic-substring/
    leet code 题库第5题 - 寻找最长回文子串
    """
    res = ""

    def check(sub_str):
        """功能函数 - 检查一个子串是否回文"""
        is_huiwen = True
        str_len = len(sub_str)
        if str_len == 1:
            return True
        # 长度为奇数
        if str_len % 2 == 1:
            mid = str_len // 2
            lidx, ridx = 0, str_len - 1
            while lidx < mid < ridx:
                if sub_str[lidx] != sub_str[ridx]:
                    is_huiwen = False
                    break
                lidx += 1
                ridx -= 1
        return is_huiwen

    return res


if __name__ == '__main__':
    tests = ["aaaa"]
    r = longestPalindrome(tests[0])