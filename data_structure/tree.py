from typing import List


class Tree(object):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.children = []

        def recursively_get_depth(self):
            return 1 + max([-1] + [child.recursively_get_depth() for child in self.children])

        def get_depth(self):
            depth = -1
            queue = [self]
            while queue:
                for i in range(len(queue)):
                    n = queue.pop(0)
                    for child in n.children:
                        queue.append(child)
                depth += 1
            return depth

        def dfs(self) -> List:
            order = []
            stack = [self]
            while stack:
                n = stack.pop()
                order.append(n.value)
                for child in n.children:
                    stack.append(child)
            return order

    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = Tree.Node(value)

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
    t = Tree()
    print(t.recursively_get_depth())
    n = Tree.Node(1)
    t.root = n
    print(t.recursively_get_depth())

    print("-" * 20)

    t = Tree()
    print(t.get_depth())
    n = Tree.Node(1)
    t.root = n
    print(t.get_depth())