# @File: q2
# @Author: Kevin Huo
# @LastUpdate: 3/26/2020 9:21 PM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    leetcode 题库 第2题 -- 已通过 152ms / 13.8MB
    https://leetcode-cn.com/problems/add-two-numbers/

    个位.next = 十位
    十位.next = 百位

    流程:
    1 将 l1 转换成 int型数据
    2 将 l2 转换成 int型数据
    3 求和
    4 将和转成 str 型数据, 比如将 708 转成 "708"
    5 对 str 的每一个字符, 创建一个ListNode, 比如 "708"可以创建3个节点 ListNode(7), ListNode(0), ListNode(8)
    6 遍历 range(len("708") - 1), 并且第i的 Node.next = 第i-1个Node
    """
    bits_1 = bits_2 = 0
    nums_1, nums_2 = [], []
    n1 = n2 = 0

    # 1 将 l1 转换成 int型数据
    node_1 = l1
    while True:
        bits_1 += 1
        nums_1.append(node_1.val)
        if node_1.next is None:
            break
        node_1 = node_1.next

    for e in range(bits_1):
        n1 += nums_1[e] * (10 ** e)

    # 2 将 l2 也转换成 int型数据
    node_2 = l2
    while True:
        bits_2 += 1
        nums_2.append(node_2.val)
        if node_2.next is None:
            break
        node_2 = node_2.next

    for e in range(bits_2):
        n2 += nums_2[e] * (10 ** e)

    # 3 求和
    n_res = n1 + n2

    # 4 - 6 将 n_res 从int 型数据转换成 ListNode 型
    # 4
    n_str = str(n_res)

    # 5
    node_dict = {}
    i = len(n_str) - 1
    while i >= 0:
        print("循环开始, i=%s, n_str[i]=%s" % (i, n_str[i]))
        tmp = ListNode(
            int(n_str[i])
        )
        node_dict[i] = tmp
        i -= 1
    # 6
    for j in range(len(n_str) - 1, 0, -1):
        node_dict[j].next = node_dict[j - 1]

    return node_dict[len(n_str) - 1]


if __name__ == '__main__':
    r1 = ListNode(2)
    r2 = ListNode(4)
    r3 = ListNode(3)
    r1.next = r2
    r2.next = r3

    r4 = ListNode(5)
    r5 = ListNode(6)
    r6 = ListNode(4)
    r4.next = r5
    r5.next = r6
    addTwoNumbers(r1, r4)
