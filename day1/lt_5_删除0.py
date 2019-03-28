'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
# ------------***--------------


#以下是有return的实现：
'''
def movezeroes(nums):
	i=0
	count=0
	while i<len(nums):
   		if nums[i]==0:
   			nums.pop(i)
   			i=i-1
   			count=count+1
   		else:
   			pass
   		i=i+1
	for j in range(0,count):
		nums.append(0)

	return nums

t=movezeroes([0,1,2,0,3])
print(t)
'''
# 但是题目要求不要return任何输出，所以按照题目要求，以下是答案，其实就是把最后一行return删掉，因为题目最后目的是判断nums这个列表的内容是否符合要求：
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                i=i-1
                count=count+1
            else:
                pass
            i=i+1
        for j in range(0,count):
            nums.append(0)
        

		
	



                
