import abc
from typing import List


if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from data_structure.tree import Tree
    from data_structure.linked_list import LinkedList
else:
    from data_structure.tree import Tree
    from data_structure.linked_list import LinkedList


class UnionFind(object):
    """base class for UnionFind"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def makeset(self, element: int) -> None:
        return

    @abc.abstractmethod
    def init_set(self, size: int)->None:
        return

    @abc.abstractmethod
    def find(self, element: int):
        return

    @abc.abstractmethod
    def union(self, x: int, y: int) -> None:
        return


class QuickFind(UnionFind):
    """quick find to implement union find"""

    def __init__(self, size):
        self.init_set(size)

    def __len__(self):
        return self.size

    def makeset(self, element: int) -> None:
        self.representative[element] = element
        self.linked_lists[element] = LinkedList(element)

    def init_set(self, size: int) -> None:
        self.size: int = size
        self.representative: List[int] = []
        self.linked_lists: List[LinkedList] = []
        for e in range(size):
            self.representative.append(e)
            l = LinkedList(e)
            self.linked_lists.append(l)

    def find(self, element: int) -> int:
        return self.representative[element]

    def union(self, x: int, y: int) -> None:
        """union by size
        """
        if self.find(x) == self.find(y):
            return

        lx = self.linked_lists[self.find(x)]
        ly = self.linked_lists[self.find(y)]
        if len(lx) >= len(ly):
            base = lx
            suffix = ly
            rep = self.find(x)
            suffix_index = self.find(y)
        else:
            base = ly
            suffix = lx
            rep = self.find(y)
            suffix_index = self.find(x)

        for node in suffix:
            self.representative[node.value] = rep
        base.extend(suffix)
        self.linked_lists[suffix_index] = None
        self.size -= 1
        return

    def check_size(self):
        num = 0
        for l in self.linked_lists:
            if l is not None:
                num += 1
        return self.size == num

    def get_sets(self) -> List[List[int]]:
        return [[n.value for n in l] for l in self.linked_lists if l is not None]


class QuickFind2(UnionFind):
    """quick find to implement union find, using list in python"""

    def __init__(self, size):
        self.init_set(size)

    def __len__(self):
        return self.size

    def makeset(self, element: int) -> None:
        self.representative[element] = element
        self.linked_lists[element] = [element]

    def init_set(self, size: int) -> None:
        self.size: int = size
        self.representative: List[int] = []
        self.linked_lists: List[List[int]] = []
        for e in range(size):
            self.representative.append(e)
            self.linked_lists.append([e])

    def find(self, element: int) -> int:
        return self.representative[element]

    def union(self, x: int, y: int) -> None:
        """union by size
        """
        if self.find(x) == self.find(y):
            return

        lx = self.linked_lists[self.find(x)]
        ly = self.linked_lists[self.find(y)]
        if len(lx) >= len(ly):
            base = lx
            suffix = ly
            rep = self.find(x)
            suffix_index = self.find(y)
        else:
            base = ly
            suffix = lx
            rep = self.find(y)
            suffix_index = self.find(x)

        for i in suffix:
            self.representative[i] = rep
        base += suffix
        self.linked_lists[suffix_index] = None
        self.size -= 1
        return

    def check_size(self):
        num = 0
        for l in self.linked_lists:
            if l is not None:
                num += 1
        return self.size == num

    def get_sets(self) -> List[List[int]]:
        return [[v for v in l] for l in self.linked_lists if l is not None]


class QuickUnion(UnionFind):
    def __init__(self, size: int):
        self.init_set(size)

    def __len__(self):
        return self.size

    def init_set(self, size: int) -> None:
        self.size: int = size
        self.forest: List[Tree.Node] = []
        self.nodes: List[Tree.Node] = []
        for e in range(size):
            n = Tree.Node(e)
            self.forest.append(n)
            self.nodes.append(n)

    def makeset(self, element: int) -> None:
        n = Tree.Node(element)
        self.forest.append(n)
        self.nodes[element] = n

    def find(self, element: int) -> Tree.Node:
        n = self.nodes[element]
        root = n
        while root.parent is not None:
            root = root.parent
        # path compression
        while n.parent is not None and n.parent is not root:
            n.parent, n = root, n.parent
        return root

    def union(self, x: int, y: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx is ry:
            return

        if rx.get_depth() >= ry.get_depth():
            rx.children.append(ry)
            ry.parent = rx
            for i in range(len(self.forest)):
                if self.forest[i] is ry:
                    self.forest[i] = None
                    break
            self.size -= 1
        else:
            ry.children.append(rx)
            rx.parent = ry
            for i in range(len(self.forest)):
                if self.forest[i] is rx:
                    self.forest[i] = None
                    break
            self.size -= 1

    def check_size(self):
        num = 0
        for t in self.forest:
            if t is not None:
                num += 1
        return self.size == num

    def get_sets(self) -> List[List[int]]:
        return [r.dfs() for r in self.forest if r is not None]


class QuickUnion2(UnionFind):
    def __init__(self, size: int):
        self.init_set(size)

    def __len__(self):
        return self.size

    def init_set(self, size: int) -> None:
        self.size: int = size
        self.forest: List[int] = list(range(size))

    def makeset(self, element: int) -> None:
        frozenset[element] = element

    def find(self, element: int) -> int:
        root = element
        while self.forest[root] != root:
            root = self.forest[root]
        # path compression
        while self.forest[element] != root:
            self.forest[element], element = root, self.forest[element]
        return root

    def union(self, x: int, y: int) -> None:
        # not union by rank
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.forest[rx] = ry
        self.size -= 1

    def check_size(self):
        for _ in range(len(self.forest)):
            self.find(_)
        return self.size == len(set(self.forest))

    def get_sets(self) -> List[List[int]]:
        for _ in range(len(self.forest)):
            self.find(_)
        roots = {root: index for index, root in enumerate(set(self.forest))}
        sets = []
        for _ in range(len(roots)):
            sets.append([])

        for node, root in enumerate(self.forest):
            sets[roots[root]].append(node)

        return sets


if __name__ == "__main__":
    """
    0-1  4-5
    |    |
    2-3  6
    """
    G = [[1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 1]]

    ufs = [QuickFind(len(G)), QuickFind2(len(G)), QuickUnion(len(G)), QuickUnion2(len(G))]
    for uf in ufs:
        if isinstance(uf, QuickFind):
            print("quick find, implemented by customed linked list")
        elif isinstance(uf, QuickFind2):
            print("quick find 2, implemented by python list")
        elif isinstance(uf, QuickUnion):
            print("quick union, implemented by customed tree")
        elif isinstance(uf, QuickUnion2):
            print("quick union 2, implemented by python list")

        # consider upper triangle
        for i in range(len(G) - 1):
            for j in range(i + 1, len(G)):
                if G[i][j] == 1:
                    uf.union(i, j)
        print("check size:", uf.check_size())
        print("sets count:", uf.size)
        sets = uf.get_sets()
        for i in range(len(sets)):
            print("{}-th set is".format(i))
            print(sets[i])
        print("-" * 20)