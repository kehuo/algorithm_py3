# @File: utils
# @Author: Kevin Huo
# @LastUpdate: 8/2/2020 1:31 AM


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(values):
    if not values:
        return None
    values = [None] + values
    n = len(values)
    tmp = [None] * n
    tmp[1] = TreeNode(values[1])
    for i in range(1, n):
        if not tmp[i]:
            continue
        if 2 * i < n and values[2 * i]:
            tmp[2 * i] = TreeNode(values[2 * i])
            tmp[i].left = tmp[2 * i]
        if 2 * i + 1 < n and values[2 * i + 1]:
            tmp[2 * i + 1] = TreeNode(values[2 * i + 1])
            tmp[i].right = tmp[2 * i + 1]
    return tmp[1]

# test
# root=generate_tree([1,2,3,4,5,6,7])
# from collections import deque
# q=deque([root])
# while q:
#   node=q.popleft()
#   print(node.val)
#   if node.left:
#     q.append(node.left)
#   if node.right:
#     q.append(node.right)



