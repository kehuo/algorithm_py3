# @File: three
# @Author: Kevin Huo
# @LastUpdate: 3/8/2020 1:06 AM


def numOfMinutes(n, headID, manager, informTime):
    """
    "用倒着推方法, 不从headID开始推. 而是从最底层员工开始推"
    执行用时 : 7100 ms
    内存消耗 :25.6 MB

    1. 初始化 res = 0
    2. 循环遍历 informTime 数组, 每当遇到一个 0, 就意味着遇到了一个最顶层的员工, 他不是任何人的领导， 所以这个员工就是叶子节点.
    3. 每当找到叶子结点， 就拿到他在informTime的索引idx(因为索引就是员工的ID), 回到manager数组中, 做4件事:
        3.1 初始化一个 curr_total_time, 代表当前员工倒推到 head 总领导所需的时间之和.
        3.2 用while manager[idx] != -1 作为判断依据， 开始while 循环, 倒着推, 每次都把他的领导的informTime累加到 curr_total_time 这个变量中.
        3.3 一直推到 -1这个领导, 停止
        3.4 比较 res 和 curr_total_time 谁大, 就把res 更新成较大的值 （即 res = max(res, curr_total_time)）
    4. 遍历完所有的informTime数组, 得到 res，就是所有员工中最后一个被通知的那个幸运儿所需的总时间.
    """
    # 1
    res = 0
    # 2
    for i in range(len(informTime)):
        if informTime[i] == 0:
            # 3 找到了一个最底层的员工, 开始往上倒着推
            # 3.1
            curr_total_time = 0
            curr_employee_id = i

            # 3.2 只要当前员工不是最高领导, 就继续循环往上推, 直到推到最高领导后停止
            while manager[curr_employee_id] != -1:
                # manager[curr_employee_id] 是当前员工的直属领导的id
                # informTime[manager[curr_employee_id]] 是当前员工的直属领导把消息通知给他所需要的时间.
                curr_total_time += informTime[manager[curr_employee_id]]
                # 然后把 curr_employee_id 换成当前员工的直属领导, 这样，在下次while循环中, 就可以累加领导的领导的通知时间, 以此类推
                curr_employee_id = manager[curr_employee_id]

            # 3.3 到这里应该已经跳出while 循环了, 说明已经倒着推到 manager 里面 -1 的最高的领导了.
            # 3.4 更新最长时间
            res = max(res, curr_total_time)
    return res


if __name__ == '__main__':
    test = [{"n": 6, "headID": 2, "manager": [2, 2, -1, 2, 2, 2], "informTime": [0, 0, 1, 0, 0, 0]}]
    start = 0
    end = 1
    for j in range(start, end):
        r = numOfMinutes(**test[j])
        print(str(r) + "\n")
