from typing import List, Tuple


if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from data_structure.binary_tree import BinaryTree
else:
    from data_structure.binary_tree import BinaryTree


class Heap(BinaryTree):
    class HeapNode(BinaryTree.Node):
        def __init__(self, value):
            super().__init__(value)
            self.prop = None
            self.next = None

    def __init__(self, data: List[int]):
        self.root = None
        self.tail = None
        self.size = 0
        for v in data:
            n = self.HeapNode(v)
            self.push(n)

    def prior(self, v1, v2):
        return v1 > v2

    def _swap(self, n1, n2):
        if n1 is n2:
            return
        n1.value, n2.value = n2.value, n1.value
        return n2

    def heapify_up(self, node):
        n = node
        while n is not self.root:
            if self.prior(n.value, n.parent.value):
                n = self._swap(n, n.parent)
                continue
            else:
                break

    def heapify_down(self, node):
        n = node
        while n.left or n.right:
            if n.left is None:
                max_child = n.right
            elif n.right is None:
                max_child = n.left
            elif self.prior(n.left.value, n.right.value):
                max_child = n.left
            else:
                max_child = n.right

            if self.prior(n.value, max_child.value) or n.value == max_child.value:
                break
            else:
                n = self._swap(n, max_child)

    def get_root(self):
        return self.root

    def get_tail(self):
        return self.tail

    def get_largest(self) -> Tuple[int, int]:
        return self.get_root()

    def get_smallest(self) -> Tuple[int, int]:
        return None
        # tail is not the smallest
        # return self.get_tail()

    def push(self, node):
        n = node
        if self.root is None:
            self.root = n
            self.tail = n
            self.size = 1
            return
        elif self.tail is self.root:
            self.root.left = n
            n.parent = self.root
            self.root.next = n
            n.prop = self.root
            self.tail = n
            self.heapify_up(n)
            self.size += 1
        else:
            if self.tail.parent.right is None:
                p = self.tail.parent
                p.right = n
                n.parent = p
                self.tail.next = n
                n.prop = self.tail
                self.tail = n
                self.heapify_up(n)
                self.size += 1
            else:
                p = self.tail.parent.next
                p.left = n
                n.parent = p
                self.tail.next = n
                n.prop = self.tail
                self.tail = n
                self.heapify_up(n)
                self.size += 1

    def pop(self):
        self._swap(self.get_root(), self.get_tail())
        n = self.tail
        if n is self.root:
            self.root = None
            self.tail = None
            self.size = 0
            return n
        else:
            p = self.tail.parent
            if p.right is n:
                p.right = None
            else:
                p.left = None
            n.prop.next = None
            self.tail = n.prop
            self.size -= 1
            self.heapify_down(self.root)

            n.parent = None
            n.prop = None
        return n

    def __str__(self):
        s = ""
        level = 0
        cnt = 0
        for v in self:
            s += str(v) + " "
            cnt += 1
            if cnt >= 2**(level):
                s += "\n"
                level += 1
                cnt = 0
        return s

    def __iter__(self):
        n = self.root
        while n:
            yield(n.value)
            n = n.next

    def modify(self, node, value):
        node.value = value
        self.heapify_up(node)
        self.heapify_down(node)

    def __len__(self):
        return self.size


class MinHeap(Heap):
    def prior(self, v1, v2):
        return v1 < v2

    def get_largest(self) -> Tuple[int, int]:
        return None
        # tail is not the largest
        # return self.get_tail()

    def get_smallest(self) -> Tuple[int, int]:
        return self.get_root()


class DeepHeap(Heap):
    def _swap(self, n1, n2):
        if n1 is n2:
            return
        if self.root is n1:
            self.root = n2
        elif self.root is n2:
            self.root = n1
        if self.tail is n1:
            self.tail = n2
        elif self.tail is n2:
            self.tail = n1
        p1, p2 = n1.parent, n2.parent
        l1, l2 = n1.left, n2.left
        r1, r2 = n1.right, n2.right
        pro1, pro2 = n1.prop, n2.prop
        nex1, nex2 = n1.next, n2.next

        if p1:
            if p1.left is n1:
                p1.left = n2
            else:
                p1.right = n2
        if p2:
            if p2.left is n2:
                p2.left = n1
            else:
                p2.right = n1
        if l1:
            l1.parent = n2
        if l2:
            l2.parent = n1
        if r1:
            r1.parent = n2
        if r2:
            r2.parent = n1
        if pro1:
            pro1.next = n2
        if pro2:
            pro2.next = n1
        if nex1:
            nex1.prop = n2
        if nex2:
            nex2.prop = n1

        n1.parent, n2.parent = n2.parent, n1.parent
        n1.left, n2.left = n2.left, n1.left
        n1.right, n2.right = n2.right, n1.right
        n1.prop, n2.prop = n2.prop, n1.prop
        n1.next, n2.next = n2.next, n1.next

        return n1


class DeepMinHeap(DeepHeap, MinHeap):
    pass


class Heap2(object):
    """ node quantity: N
        index from 1 to N
        parents: 1 to N//2
        leaves: N//2+1 to N
        i's parent: i//2
        i's children: 2*i and 2*i+1
    """

    def __init__(self, data: List[int]):
        self.heap = [None] + data
        N = len(data)
        for i in range(N // 2, 0, -1):
            self.heapify_down(i)

    def __len__(self):
        return len(self.heap) - 1

    def prior(self, v1, v2):
        return v1 > v2

    def heapify_down(self, parent: int) -> None:
        p = parent
        v = self.heap[parent]
        N = len(self.heap) - 1
        while 2 * p <= N:
            max_child = 2 * p
            if max_child < N and self.prior(self.heap[max_child + 1], self.heap[max_child]):
                # has two children and next one is prior
                max_child += 1
            if self.prior(v, self.heap[max_child]) or v == self.heap[max_child]:
                break
            else:
                self.heap[p] = self.heap[max_child]
                p = max_child
        self.heap[p] = v

    def pop(self):
        root = 1
        tail = len(self.heap) - 1
        self.heap[root], self.heap[tail] = self.heap[tail], self.heap[root]
        v = self.heap.pop()
        if len(self.heap) > 1:
            self.heapify_down(root)
        return v


class MinHeap2(Heap2):
    def prior(self, v1, v2):
        return v1 < v2


if __name__ == "__main__":
    print("heap sort")
    l = [2, 9, 7, 6, 5, 8]
    hs = [Heap(l), MinHeap(l), DeepHeap(l), DeepMinHeap(l)]
    for h in hs:
        print("origin", l)
        sl = []
        while len(h) > 0:
            sl.append(h.pop().value)
        print(sl)

    print("heap sort 2", "-" * 20)

    hs = [Heap2(l), MinHeap2(l)]
    for h in hs:
        print("origin", l)
        sl = []
        while len(h) > 0:
            sl.append(h.pop())
        print(sl)