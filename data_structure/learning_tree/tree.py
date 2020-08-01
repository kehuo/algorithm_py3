# from utils import TreeNode, generate_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def search(root):
#   if not root:
#     return 0
#   l=search(root.left)
#   r=search(root.right)
#   return max(l,r)+1

from collections import defaultdict

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

# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#       leaf=[]
#       stack=[(root,"")]
#       while stack:
#         node,path=stack.pop()
#         if node.left:
#           stack.append((node.left,path+'l'))
#         if node.right:
#           stack.append((node.right,path+'r'))
#         if not node.left and not node.right:
#           leaf.append(path)

#       ans=0
#       for i in range(len(leaf)):
#         x=leaf[i]
#         for j in range(i):
#           y=leaf[j]
#           ret=len(x)+len(y)
#           for a,b in zip(x,y):
#             if a==b:
#               ret-=2
#             else:
#               break
#           if ret<=distance:
#             ans+=1
#       return ans

# def test():
#   s=Solution()
#   null=None
#   testcases=[
#     dict(root = [1,2,3,null,4], distance = 3),
#     dict(root = [1,2,3,4,5,6,7], distance = 3),
#     dict(root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3),
#     dict(root = [100], distance = 1),
#     dict(root = [1,1,1], distance = 2)
#   ]
#   for t in testcases:
#     print(s.countPairs(generate_tree(t["root"]), t["distance"]))

# test()

# Trie(字典树，前缀树)
# abc
# abd
# ab

# from collections import defaultdict
# Trie=lambda :defaultdict(Trie)

# root=Trie()
# # # trie是一个前缀树

# s=['abc','abd','ab']
# for line in s:
#   now = root
#   for ch in line:
#     now=now[ch]

# #   x
#     a b
#     b  d
#   c  d

# print(root)
# class TreeNode:
#   def __init__(self):
#     self.children = {}

# root=TreeNode()
# root.children['a']=TreeNode()
# root.children['b'].children=TreeNode()

# closure
"""
1. 它要输入一些参数p，它返回一个函数f
2. 函数f在调用过程中会使用参数p
"""
a = [1, 2, 3, 4, 5]


# def greater_than_2(l):
#   for x in l:
#     if x>2:
#       print(x)
# # greater_than_2(a)

# def greater_than_3(l):
#   for x in l:
#     if x>3:
#       print(x)
# greater_than_3(a)

# def warpper(thread):
#   def f(l):
#     for x in l:
#       if x>thread:
#         print(x)
#   return f

# greater_than_2=warpper(2)

# greater_than_2(a)
# # print(thread)
# greater_than_3=warpper(3)
# greater_than_3(a)

def sup(x):
    def log(func):
        def f(*args, **kwargs):
            result = func(*args, **kwargs)
            print(x, 'the result is:', result)
            return result

        return f

    return log


@sup(5)
def f1(n):
    # print(n)
    return n


# @log
def f2(m):
    result = m + 10
    # print(result)
    return result


print(f1(3))