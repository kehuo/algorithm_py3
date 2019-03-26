'''https://leetcode-cn.com/problems/two-sum/submissions/
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

# -*- coding: UTF-8 -*-
arr=list(map(int,input('type a list here: ').split()))
line2=input('type a target number here: ')

#arr=list(map(int,line1))
#arr=int,arr)
target=int(line2)
res=[]
print(arr)
print(target)
print('len(arr) ',len(arr),'\n')

if len(arr)<2:
    print('typeError, try again.')
    exit()

for i in range(0,len(arr)):
    for j in range(1,len(arr)-1):
        if arr[i]+arr[j]==target and i!=j:
            res.append(i)
            res.append(j)
            print(res)
        else:
            print('no')
print('final res: ',res)
print('finish')
