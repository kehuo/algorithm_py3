def validateBinaryTreeNodes(n, leftChild, rightChild):
    """
    n: 节点数量
    leftChild: 一个列表, 存储所有节点的左子节点的 值
    rightChild: 一个列表, 存储所有节点的右子节点的 值.

    只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

    输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
    输出：true

    输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
    输出：false

    输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
    输出：false
    """
    parent_map = dict()

    class Node(object):
        def __init__(self, value, left, right, parent=-100):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    is_valid = True
    for idx in range(n):
        # 1 先构造
        node = Node(value=idx, left=leftChild[idx], right=rightChild[idx])
        # 先去parent_map找自己的 父节点 是哪个。 parent_map中k是子节点, v是父节点.
        # 如果找不到自己的父节点, 则不合法
        if len(parent_map) > 0:
            if node.value not in parent_map:
                print("找不到当前node:[%s]的父节点,不合法" % i)
                is_valid = False
                break
            node.parent = parent_map[node.value]
        if node.left != -1:
            # 如果一个子节点有多个父亲节点, 则不合法
            if node.left in parent_map:
                is_valid = False
                print("一个左子节点有多个父节点, 不合法")
                break
            parent_map[node.left] = node.value
        if node.right != -1:
            if node.right in parent_map:
                is_valid = False
                print("一个右子节点有多个父节点, 不合法")
                break
            parent_map[node.right] = node.value

        # 2 构造完成后, 开始检查
        # 2.1 一个节点的值, 是否是自己的父节点 （换句话说, 自己是自己的父亲）
        if node.value == node.parent:
            is_valid = False
            print("一个节点本身是自己的父亲, 不合法.")
            break
        # 2.2 如果除了根节点之外的任何节点, 他的parent=-100, 则说明不止一颗树, 不合法
        if node.parent == -100:
            if node.value != 0:
                is_valid = False
                print("除了根节点之外, 当前节点%s的parent=%s, 说明有多颗树, 不合法" % (i, node.parent))
                break
        # 2.2 如果一个节点的左子节点, 或者右子节点 = 他的父节点, 则非法. 等于是一个双向的树.
        if (node.parent == node.left) or (node.parent == node.right):
            is_valid = False
            print("当前idx=%s 的左子节点[%s], 或者右子节点[%s] 和他的父节点[%s] 相等, 等于是一个双向的树. 非法." % (i, node.left, node.right, node.parent))
            break
    print("结束, res=%s\n" % is_valid)
    return is_valid


if __name__ == '__main__':
    res_list = []
    test = [
        {"n": 4,
         "leftChild": [1, -1, 3, -1],
         "rightChild": [2, -1, -1, -1]},
        {"n": 4,
         "leftChild": [1, -1, 3, -1],
         "rightChild": [2, 3, -1, -1]},
        {"n": 2,
         "leftChild": [1, 0],
         "rightChild": [-1, -1]},
        {"n": 6,
         "leftChild": [1, -1, -1, 4, -1, -1],
         "rightChild": [2, -1, -1, 5, -1, -1]},
        {"n": 5,
         "leftChild": [1, 3, -1, -1, -1],
         "rightChild": [-1, 2, 4, -1, -1]}

    ]

    s = 0
    e = 5
    for i in range(s, e):
        t = test[i]
        res = validateBinaryTreeNodes(t["n"], t["leftChild"], t["rightChild"])
        res_list.append(res)
    # 标准答案: [True, False, False, False, True]
    print(res_list)
