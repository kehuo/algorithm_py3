# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 10/1/2020 12:28 PM


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        todo - 暂时没实现, 目前代码不能运行。 后续再完善
        https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

        举例说明滑动窗口的算法
        s = "pwwkew"
        初始窗口 left, right = 0, 0
        初始子串 child = ""
        当前子串长度 n = len(child) = 0
        初始化最大长度 max_len = 0

        **** Step 1 -- 当遇到第一个字母 "p", 由于子串中不包含，所以可以加入.
        left 不变, right 向右移动一格, 移动后：
        left = 0
        right = 1
        child = "p"
        n = 1
        max_len = max(max_len, n) = 2

        **** Step 2 -- 当遇到第二个字母 "w". 由于child不包含他，所以可以加入:
        left 不变, right向右移动一格, 移动后:
        left = 0
        right = 2
        child = "pe"
        n = 2
        max_len = max(n, max_len) = 2

        **** Step 3 -- 当遇到第三个字母 "w" 时, 由于child已经包含该字母, 所以需要滑动窗口. 具体滑动方法如下：
        #1 - 先移动left, 将其移动到 "上一个 w 出现的索引 + 1 的位置", 也就是刚好不包括上一个 "w" 的地方.
        在这个例子中，上一个 "w" 出现的位置是 1, 所以，将left 移动到 1 + 1 也就是 2 的位置.

        #2 - 再移动right, 将其向右移动一格, 用来包含当前新出现的 "w".

        移动后:
        left = 2
        right = 3
        child = "w"
        n = 1
        max_len =  max(n, max_len) = max(1, 2) = 2

        **** Step 4 - 当遇到第4个字母 "k" 时, 由于 child 不包含, 所以可以加入:
        left 不变, right 向右移动一格. 移动后:
        left = 2
        right = 4
        child  = "wk"
        n = 2
        max_len =  max(n, max_len) = max(2, 2) = 2

        **** Step 5 - 当遇到第5个字母 "e" 时, 由于 child 不包含, 所以可以加入:
        left 不变, right 向右移动一格. 移动后:
        left = 2
        right = 5
        child = "wke"
        n = 3
        max_len =  max(n, max_len) = max(3, 2) = 3

        **** Step 6 - 当遇到第6个字母, 也就是最后一个字母 "w" 时, 由于 child 包含, 所以需要滑动窗口. 具体滑动方法如下：
        #1 - 先移动left, 将其移动到 "上一个 w 出现的索引 + 1 的位置", 也就是刚好不包括上一个 "w" 的地方.
        在这个例子中，上一个 "w" 出现的位置是 2, 所以，将left 移动到 2 + 1 也就是 3 的位置.

        #2 - 再移动right, 将其向右移动一格, 用来包含当前新出现的 "w".
        移动后:
        left = 3
        right = 6
        child = "kew"
        n = 3
        max_len =  max(n, max_len) = max(3, 3) = 3

        由于 right = len(s) 所以程序结束. 返回最终结果 max_len = 3
        """
        n = len(s)
        # d 记录每个已经出现过的字母在 s 字符串中上一次出现的索引, 比如 d={"w": 2} 代表 "w" 上一次出现在 s[2] 处.
        left, right = 0, 0
        d = {}
        max_len = right - left
        while right < n:
            curr = s[right-1]
            if curr in d:
                left = right
            d[curr] = right - 1
            # 无论如何 right 肯定要往右移动一格
            right += 1
            # 最后更新 max_len
            max_len = max(max_len, right - left)
        print(max_len)
        return max_len


if __name__ == '__main__':
    # ans = [3, 3]
    tests = [
        "pwwkew",
        "abcabcbb"
    ]
    t = tests[1]
    solution = Solution()
    solution.lengthOfLongestSubstring(t)
