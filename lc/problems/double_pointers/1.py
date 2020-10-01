# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 10/1/2020 11:50 AM


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        已提交通过
        https://leetcode-cn.com/problems/container-with-most-water/

        官方题解:
        https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/

        如何移动指针:
        1 - 相同情况下, 2边距离越远越好
        2 - 区域受限于较短边
        """
        l, r = 0, len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)
        while l < r-1:
            if height[l] > height[r]:
                moved_r = r - 1
                if height[moved_r] > height[r]:
                    max_area = max(max_area, min(height[l], height[moved_r]) * (moved_r - l))
                r -= 1
            else:
                moved_l = l + 1
                if height[moved_l] > height[l]:
                    max_area = max(max_area, min(height[r], height[moved_l]) * (r - moved_l))
                l += 1
        return max_area


if __name__ == '__main__':
    # ans = [49, 72]
    tests = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 8, 6, 2, 5, 4, 8, 3, 7, 14, 125, 6]
    ]
    t = tests[0]
    s = Solution()
    s.maxArea(t)
