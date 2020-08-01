# @File: tree
# @Author: Kevin Huo
# @LastUpdate: 8/1/2020 7:52 PM



from collections import deque

# bfs dfs


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def bfs(root:TreeNode):
  # queue
  # double ended quee
  visited=set()
  q=deque([root])
  while q:
    node=q.popleft()
    # do something-a
    if node.left:
      # do something-b1
      q.append(node.left)
    if node.right:
      # do something-b2
      q.append(node.right)

def dfs(root:TreeNode):
  # stack
  pass


def test():
  t1=TreeNode(1)
  t2=TreeNode(2)
  t3=TreeNode(3)
  t1.left=t2
  t2.left=t3
  t3.left=t1
  # gaph
  bfs(t1)

test()




def generate_tree(values):
  if not values:
    return None
  values=[None]+values
  n=len(values)
  tmp=[None]*n
  tmp[1]=TreeNode(values[1])
  for i in range(1,n):
    if not tmp[i]:
      continue
    if 2*i<n and values[2*i]:
      tmp[2*i]=TreeNode(values[2*i])
      tmp[i].left=tmp[2*i]
    if 2*i+1<n and values[2*i+1]:
      tmp[2*i+1]=TreeNode(values[2*i+1])
      tmp[i].right=tmp[2*i+1]
  return tmp[1]
