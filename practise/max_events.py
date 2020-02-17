def maxEvents_old(events) -> int:
    """
    2020_02_16 - 第176场竞赛 - 最多可以参加的会议数目
    https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/

    实例及 DP思路：
    首先令 events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    可知 events 共5个索引，分别是 0， 1， 2， 3， 4

    我们定义 opt(i), 其中i是events的索引, 取值范围 0-4. 那么 opt(i)代表:
    "如果最多能选择的会议，是从0-i, 那么opt(i)代表 0-i 这些会议中能得到的最优解"

    比如 opt(3) 就代表了如果只能从 events[0], events[1], events[2], events[3] 这4个会议中选择的话，所计算出的最优解res.

    对于opt(i)的计算方法，考虑一下通项公式:
    1. if 选择 event[i] 这个会议, 那么 opt(i) = 1 + opt(previous(i)), 其中:
        1 代表: 因为选了这个会议, 所以参加的会议数量 + 1, 没有什么疑问, 很清晰.
        previous(i) 代表: 如果选择i这个会议, 那么从剩下的 0 ~ (i-1) 的会议中, 离的最近的一个可以选择的会议. 其中
            <1> previous(i) 需要根据题目的规则, 进行计算. 规则是: 当天会议i的开始时间，不得早于previous(i)的结束时间.
            <2> 只能往events的队首，也就是索引为0的这个方向看, 不能往events的末尾方向看.
        opt(previous(i))代表: previous(i) 可以取得的最优解res
    2. if 不选择 events[i] 这个会议, 那么opt(i) = opt(i-1)

    可以看出, 计算previous(i), 是这个方法的核心.

    另外，容易看出 当 i=0, 则 opt(0) = 1, 因为要么选，要么不选，选的话能参加的会议数量=1， 不选就等于0. 所以最优解=max(1, 0)
    """
    opts = [0] * len(events)
    prev = [None]

    # i == 1 >> 最大能选的会议数量就是1
    opts[0] = 1

    for i in range(1, len(events)):
        # 选i >> opt(i) = 1 + opt(previous(i))
        # 计算 previous(i) 的值
        sub = list(reversed(events[:i]))
        has_previous_value = False
        for j in range(len(sub)):
            # 前一天的会议结束时间 <= 今天的会议开始时间, 可以当做 previous(i)
            if sub[j][1] <= events[i][0]:
                print("i=%s, j=%s, sub=%s" % (i, j, sub))
                prev.append(i - j - 1)
                has_previous_value = True
                break
        if not has_previous_value:
            prev.append(None)

        if prev[i] is not None:
            yes = opts[prev[i]] + 1
        else:
            yes = 1

        # 不选 i >> opt(i) = opt(i-1)
        no = opts[i - 1]
        opts[i] = max(yes, no)
    print(prev)
    return opts[len(events) - 1]


# test = maxEvents_old([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]])
# print(test)


def maxEvents(events):
    """
    思路分两步
    1.具体到某一天上，我能去哪些（还没去过的）会议？
    2.这些能去的会议里，我选哪个？（选马上结束的那个）

    流程:
    1 求出总共需要多少天, 从第 day_range[0] 天 到 day_range[1] 天
    2 对于每一天, 能去哪些(还没去过的)会议
    """
    # 1 先求出所有会议所需的最大天数
    # day_range = [1, 4], 代表一共需要考虑4天, day1, day2, day3, day4.
    day_range = [
        min([i[0] for i in events]),
        max([j[1] for j in events])
    ]

    # 2 维护1个列表, 记录 "已经参加过" 的会议
    participated_meetings = []
    for i in range(day_range[0], day_range[1] + 1):
        # 2.1 先不考虑是否参加过, 先选出day[i]这一天所有可以参加的会议，放入 options 数组
        # 注意, options里存储的是会议的索引, 因为可能events里有2个一模一样的会议, 但是索引不一样. 比如
        # events = [[1, 2], [1, 2], [2, 4]], 这种情况下, 第一个会议和第二个会议时间完全相同, 所以只能通过索引来唯一的识别.
        options = [idx for idx in range(len(events)) if events[idx][0] <= i <= events[idx][1]]

        # 从options中, 把已经参加过的会议剔除掉
        if len(participated_meetings) > 0:
            for one in participated_meetings:
                if one in options:
                    # options.pop(options.index(one))
                    options.remove(one)
        # 2.2 从options中选一个参加, 选择的逻辑是 - 选马上结束的那个
        end_soon = [idx for idx in options if events[idx][1] == min([events[j][1] for j in options])]
        # print("第%d天可参加的所有会议: %s, 马上结束的会议:%s" % (i, options, end_soon))

        # 2.3 如果end_soon只有个项, 那选这个会议参加即可；若有多个会议都在同一天结束, 那么再加一层规则: 开始最晚的会议.
        if len(end_soon) == 1:
            # 就选这个会议参加, 将这个状态更新到 not_participated_meetings 数组中.
            participated_meetings.append(end_soon[0])
        elif len(end_soon) > 1:
            start_late = [idx for idx in end_soon if events[idx][0] == max([events[j][0] for j in end_soon])]

            if len(start_late) == 1:
                participated_meetings.append(start_late[0])
            elif len(start_late) > 1:
                # 这里就是2个完全一样的会议，开始时间和结束时间完全一样，这种就认为设置一个规则，取后面的一个即可.
                participated_meetings.append(start_late[-1])
        print("第%d天可参加的所有会议: %s, 马上结束的会议:%s" % (i, options, end_soon))
        print("已参加的会议: %s\n" % participated_meetings)

    return len(participated_meetings)


test = maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]])
print(test)
