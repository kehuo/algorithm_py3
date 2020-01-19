class MinStack:
    """
    最小栈 - 已完成
    https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/877/

    题目
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    要求实现:
    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。


    示例:
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.get_min();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.get_min();   --> 返回 -2.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []

    def push(self, x: int) -> None:
        self.item.append(x)

    def pop(self) -> None:
        self.item.pop()

    def top(self) -> int:
        return self.item[-1] if len(self.item) > 0 else None

    def get_min(self) -> int:
        return min(self.item)
