# @File: three
# @Author: Kevin Huo
# @LastUpdate: 3/8/2020 1:06 AM


def numOfMinutes(n, headID, manager, informTime):
    """
    https://leetcode-cn.com/problems/time-needed-to-inform-all-employees/

    "用倒着推方法, 不从headID开始推. 而是从最底层员工开始推"
    优势 - 比正推简单
    缺点 - 时间复杂度目前是 O(nlogn), 大于正推的线性复杂度

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


def numOfMinutes_v2(n, headID, manager, informTime):
    """
    正推方法 - 优势: 时间复杂度可优化到O(n). 缺点(对我来说):较难

    d = {领导1: [下属1, 下属2],
         领导2: [下属3],
         领导3: [下属4, 下属5, 下属6]}


    正推, 并维护一个字典 t, 存储了 "最高领导到每一个 非叶子节点 所需的总时间".
    实例1:
    manager = [2, 2, -1, 2, 2, 2]
    informTime = [0, 0, 1, 0, 0, 0]
    t = {0: 1, 1: 1, 3: 1, 4: 1, 5: 1}, 代表:
    最高领导通知到:
        第0个员工的总用时为 1min;
        第1个员工的总用时为 1min;
        ...
        第5个员工的总用时为 1min;
        (END)

    实例2:
    headID = 0
    manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    t = {1: 1, 2: 1,
         3: 2, 4: 2, 5: 2, 6: 2}
    最高领导通知到:
        第1个员工的总用时 1min;
        第2个员工的总用时 1min;

        第3个员工的总用时 1+1=2min;
        第4个员工的总用时 1+1=2min;
        第5个员工的总用时 1+1=2min;
        第6个员工的总用时 1+1=2min;
        (END)
    **注意, 这里t到第六个员工就停止的原因在于: 以后所有的员工都是叶子结点, 不需要记录. (因为t本质的作用, 是避免重复计算)
    """
    res = 0

    d = {}
    for i in range(len(manager)):
        if manager[i] not in d:
            d[manager[i]] = [i]
            continue
        d[manager[i]].append(i)
    print("d: %s" % d)
    t = {}

    # 广度优先搜索 遍历d
    # 1. 令headID为初始节点, 并将初始节点放入 q (即 headID)
    # 2. 将初始节点移出q, 说明初始节点就是"当前访问的节点" --> curr = q.pop(0) --> 注意移出队列只能从队首移出.
    # 3. 将headID的所有邻接节点放入q (通过搜索d实现, 比如d[headID]的值就是headID的所有"邻接下属子节点")
    # 4. 执行当前循环的 主逻辑
    # 5. 主逻辑完毕后, 继续下一个while循环

    # 1
    q = [headID]
    visited = []
    while q:
        # 2
        print("q:=%s" % q)
        curr = q.pop(0)
        visited.append(curr)
        # 3
        if curr in d:
            q.extend(d[curr])

        # 4
        curr_total_time = 0
        # A. 如果 informTime[curr] == 0 --> 叶子节点 --> 计算 "当前总时间", 即:
        #   curr_total_time = informTime[manager[curr]] + t[manager[curr]] --> res = max(res, curr_total_time)
        # B. 如果 informTime[curr] != 0 --> 有下属 --> 更新t --> 搜索d, 将自己的第一个下属放入q --> 下一个循环

        # A
        if informTime[curr] == 0:
            # 计算当前叶子结点的总时间
            curr_total_time += informTime[manager[curr]]
            if manager[curr] in t:
                curr_total_time += t[manager[curr]]
            # 和res比较, 取较大值
            res = max(res, curr_total_time)
        # B
        elif informTime[curr] != 0:
            # t中不需要记录最高领导的数据
            if curr == headID:
                continue
            # 更新t
            t[curr] = informTime[manager[curr]]
            if manager[curr] in t:
                t[curr] += t[manager[curr]]
    print("t: %s" % t)
    print("visited: %s" % visited)
    return res


if __name__ == '__main__':
    #
    test = [
        # 1 -> 答案 = 1
        {"n": 6,
         "headID": 2,
         "manager": [2, 2, -1, 2, 2, 2],
         "informTime": [0, 0, 1, 0, 0, 0]},
        # 2 -> 答案 = 3
        {"n": 15,
         "headID": 0,
         "manager": [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
         "informTime": [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
        # 3 -> 答案 = 1076
        {"n": 4,
         "headID": 2,
         "manager": [3, 3, -1, 2],
         "informTime": [0, 0, 162, 914]}
    ]
    start = 1
    end = 3
    all_res = []

    for j in range(start, end):
        r = numOfMinutes_v2(**test[j])
        all_res.append(r)
        print(str(r) + "\n")

    # 答案 = [1, 3, 1076]
    print(all_res)
