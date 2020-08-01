from tree import *
from utils import TreeNode,generate_tree
from collections import deque

# bfs dfs



# def bfs(root:TreeNode):
#   # queue
#   # double ended quee
#   visited=set()
#   q=deque([root])
#   while q:
#     node=q.popleft()
#     # do something-a
#     if node.left:
#       # do something-b1
#       q.append(node.left)
#     if node.right:
#       # do something-b2
#       q.append(node.right)

# def dfs(root:TreeNode):
#   # stack
#   visited=set()
#   stack=[root]
#   while stack:
#     node=stack.pop()
#     if node in visited:
#       continue
#     print(node.val)
#     visited.add(node)
#     # do something-a

#     # for ch in node.children:


#     if node.left:
#       # do something-b1
#       stack.append(node.left)
#     if node.right:
#       # do something-b2
#       stack.append(node.right)


# def test():
#   t1=TreeNode(1)
#   t2=TreeNode(2)
#   t3=TreeNode(3)
#   t1.left=t2
#   t2.left=t3
#   t3.left=t1
#   # gaph
#   dfs(t1)

# test()


# 求一棵二叉树的高度


# def dfs(root:TreeNode):
#   # stack
#   ans=0
#   stack=[(root,1)]
#   while stack:
#     node,height=stack.pop()
#     if node.left:
#       stack.append((node.left,height+1))
#     if node.right:
#       stack.append((node.right,height+1))
#     if not node.left and not node.right:
#       ans=max(ans,height)
#   return ans


# def bfs(root:TreeNode):
#   # queue
#   # double ended quee
#   q=deque([root])
#   ans=0
#   while q:
#     for _ in range(len(q)):
#       node=q.popleft()
#       # do something-a
#       if node.left:
#         # do something-b1
#         q.append(node.left)
#       if node.right:
#         # do something-b2
#         q.append(node.right)

#     ans+=1
#   return ans



# # 一棵有n个节点的满二叉树，高度为logn，叶子有n/2个
# def test():
#   # [1,2,3,4,5,6,7]
#   #    1
#   #   2 3
#   # 4 5 6 7
#   root=generate_tree([1,2,3,4,5,6,7])

#   if not root:
#     return 0
#   ans=bfs(root)
#   print(ans)

# test()


# def search(root):
#   if not root:
#     return 0
#   l=search(root.left)
#   r=search(root.right)
#   return max(l,r)+1

# root=generate_tree([1,2,3,4,5,6,7])
# print(search(root))
