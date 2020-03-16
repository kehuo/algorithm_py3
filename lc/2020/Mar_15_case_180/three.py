# @File: three
# @Author: Kevin Huo
# @LastUpdate: 3/15/2020 10:28 AM


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def balanceBST(root: TreeNode):
    """
    已提交成功, 用时 6448ms, 内存 18MB
    https://leetcode-cn.com/problems/balance-a-binary-search-tree/

    分2步:
    1. bfs或者dfs 遍历所有节点, 全部放入一个数组,
    2. 对数组排序, 保证这个数组是个有序数组
    2. 使用二分法, 将这个有序数组构造为一棵平衡二叉搜索树
    """
    def _bfs(_node):
        """功能函数1 - 广度优先搜索"""
        _array = []
        q = [_node]
        while q:
            curr = q.pop(0)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            curr.left = None
            curr.right = None
            _array.append(curr)
        return _array

    def _dfs(_node):
        """功能函数2 -- 深度优先搜索 (因为做题是为了学习, 所以深度和广度搜索, 都顺便在这个题中复习一下)"""
        _array = []
        q = [_node]
        while q:
            # 和bfs唯一的区别, 就是把pop(0) 改成 pop(-1), 时间会比 pop(0) 快20倍+ (bfs用时6448ms, dfs用时300ms)
            curr = q.pop(-1)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            curr.left = None
            curr.right = None
            _array.append(curr)
        return _array

    def _erfen(_array):
        """功能函数3 - 二分法"""
        if len(_array) == 0:
            return None
        # 二分法重构一颗平衡二叉树
        _mid = len(_array) // 2
        _left_sub_array = _array[:_mid]
        _right_sub_array = _array[_mid+1:]

        _root = _array[_mid]
        _root.left = _erfen(_left_sub_array)
        _root.right = _erfen(_right_sub_array)

        return _root

    # 1 先bfs/dfs (由于bfs中的pop(0)非常慢, 所以如果这里用dfs 的 pop(-1), 算法所需时间会比bfs快20倍+)
    array = _dfs(root)
    # 2 排序
    array.sort(key=lambda elem: elem.val)
    # 3 二分法重构新的平衡二叉树
    new_root = _erfen(array)

    return new_root


if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.right = TreeNode(3)
    a.right.right.right = TreeNode(4)
    a.right.right.right.right = TreeNode(5)

    res = balanceBST(a)
