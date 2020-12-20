# @File: 环形链表
# @Author: Kevin Huo
# @LastUpdate: 12/15/2020 9:46 PM


class CircleList(object):
    def __init__(self, size=10):
        self.size = size
        self.DEFAULT_DATA = None
        self.space = [self.DEFAULT_DATA] * (self.size + 1)
        self.head = 0
        self.tail = 0

    def __str__(self):
        return str(self.space)

    def push(self, data):
        """
        队尾push, 队首pop
        push from tail
        pop from head
        如果队列已满, 则不能继续Push, 并且返回False
        如果 push 成功, 则返回 True
        """
        next_tail = (self.tail + 1) % (self.size + 1)
        if next_tail == self.head:
            # 已满
            print("full queue = %s, failed to push %s" % (self.space, data))
            return False
        self.space[self.tail] = data
        self.tail = next_tail
        print(self.space)
        return True

    def pop(self):
        if self.head == self.tail:
            print("empty queue, nothing to pop")
            return None
        popdata = self.space[self.head]
        self.space[self.head] = self.DEFAULT_DATA
        self.head = (self.head + 1) % (self.size + 1)
        print(self.space)
        return popdata


def main():
    c = CircleList(size=5)
    c.push(1)
    c.push(2)
    c.pop()
    c.pop()
    c.push(3)
    c.push(4)
    c.push(5)
    c.push(6)
    c.push(7)
    c.push(8)
    c.push(9)
    c.pop()
    c.pop()


if __name__ == '__main__':
    main()
