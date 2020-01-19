class MyCircularQueue:
    """
    设计简单的 循环队列
    https://leetcode-cn.com/explore/learn/card/queue-stack/216/queue-first-in-first-out-data-structure/865/

    题目
    设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。
    它也被称为“环形缓冲器”。
    好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。
    但是使用循环队列，我们能使用这些空间去存储新的值。

    你的实现应该支持如下操作：
    MyCircularQueue(k): 构造器，设置队列长度为 k 。
    Front: 从队首获取元素。如果队列为空，返回 -1 。
    Rear: 获取队尾元素。如果队列为空，返回 -1 。
    enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
    deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
    isEmpty(): 检查循环队列是否为空。
    isFull(): 检查循环队列是否已满。

    示例：
    MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3
    circularQueue.enQueue(1);  // 返回 true
    circularQueue.enQueue(2);  // 返回 true
    circularQueue.enQueue(3);  // 返回 true
    circularQueue.enQueue(4);  // 返回 false，队列已满
    circularQueue.Rear();  // 返回 3
    circularQueue.isFull();  // 返回 true
    circularQueue.deQueue();  // 返回 true
    circularQueue.enQueue(4);  // 返回 true
    circularQueue.Rear();  // 返回 4
    """
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = []
        self.q_max_len = k

    def en_queue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.q) < self.q_max_len:
            self.q.append(value)
            return True
        else:
            return False

    def de_queue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.q) == 0:
            return False
        else:
            self.q.pop(0)
            return True

    def front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if len(self.q) == 0 else self.q[0]

    def rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if len(self.q) == 0 else self.q[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if len(self.q) == 0 else False

    def is_full(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if len(self.q) == self.q_max_len else False


def main():
    q = MyCircularQueue(8)
    print(q.is_empty())
    q.en_queue(3)
    print(q.is_empty())


if __name__ == '__main__':
    main()