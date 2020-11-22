# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 11/22/2020 10:12 AM


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        https://leetcode-cn.com/contest/weekly-contest-216/problems/ways-to-make-a-fair-array/
        rd[i][0] 代表 nums[i+1:] 中偶数下标的和
        rd[i][1] 代表 nums[i+1:] 中奇数下表的和

        ld[i][0] 代表 nums[:i] 中偶数下标的和
        ld[i][1] 代表 nums[:i] 中奇数下标的和

        nums = [1,2,3,4,5]
        当i=0
        rd[0][0] = nums[1:]偶数下标和 = [2,3,4,5]偶数下标和 = 2+4 = 6
        rd[0][1] = nums[1:]奇数下标和 = [2,3,4,5]奇数下标和 = 3+5 = 8

        ld[0][0] = 0
        ld[0][1] = 0

        rd[0][0]+ld[0][0] != rd[0][1]+ld[0][1]


        i=1
        rd[1][0] = nums[1+1:]偶数下标和 = [3,4,5]偶数下标和 = nums[i:]奇数下标和 = [2,3,4,5]奇数下标和 = rd[1-1][1] = rd[0][1] = 8
        rd[1][0] = nums[1+1:]奇数下标和 = [3,4,5]奇数下标和 =  rd[1-1][0]-nums[i] = 6-2 = 4


        if (i-1)%2==0:
            ld[i][0] = nums[:1] 偶数下标和 = [1]偶数下标和 = ld[i-1][0]+nums[i-1]
            ld[1][1] = ld[1-1][1]
        elif i%2==1:
            ld[1][0] = nums[:1] 偶数下标和 = [1]偶数下标和 = ld[1-1][0]
            ld[1][1] = ld[1-1][1] + nums[i]
        因为i==1, 所以(1-1)%2==0, 所以:
            ld[1][0] = ld[i-1][0]+nums[i-1] = 0 + nums[0] = 1
            ld[1][1] = ld[i-1][1]
        """
        res = 0
        n = len(nums)
        rd = [[0, 0] for _ in range(n)]
        ld = [[0, 0] for _ in range(n)]
        # 初始化rd[0][0] 和 rd[0][1]
        rd[0][0] = sum([nums[x] for x in range(1, n) if x % 2 == 1])
        rd[0][1] = sum([nums[x] for x in range(1, n) if x % 2 == 0])
        # print("nums=%s" % nums)
        # print("rd[0]=%s, ld[0]=%s" % (rd[0], ld[0]))
        if (rd[0][0] + ld[0][0]) == (rd[0][1] + ld[0][1]):
            res += 1
        for i in range(1, n):
            rd[i][0] = rd[i - 1][1]
            rd[i][1] = rd[i - 1][0] - nums[i]
            if (i - 1) % 2 == 0:
                ld[i][0] = ld[i - 1][0] + nums[i - 1]
                ld[i][1] = ld[i - 1][1]
            elif (i - 1) % 2 == 1:
                ld[i][0] = ld[i - 1][0]
                ld[i][1] = ld[i - 1][1] + nums[i - 1]
            # print("被删除的索引i=%s, 被删除数字nums[i]=%s, rd[i]=%s, ld[i]=%s" % (i, nums[i], rd[i], ld[i]))
            if i % 2 == 0:
                if (rd[i][0] + ld[i][0]) == (rd[i][1] + ld[i][1]):
                    res += 1
            elif i % 2 == 1:
                if (rd[i][1] + ld[i][0]) == (rd[i][0] + ld[i][1]):
                    res += 1
        # print("rd=%s" % rd)
        # print("ld=%s" % ld)
        return res