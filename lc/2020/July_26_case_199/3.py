# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 7/26/2020 10:30 AM


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        https://leetcode-cn.com/contest/weekly-contest-199/problems/number-of-good-leaf-nodes-pairs/

        一个数组表示的二叉树中, 索引为 i 的节点的左右叶节点的索引分别是 (2i-1) 和 (2i). 比如:
        根节点的索引 i = 0, 所以它的左节点索引是 2i-1 = 1, 右节点是 2i = 2.
        对于索引为2的节点，它的左节点索引是 2x2-1 = 3, 右节点索引是 2x2=4

        思路：
        1 - 深度优先遍历, 找到所有叶子结点
        2 - 对于所有的叶子结点, 进行两两比较

        leaf - 所有叶子结点
        """
        q = [root]
        res = []
        visited = []
        leaf = []
        while q:
            curr = q.pop(0)
            if curr is None:
                if len(q) > 0:
                    res.append(None)
                continue
            print("当前节点是%s, 左节点=%s, 右节点=%s" % (curr.val, curr.left, curr.right))
            res.append(curr.val)
            visited.append(curr)
            if curr.left or curr.right:
                q.append(curr.left)
                q.append(curr.right)
                print("将%s的左、右节点放入q" % curr.val)
            else:
                # print("叶子结点%s, 左右节点均为None, 当前q长度=%s" % (curr.val, len(q)))
                if len(q) > 0:
                    res.append(None)
                leaf.append(curr)

        print("res: %s" % res)
        print("visited: %s" % [n.val for n in visited])
        print("leaf: %s" % [n.val for n in leaf])


if __name__ == '__main__':
    # [1, 2, 3, null, 4]
    n1 = TreeNode(val=1)
    n1.left = TreeNode(val=2)
    n1.left.right = TreeNode(val=4)
    n1.right = TreeNode(val=3)

    # n2 = [1,2,3,4,5,6,7]
    n2 = TreeNode(val=1)
    n2.left = TreeNode(val=2)
    n2.right = TreeNode(val=3)
    n2.left.left = TreeNode(val=4)
    n2.left.right = TreeNode(val=5)
    n2.right.left = TreeNode(val=6)
    n2.right.right = TreeNode(val=7)

    # n3 = [7,1,4,6,null,5,3,null,null,null,null,null,2]
    n3 = TreeNode(7)
    n3.left = TreeNode(1)
    n3.right = TreeNode(4)
    n3.left.left = TreeNode(6)
    n3.right.left = TreeNode(5)
    n3.right.right = TreeNode(3)
    n3.right.right.right = TreeNode(2)

    tests = [
        [n1, 3], [n2, 3], [n3, 3]
    ]
    t = tests[2]

    solution = Solution()
    solution.countPairs(*t)
