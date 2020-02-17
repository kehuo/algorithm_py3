from typing import List


class BinaryTree(object):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.left = None
            self.right = None

        # def __str__(self):
        #     return str(self.value)

        def recursively_get_depth(self):
            l = self.left.recursively_get_depth() if self.left is not None else -1
            r = self.right.recursively_get_depth() if self.right is not None else -1
            return 1 + max(l, r)

        def get_depth(self):
            # traverse by level
            depth = -1
            queue = [self]
            while queue:
                for i in range(len(queue)):
                    n = queue.pop(0)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                depth += 1
            return depth

        def dfs(self) -> List:
            order = []
            stack = [self]
            while stack:
                n = stack.pop()
                order.append(n.value)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            return order

    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = BinaryTree.Node(value)

    def recursively_get_depth(self):
        if self.root is None:
            return -1
        else:
            return self.root.recursively_get_depth()

    def get_depth(self):
        if self.root is None:
            return -1
        else:
            return self.root.get_depth()

    def dfs(self) -> List:
        if self.root is None:
            return []
        else:
            return self.root.dfs()


if __name__ == "__main__":
    t = BinaryTree()
    print(t.recursively_get_depth())
    n = BinaryTree.Node(1)
    t.root = n
    print(t.recursively_get_depth())

    print("-" * 20)

    t = BinaryTree()
    print(t.get_depth())
    n = BinaryTree.Node(1)
    t.root = n
    print(t.get_depth())