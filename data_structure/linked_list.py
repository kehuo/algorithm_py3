class LinkedList(object):
    class Node(object):
        def __init__(self, value: int):
            self.value = value
            self.next = None

    def __init__(self, value):
        node = LinkedList.Node(value)
        self.length = 1
        self.first = node
        self.last = node

    def __iter__(self):
        node = self.first
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.length

    def append(self, value):
        n = LinkedList.Node(value)
        self.last.next = n
        self.last = n
        self.length += 1

    def extend(self, l):
        self.last.next = l.first
        self.last = l.last
        self.length += l.length


if __name__ == "__main__":
    l = LinkedList(3)
    l.append(5)
    l.append(7)
    print("l")
    for n in l:
        print(n.value)

    print("l2")
    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.extend(l)
    for n in l2:
        print(n.value)