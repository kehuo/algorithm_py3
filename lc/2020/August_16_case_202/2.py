# @File: 2
# @Author: Kevin Huo
# @LastUpdate: 8/16/2020 1:07 PM


class Solution:
    def minOperations(self, n: int) -> int:
        """
        https://leetcode-cn.com/contest/weekly-contest-202/problems/minimum-operations-to-make-array-equal/
        已经通过提交

        若n为偶数:
        1 - 那么一共有 n/2 组数字. 比如 [1, 3, 5, 7] 中n=4, 一共4/2=2组数字： 3/5 和 1/7
        2 - 找到"中间的2项", 也就是 arr[n/2 - 1] 和 arr[n/2]
        3 - 求均值, 即 mid = (arr[n/2 - 1] + arr[n/2]) / 2 = (arr[1] + arr[2]) / 2 = (3+5)/2 = 8/2 = 4
        4 - 从i=0开始算, 比如arr[0]= 1, 他要达到 "中间值mid" 需要多少次操作 >> 4-1 = 3 >> 一共需要3次操作
        5 - 当i=1时, arr[1] 达到中间值需要 4-3=1次操作.
        6 根据上面规律可以发现, 对于一个i, 如果他小于n/2 (比如对于n=4, 我们只看0和1，因为只有0和1小于2), 那么索引为i的这组数字要达到相等，需要:
            中间值 - (2*i + 1) 次操作.
        7 所以，当 n 等于偶数时，我们直接用一个循环，遍历 for i in range(0, n/2), total_count += (中间值-(2*i+1))


        若 n 为奇数：
        1 - 中间值 mid 可以直接拿到
        2 - 其他和偶数方法一样
        """

        if n == 1:
            return 0
        if n == 2:
            return 1

        arr = []
        for idx in range(n):
            arr.append((2 * idx) + 1)

        # print(arr)
        total = 0
        # 偶数
        if n % 2 == 0:
            # 中间值
            oushu_mid = (arr[n // 2 - 1] + arr[n // 2]) // 2
            # for 循环累加
            oushu_end = n // 2
            for i in range(oushu_end):
                total += (oushu_mid - (2 * i + 1))

        # 奇数
        elif n % 2 == 1:
            # print("jishu")
            # 3 //2 = 1
            jishu_mid = arr[n // 2]
            # print("jishu_mid=%s" % jishu_mid)
            jishu_end = (n - 1) // 2
            for i in range(jishu_end):
                total += (jishu_mid - (2 * i + 1))
        return total