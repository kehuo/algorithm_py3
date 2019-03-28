'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
#solution 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        current=""
        for i in range(len(s)):
            index=current.find(s[i])
            if index==-1:
                current+=s[i]
            else:
                if len(current)>max_len:
                    max_len=len(current)
                current=current[index+1:]+s[i]
        if len(current)>max_len:
            max_len=len(current)
        return max_len
        
        
#solution 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin=0
        max_len=0
        for i in range(len(s)):
            if s[i] not in s[begin:i]:
                continue
            else:
                max_len=max(max_len,i-begin)
                begin=s.find(s[i],begin)+1
        max_len=max(max_len,len(s)-begin)
        return max_len