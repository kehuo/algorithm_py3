# @File: my_practice
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 10:07 AM


"""
二叉树，甚至包括一般的所有类型的树，一共分为3种遍历方式:
1 - DFS - 使用 stack, 即python自带的 list 类型数据结构即可.
2 - BFS - 使用 队列, 但是如果用python built-in list 结构，在做 pop(0) 操作时非常慢，所以改用 collections.deque 实现.
3 - 递归 - 有 前序/中序/后序 递归。 前序是指 自己-左-右，中序指 左-自己-右， 后序指 左-右-自己。

"""

class BinaryTreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1 - DFS 遍历二叉树
def dfs(root: BinaryTreeNode):
    # stack
    pass


# 2 - BFS 遍历二叉树
def bfs(root: BinaryTreeNode):
    # collections.deque
    from collections import deque
    pass


# 3 - 递归遍历二叉树
# 3.1 - 前序遍历
def preorder(root: BinaryTreeNode):
    """
    1 - 定义基准情况
    2 - 其他情况的递归逻辑
    """

    # 1 - 基准情况
    if root is None:
        return
    # 2 - 前序 自己-左-右
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# 3.2 - 中序遍历

# 3.3 - 后序遍历


if __name__ == '__main__':
    # 测试用例 - 用一颗满二叉树[1, 2, 3, 4, 5, 6, 7]
    #               1
    #            2     3
    #           4 5   6 7
    t1 = BinaryTreeNode(1)
    t2 = BinaryTreeNode(2)
    t3 = BinaryTreeNode(3)
    t4 = BinaryTreeNode(4)
    t5 = BinaryTreeNode(5)
    t6 = BinaryTreeNode(6)
    t7 = BinaryTreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    # 3.1 - 前序遍历
    preorder(t1)

