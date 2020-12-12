# @File: 2.py
# @Author: Kevin Huo
# @Date: 2020/10/4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, Counter


class Solution:
    """
    已通过 - https://leetcode-cn.com/contest/weekly-contest-209/problems/even-odd-tree/
    """
    def isEvenOddTree(self, root: TreeNode) -> bool:
        res = True
        q = deque([root])
        lv = 0
        while q:
            curr_lv = lv
            lv += 1
            nums_in_this_lv = []
            for _ in range(len(q)):
                node = q.popleft()
                nums_in_this_lv.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # print("level=%s, nums_in_this_level=%s" % (curr_lv, nums_in_this_lv))
            # 严格递增
            c = Counter(nums_in_this_lv)
            for k in c:
                if c[k] > 1:
                    res = False
                    break
            # check 递增/递减
            if curr_lv % 2 == 0:
                # oushu
                sorted_nums = sorted(nums_in_this_lv)
                if sorted_nums != nums_in_this_lv:
                    print("1")
                    res = False
                    break

                for one in nums_in_this_lv:
                    if one % 2 == 0:
                        print("2")
                        res = False
                        break
            elif curr_lv % 2 == 1:
                # jishu
                reversed_sorted_nums = sorted(nums_in_this_lv, reverse=True)
                # print("lv=%s, reversed=%s equeal? %s" % (curr_lv, reversed_sorted_nums, reversed_sorted_nums==nums_in_this_lv))
                if reversed_sorted_nums != nums_in_this_lv:
                    res = False
                    break
                for one in nums_in_this_lv:
                    if one % 2 == 1:
                        res = False
                        break

        return res



