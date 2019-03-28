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
a=[1,2,3]
a=[str(i) for i in a]
a=int(''.join(a))
print(a)
a=a+1
print(a)
a=str(a)
res=list(map(int,a))
print(res)
'''
# 以下是代码实现：

def plusOne(digits):
    digits=[str(i) for i in digits]
    digits=''.join(digits)
    digits=int(digits)
    digits=digits+1
    digits=str(digits)
    digits=list(map(int,digits))
    return digits


