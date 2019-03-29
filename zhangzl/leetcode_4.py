'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/27/
题目 - 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
需要注意的特殊情况:
特殊1:
输入: [9]
输出: [1,0]

特殊2:
输入: [9,9]
输出: [1,0,0]

--------------***--------------

'''


#solution 1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        reversed_result=[]
        digits.reverse()
        for i,digit in enumerate(digits):
            num=digit+carry
            carry=num//10
            reversed_result.append(num%10)
            if not carry:
                reversed_result+=digits[i+1:]
                break
        if carry:
            reversed_result.append(carry)
        reversed_result.reverse()
        return reversed_result
        
#solution 2
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                break
            if digits[0]==0:
                digits=[1]+digits
        return digits
        
