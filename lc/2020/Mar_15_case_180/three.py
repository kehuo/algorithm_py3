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
    1. bfs遍历所有节点, 全部放入一个数组, 并保证这个数组是个有序数组
    2. 使用二分法, 将一个有序数组构造为一颗平衡二叉搜索树
    """
    def _bfs(_node):
        """功能函数1 - 广度优先搜索"""
        _sorted_array = []
        visited = []
        q = [_node]
        while q:
            curr = q.pop(0)
            if curr in visited:
                continue
            visited.append(curr)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            curr.left = None
            curr.right = None
            _sorted_array.append(curr)
        _sorted_array.sort(key=lambda elem:elem.val)
        return _sorted_array

    def _erfen(_array):
        """功能函数2 - 二分法"""
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

    # 1 先bfs
    array = _bfs(root)
    # 2 二分法重构新的平衡二叉树
    new_root = _erfen(array)

    return new_root


if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.right = TreeNode(3)
    a.right.right.right = TreeNode(4)
    a.right.right.right.right = TreeNode(5)

    res = balanceBST(a)
