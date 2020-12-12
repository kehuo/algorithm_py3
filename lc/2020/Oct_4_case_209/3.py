# @File: 3.py
# @Author: Kevin Huo
# @Date: 2020/10/4

from typing import List
import math


class Solution:
    """
    https://leetcode-cn.com/contest/weekly-contest-209/problems/maximum-number-of-visible-points/
    """
    def cal_total_angle(self, curr_line_k, angle):
        """
        curr_line_k: 当前点points[i] 和 location 形成的直线的斜率
        angle: 题目给定的视野的角度

        返回:
        根据斜率，求出当前直线的角度
        """

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
        循环一次:
        1 - d用来记录 location 和每一个点所连城的直线的 斜率 k = (y2 - y1) / (x2 - x1)

        第二次循环:
        对于每一个points中的点，都有一条和location连城的直线, 这条直线的斜率就是视野的2条边的其中一条，记做 curr_view_line_k。那么：
        我们有2种方法检查观测到的点的数量：
        我们用一个数组 can_see = [] 记录"对于每一条直线，能看到的最多点的数量"
        #1 - 角度angle 顺时针转
        #2 - 角度angle 逆时针转
        这样，我们就可以通过 angle, curr_view_line_k(当前直线的斜率) 求出视野的另一条直线的斜率 other_view_line_k
        然后，去 d 中找出所有 斜率的绝对值 小于等于 other_view_line_k 的绝对值 的点.

        返回can_see 中的最大值 max(can_see).
        或者，就用一个变量max_view = 0 记录，这样内存占用会小一点
        """
        d = {}
        for i in range(len(points)):
            p = points[i]
            if p == location:
                d[i] = 0
                continue
            y = (p[1] - location[1])
            x = (p[0] - location[0])
            if x == 0:
                d[i] = float("inf")
                continue
            d[i] = y / x
        print("d= %s" % d)

        can_see = []
        for i in range(len(points)):
            tmp_can_see_val_ssz = 0
            tmp_can_see_val_nsz = 0
            p = points[i]
            curr_view_line_k = d[i]
            # 根据斜率求出弧度 弧度和角度的换算公式是 2*pi / 360度
            curr_hudu = math.atan(curr_view_line_k)
            curr_angle = (curr_hudu * 360) / (2 * math.pi)
            # 根据angle 求另一条斜率, 有2种情况
            # 1 - 顺时针
            total_angle_ssz = curr_angle - angle
            # 求另一条边的斜率
            other_view_line_k_ssz = math.tan(total_angle_ssz)
            print("顺时针，当前角度=%s , 总共角度total = %s, 另一条斜率=%s" % (curr_angle, total_angle_ssz, other_view_line_k_ssz))
            # 计算当前视野中能看到的点的数量
            for k in d:
                if abs(d[k]) <= abs(other_view_line_k_ssz):
                    tmp_can_see_val_ssz += 1

            # 逆时针
            total_angle_nsz = curr_angle + angle
            # 求另一条边斜率
            other_view_line_k_nsz = math.tan(total_angle_nsz)
            for k in d:
                if abs(d[k]) <= abs(other_view_line_k_nsz):
                    tmp_can_see_val_nsz += 1
            can_see.append(max(tmp_can_see_val_ssz, tmp_can_see_val_nsz))
        return max(can_see)
