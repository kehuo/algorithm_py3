import heapq
if __name__ == '__main__':
    import sys
    sys.path.append("..")


def max_events_v1(events):
    """
    v1版本 - 时间复杂度 = O(n^^3) 立方

    思路分两步
    1.具体到某一天上，我能去哪些（还没去过的）会议？
    2.这些能去的会议里，我选哪个？（选马上结束的那个）

    流程解释：
    v1 - 版本
    1 先求出所有会议所需的天数的范围 (所有的会议, 最早开始于 start, 最晚结束于 end).

    2 对于每一天, 做2件事:
        2.1 找到这一天可以参加的所有会议, 把这些会议在events中的索引, 存储在 options 数组中.
            # 注意, options里存储的是会议的索引, 而不是会议本身数据, 因为可能events里有2个一模一样的会议, 但是索引不一样. 比如
            # events = [[1, 2], [1, 2], [2, 4]], 这种情况下, 第一个会议和第二个会议时间完全相同, 所以只能通过索引来唯一的识别.

        2.2 从options中, 把已经参加过的会议剔除掉
            # 注意 participated_meetings 这个字典的作用: 记录 "已经参加过" 的会议
            注意: 这里维护的是字典而不是数组, 因为对字典进行 if xxx in dict的时间复杂度是常数, 而对数组是线性, 所以用字典.
        2.3 剔除完之后, 从当前 options 中随便挑一个会议进行参加, 选择的原则是 (马上要结束的那一个)
            # 并且将这个已经选中，确认要参加的会议，更新到 participated_meetings 这个字典中.

    3 遍历完所有的天数之后, 返回 “已参加的会议” 这个字典的长度, 即为最终答案
    """
    # 1 先求出所有会议所需的最大天数
    day_range = [
        min([i[0] for i in events]),
        max([j[1] for j in events])
    ]

    # 2
    participated_meetings = []
    for i in range(day_range[0], day_range[1] + 1):
        # 2.1 O(n)
        options = [idx for idx in range(len(events)) if events[idx][0] <= i <= events[idx][1]]

        # 2.2 O(n^^2)
        if 0 < len(participated_meetings) > len(events):
            for one in participated_meetings:
                if one in options:
                    options.remove(one)

        # 2.3 O(n)
        if len(options) > 0:
            end_soon = [idx for idx in options if events[idx][1] == min([events[j][1] for j in options])][0]
            participated_meetings.append(end_soon)

    return len(participated_meetings)


def max_events_v2(events):
    """
    2020_02_16 - 第176场竞赛 - 最多可以参加的会议数目
    https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/
        # 由于这道题需要考虑全局的状态, 所以动态规划暂不适用于此问题. 考虑用以下其他方法解答.

    v2 - 时间复杂度 - O(n^^2)
    """
    # 1
    start = min([i[0] for i in events])
    end = max([j[1] for j in events])

    # 2
    res = 0
    for today in range(start, end + 1):
        # 2.1 options = 每一天“可以参加的所有会议” = {1: [[1, 4], [1, 3]], 2: [[2, 5], [2, 4]]}
        # print("开始, i=%s, res=%s, events=%s" % (i, res, events))
        options = dict()
        for idx in range(len(events)):
            if events[idx][0] <= today <= events[idx][1]:
                options[idx] = events[idx]

        # 2.2
        if len(options) > 0:
            end_soonest_value = min([idx[1] for idx in options.values()])
            end_soon = [idx for idx in options if options[idx][1] == end_soonest_value][0]

            res += 1
            events.pop(end_soon)
        # print("结束, i=%s, res=%s, events=%s" % (i, res, events))
    return res


def max_events_v3(events):
    """
    2020_02_16 - 第176场竞赛 - 最多可以参加的会议数目
    https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/
        # 由于这道题需要考虑全局的状态, 所以动态规划暂不适用于此问题. 考虑用以下其他方法解答.

    v3 - 时间复杂度 - O(n^^2)
    相对于v2, 这个版本需要优化2.1， 争取在第一个循环内, 将每一天所能参加的会议，都分配到一个大字典all_options 中.

    但是存在的问题是, 虽然2.1优化了， 但是2.2又有问题。每次res+=1后，需要遍历 all_options大字典的每一项，把刚才已经参加的会议
    删掉. 这其实也是一个线性复杂度的遍历。

    所以，目前的做法，等于是把2.1的线性复杂度移到了 2.2而已。
    todo 已经测试, 目前v2 其实反倒比v3要快。 所以v3需要优化，保证 2.1 和 2.2 都是常数复杂度.

    该版本的2.1 不科学, 需要大幅度重写, 直接更新在v4
    """
    # 1
    start = min([i[0] for i in events])
    end = max([j[1] for j in events])

    # 2
    res = 0
    all_options = dict()
    for today in range(start, end + 1):

        # 2.1 options = 每一天“可以参加的所有会议” = {1: [[1, 4], [1, 3]], 2: [[2, 5], [2, 4]]}
        if all_options == {}:
            for each_day in range(start, end + 1):
                all_options[each_day] = dict()
                for idx in range(len(events)):
                    if events[idx][0] <= each_day <= events[idx][1]:
                        all_options[each_day][idx] = events[idx]

        options = all_options[today]
        # 2.2
        if len(options) > 0:
            end_soonest_value = min([k[1] for k in options.values()])
            end_soon = [idx for idx in options if options[idx][1] == end_soonest_value][0]

            res += 1

            # 这里要从 all_options 中, 把所有包含这一个会议的项都删掉.
            for k in all_options:
                if end_soon in all_options[k].keys():
                    del all_options[k][end_soon]
    return res


def max_events_v4(events):
    """
    v4 - 时间复杂度 - O(n)
    相对于v3, 这个版本优化了2.1:
        1. 将 all_options 一个字典存储的信息, 分成 start_dict 和 end_dict 2个字典存储
        2. 将 初始化这2个字典的步骤, 移到 step2 大循环之外.

    该版本已通过 leetcode 测试 - 1800ms / 70MB
    todo 优化2.2 - 通过 堆 实现 优先队列 > 使得2.2的整体效率达到 O(log(n))
    """
    # 1 准备工作
    # 1.1 - 计算所有会议中 最早开始的时间min_start 和 最晚结束的时间max_end - 复杂度 O(n)
    min_start = min([i[0] for i in events])
    max_end = max([j[1] for j in events])

    # 1.2 初始化 end_dict - O(n)
    start_dict = {}
    end_dict = {}
    for today in range(min_start, max_end + 1):
        start_dict[today] = []
        end_dict[today] = []

    # 1.3 遍历events, 构造 end_dict - O(n). 因为append操作是O(1)复杂度
    for idx in range(len(events)):
        one = events[idx]
        start_dict[one[0]].append(idx)
        end_dict[one[1]].append(idx)

    res = 0
    options = []
    # 2 主循环 O(n)
    for today in range(min_start, max_end + 1):
        # 2.1 每天动态的维护 options 数组.
        # 维护方式 - 第i天放入start_end[i], 并删除 end_dict[i-1]. 若 i==1 则不用删除, 只放入.
        options.extend(start_dict[today])
        if today > min_start:
            for m in end_dict[today - 1]:
                if m in options:
                    options.remove(m)

        # 2.2
        if len(options) > 0:
            end_soonest_value = min([events[idx][1] for idx in options])
            end_soon = [idx for idx in options if events[idx][1] == end_soonest_value][0]

            # 将已选择的会议从 options 数组中删除
            res += 1
            options.remove(end_soon)
    return res


def max_events_v5(events):
    """
    2020-02-22 在v4的基础上, 对2.2步骤使用优先队列实现, 优化性能.
    """
    # 1 准备工作
    # 1.1 - 计算所有会议中 最早开始的时间min_start 和 最晚结束的时间max_end - 复杂度 O(n)
    min_start = min([i[0] for i in events])
    max_end = max([j[1] for j in events])

    # 1.2 初始化 end_dict - O(n)
    start_dict = {}
    end_dict = {}
    for today in range(min_start, max_end + 1):
        start_dict[today] = []
        end_dict[today] = []

    # 1.3 遍历events, 构造 end_dict - O(n). 因为append操作是O(1)复杂度
    for idx in range(len(events)):
        one = events[idx]
        start_dict[one[0]].append(idx)
        end_dict[one[1]].append(idx)

    res = 0
    options = []
    # 2 主循环 O(n)
    for today in range(min_start, max_end + 1):
        # 2.1 每天动态的维护 options 数组.
        # 维护方式 - 第i天放入start_end[i], 并删除 end_dict[i-1]. 若 i==1 则不用删除, 只放入.

        # 将 start_dict[today] 中的项写入 options
        for k in start_dict[today]:
            heapq.heappush(options, [events[k][1], events[k][0]])
        # 删除前一天的 end_dict[i-1]
        # todo 2020-02-22 注释 - 这里heapq.heappop 方法有问题, 之后再优化
        if today > min_start:
            for m in end_dict[today - 1]:
                if options[0][0] < today:
                    heapq.heappop(options)

        # 2.2
        if len(options) > 0:
            # 调用 extract_max 方法, 找到并弹出最大值, 作为要参加的会议
            end_soon = heapq.heappop(options)
            res += 1

    return res


if __name__ == '__main__':
    test_inputs = list()
    # 答案 = 5
    test_inputs.append(
        [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    )

    # 答案 = 2
    test_inputs.append(
        [[52, 79], [7, 34]]
    )

    # 答案 = 3
    test_inputs.append(
        [[1, 2], [2, 3], [3, 4]]
    )

    # 答案 = 4
    test_inputs.append(
        [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    )
    # test_events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]

    # 答案 = 800
    big1 = [[659,919],[442,831],[981,1109],[815,1501],[712,1187],[125,707],[808,1354],[234,607],[970,1886],[97,891],[418,862],[603,1385],[89,527],[927,1892],[304,605],[459,1102],[38,498],[746,1650],[703,1146],[850,926],[810,1716],[118,722],[262,402],[799,879],[581,1476],[507,1218],[767,1441],[239,761],[774,1569],[972,1811],[574,1495],[540,1067],[249,809],[401,1064],[489,984],[181,798],[585,924],[280,1074],[86,469],[259,1006],[686,772],[628,1355],[980,1772],[485,656],[689,1338],[527,1155],[247,453],[636,790],[305,507],[672,791],[63,226],[538,758],[364,1168],[363,470],[331,1118],[832,1047],[637,1591],[947,1693],[75,493],[907,1479],[973,1478],[926,1218],[150,544],[107,577],[171,561],[664,997],[70,521],[394,461],[485,572],[708,980],[37,636],[535,601],[745,818],[441,812],[713,881],[219,806],[121,307],[153,406],[193,743],[7,391],[88,265],[725,976],[458,1392],[435,1333],[537,554],[57,919],[996,1107],[862,1362],[663,1163],[972,1406],[846,1670],[196,595],[409,572],[634,1266],[659,1530],[617,1092],[605,1356],[309,438],[302,887],[581,675],[936,1690],[361,1281],[764,1159],[851,1782],[137,519],[471,910],[813,1365],[191,850],[727,1240],[28,596],[545,1543],[491,833],[728,980],[68,891],[458,644],[231,850],[773,1709],[371,742],[358,745],[993,1860],[339,914],[853,1176],[735,805],[59,870],[378,1198],[813,1333],[223,600],[923,1179],[755,1725],[411,1367],[459,611],[495,710],[112,225],[54,841],[233,856],[924,943],[229,266],[992,1687],[339,828],[504,927],[857,1402],[492,947],[518,544],[6,27],[424,1166],[15,151],[941,1739],[286,505],[633,913],[150,944],[181,342],[522,980],[429,581],[500,596],[438,962],[716,1132],[611,1503],[186,997],[887,1418],[46,149],[988,1295],[790,1403],[182,1003],[937,1129],[451,484],[769,1353],[699,817],[807,947],[636,1372],[593,1233],[542,775],[356,1289],[691,1443],[379,1123],[58,360],[146,1145],[336,538],[598,1571],[211,854],[657,825],[682,1258],[690,1116],[774,856],[584,827],[978,1305],[989,1375],[101,270],[934,1256],[504,512],[389,1199],[284,1053],[105,1045],[975,1010],[905,1579],[450,457],[317,1162],[510,977],[367,1346],[82,341],[722,1466],[168,280],[897,1598],[96,488],[85,95],[701,1375],[909,1138],[718,978],[444,601],[786,1122],[427,1058],[933,1126],[315,999],[188,813],[435,1208],[462,1340],[629,1139],[255,575],[991,1135],[540,581],[41,607],[820,1085],[180,299],[545,1141],[801,1304],[355,878],[92,168],[535,745],[122,636],[812,854],[728,1197],[983,1063],[654,1509],[837,1156],[397,975],[587,1494],[332,876],[110,968],[900,1435],[720,1357],[616,1315],[454,653],[252,918],[527,825],[661,1103],[428,819],[310,457],[468,1010],[318,1146],[142,687],[107,789],[514,912],[483,1083],[435,664],[775,1278],[380,1333],[877,1082],[624,1197],[44,967],[357,1013],[97,590],[51,1044],[839,1643],[195,287],[975,1743],[91,332],[264,581],[430,1163],[980,1390],[635,851],[95,772],[885,1406],[283,863],[517,702],[546,1239],[161,272],[745,1153],[535,1529],[268,959],[511,632],[326,1308],[112,518],[209,1152],[637,1274],[383,1378],[1,922],[693,1187],[448,475],[459,1302],[811,1611],[726,747],[875,921],[521,1192],[513,1374],[996,1740],[538,734],[215,1126],[453,1343],[773,1190],[350,652],[435,721],[882,1245],[179,907],[783,1162],[495,1143],[737,896],[589,1207],[923,1845],[398,855],[232,880],[386,642],[642,707],[86,810],[580,1579],[586,1435],[520,654],[518,714],[105,602],[988,1445],[206,211],[983,1578],[471,929],[663,1625],[638,1120],[365,573],[199,729],[216,1189],[989,1563],[476,1156],[938,939],[569,1438],[490,1193],[260,475],[145,788],[49,698],[553,1030],[81,472],[845,1536],[54,121],[159,915],[644,904],[16,944],[203,1060],[903,1731],[983,1446],[155,912],[991,1216],[540,983],[664,783],[325,1136],[417,1191],[122,724],[579,689],[43,229],[205,685],[596,1198],[419,1066],[606,662],[389,835],[920,1166],[519,1043],[288,1139],[95,819],[631,905],[794,1531],[532,1108],[291,1159],[869,1456],[568,964],[231,676],[64,533],[236,319],[480,1435],[282,922],[412,1217],[524,748],[573,1023],[314,897],[642,1447],[734,1685],[794,934],[41,738],[434,864],[226,907],[308,1279],[14,114],[703,717],[344,1022],[812,1013],[66,175],[420,616],[366,650],[586,1101],[494,500],[133,743],[305,499],[394,828],[939,1393],[692,1501],[231,419],[237,509],[724,915],[570,729],[142,514],[669,1468],[113,535],[527,590],[191,244],[433,1113],[610,784],[466,1452],[506,1144],[300,640],[779,1547],[15,617],[356,692],[833,1211],[77,391],[421,1146],[99,276],[425,794],[477,1214],[621,1280],[777,1737],[587,1582],[956,1366],[340,890],[328,683],[422,1340],[840,1729],[653,949],[581,1453],[142,195],[357,677],[534,802],[940,1181],[48,749],[36,228],[434,1206],[469,1405],[995,1631],[521,713],[701,1699],[379,669],[230,633],[578,1090],[234,422],[563,1083],[298,899],[218,954],[824,1752],[876,1097],[685,1607],[340,514],[906,1071],[498,1236],[592,1301],[386,497],[38,861],[900,1868],[38,601],[168,314],[100,1091],[557,1052],[885,1209],[494,1360],[909,999],[143,203],[590,845],[632,1517],[366,1236],[292,1147],[156,179],[601,1061],[131,566],[313,968],[251,856],[372,695],[413,525],[767,1477],[278,471],[7,637],[650,969],[915,958],[498,1421],[647,1233],[950,1256],[720,1173],[614,1119],[671,1242],[417,621],[841,1475],[919,1376],[726,921],[775,1127],[183,339],[842,1077],[237,1027],[765,1235],[952,1726],[664,1191],[926,1044],[808,1546],[305,306],[653,1358],[474,698],[386,1074],[381,1131],[668,1317],[578,1449],[331,1027],[487,946],[788,819],[565,1193],[175,1129],[141,711],[792,1729],[355,703],[1,967],[886,1028],[755,1605],[133,561],[682,1467],[368,1036],[532,904],[971,1836],[826,1447],[816,1717],[134,1128],[827,1377],[726,765],[866,981],[804,1680],[704,1624],[657,1380],[693,956],[742,1237],[181,346],[989,1061],[373,1325],[359,442],[98,119],[252,1035],[27,94],[190,1177],[6,1003],[882,1638],[763,1527],[679,919],[140,580],[594,1023],[248,378],[919,1640],[437,550],[257,888],[447,886],[753,1526],[615,1508],[66,867],[96,747],[580,675],[953,1727],[228,583],[873,926],[661,1201],[214,1133],[581,1466],[712,1472],[993,1118],[472,776],[879,1093],[797,1563],[662,1155],[529,1480],[764,1378],[478,734],[690,1119],[733,747],[530,1365],[475,1243],[485,1257],[192,1008],[755,1752],[826,1180],[432,482],[828,1242],[588,1165],[347,1064],[714,1285],[151,382],[668,764],[835,1132],[261,704],[506,1431],[379,764],[82,722],[569,1502],[560,1499],[869,1357],[144,815],[670,1568],[963,1215],[66,197],[358,800],[987,1786],[891,1619],[696,1303],[373,739],[307,683],[808,1637],[90,335],[271,1068],[811,1071],[255,1182],[472,1191],[768,879],[953,1254],[201,772],[417,1297],[731,752],[177,1165],[683,1037],[443,459],[92,403],[13,783],[303,650],[471,1213],[594,1456],[65,954],[836,1611],[632,1137],[479,1356],[183,949],[935,1031],[162,930],[244,654],[362,954],[986,1689],[667,814],[590,1059],[583,1233],[450,862],[519,597],[439,503],[681,1021],[805,1654],[821,1224],[926,1818],[540,1311],[735,1615],[482,682],[271,881],[614,758],[316,1064],[819,1415],[537,1112],[707,871],[584,1465],[920,1129],[798,1005],[661,1119],[73,722],[222,619],[182,961],[181,611],[367,965],[837,1783],[415,658],[181,691],[798,1705],[217,918],[649,677],[314,935],[233,298],[350,1181],[614,624],[305,434],[152,224],[605,1078],[315,961],[995,1273],[240,462],[48,529],[902,1460],[37,596],[140,542],[511,1044],[284,1107],[759,1217],[377,1225],[823,1052],[106,877],[334,1265],[814,1062],[523,903],[228,998],[83,585],[602,1166],[269,537],[721,760],[666,675],[260,1137],[40,429],[833,1138],[858,1415],[69,716],[680,852],[904,1781],[874,1491],[77,770],[59,452],[918,940],[980,1717],[269,385],[205,978],[865,973],[536,1445],[615,1585],[779,1106],[171,203],[705,1554],[148,508],[767,1542],[276,1143],[357,523],[731,886],[87,844],[216,946],[255,1091],[771,1752],[117,815],[3,203],[172,754],[232,933],[568,1237],[442,560],[886,1580],[46,602],[645,1408],[233,1158],[919,1748],[12,101],[265,1202],[970,1234],[299,355],[954,985],[336,593],[190,903],[896,1706],[423,1237],[527,1446],[685,1060],[855,1431],[403,729],[344,887],[689,1218],[943,1090],[639,767],[253,1154],[217,644],[209,879],[108,286],[564,634],[445,1036],[274,575],[390,600],[535,1079],[505,1419],[208,1022],[132,474],[41,415],[776,1008],[257,1092],[244,1079],[883,1296],[110,753],[88,569],[596,688],[389,1300],[417,1247],[528,1282],[52,833],[496,771],[611,905],[153,741],[552,748],[524,1357],[648,863],[899,1723],[724,859],[503,1486],[844,992],[264,471],[261,637],[998,1972],[161,1054],[185,553],[36,239],[136,630],[940,1268],[535,535]]
    test_inputs.append(big1)

    # 答案 = 1459
    big2 = [[53764,100000],[62747,100000],[61273,80082],[1534,92809],[92312,100000],[72666,83294],[7211,70344],[45032,100000],[37521,100000],[38647,61499],[99338,100000],[25271,100000],[60907,100000],[8005,85785],[4984,47156],[216,73318],[44204,58842],[5675,48382],[67104,100000],[93293,99756],[45226,45735],[96260,100000],[5614,84127],[82460,100000],[39753,100000],[35941,82775],[63191,100000],[91005,100000],[4278,56331],[54000,94563],[37747,72568],[14535,67231],[70073,93926],[4333,57616],[3033,14501],[42153,64904],[16148,43535],[19275,100000],[36302,83450],[43288,61806],[57375,100000],[11170,72089],[24263,72398],[11593,87031],[76314,88306],[75535,98412],[92632,100000],[89199,100000],[6736,67847],[19967,67686],[71407,76934],[51123,100000],[91630,100000],[1633,81308],[51003,74456],[4225,68327],[41103,56284],[79875,100000],[46804,100000],[95612,100000],[371,54857],[84836,89937],[23181,86785],[41616,100000],[97861,100000],[29301,100000],[58263,100000],[41182,100000],[62911,100000],[15866,92630],[3341,99555],[13466,73738],[42519,49011],[65693,100000],[41969,77432],[5292,50511],[85030,100000],[27083,100000],[90983,100000],[87689,100000],[53428,100000],[12393,37453],[42168,94936],[8808,70970],[34319,100000],[24501,89227],[81168,100000],[48849,100000],[9961,75788],[82506,82695],[72841,84506],[31272,41201],[46524,100000],[37761,100000],[50978,100000],[90945,100000],[18441,100000],[33054,59515],[93912,100000],[58992,100000],[85042,94662],[4449,36222],[41656,62378],[4819,43856],[70018,100000],[16812,80817],[27960,84579],[65000,100000],[29654,62435],[2788,9466],[67031,100000],[44460,65445],[74070,100000],[58761,100000],[77380,100000],[85007,93841],[16245,85767],[95409,100000],[26636,67861],[43310,100000],[61047,100000],[77019,98077],[43951,100000],[47118,100000],[90039,100000],[67233,100000],[55236,100000],[31419,91989],[68007,100000],[84335,100000],[97143,100000],[10249,72340],[41404,46941],[53688,100000],[75702,81180],[98091,100000],[67181,100000],[62980,100000],[12404,17021],[96768,100000],[7444,18397],[88986,100000],[57441,93559],[72574,100000],[43810,50289],[6983,76976],[9070,78880],[72230,100000],[47959,93884],[71397,71510],[61633,68737],[83222,100000],[89545,100000],[8375,24121],[12675,54617],[22719,80859],[92952,100000],[93576,100000],[7984,75564],[18610,88569],[28492,52958],[29238,100000],[75438,100000],[34594,47418],[42392,87358],[28800,70048],[32921,100000],[85351,100000],[99963,100000],[84752,100000],[49273,100000],[87373,100000],[85943,100000],[22443,50966],[39860,71428],[59711,81258],[75889,100000],[42494,100000],[89779,100000],[3615,57587],[94134,100000],[92083,100000],[16478,77095],[93006,100000],[1967,30026],[27733,75946],[11711,87398],[26828,73581],[54751,100000],[60895,66135],[99854,100000],[26377,84209],[95468,100000],[68553,92922],[71456,100000],[9407,44491],[43354,100000],[67786,79405],[92196,100000],[79819,92521],[93030,100000],[87719,100000],[11032,17547],[92358,100000],[64262,100000],[45827,47843],[33587,72408],[87322,100000],[41920,100000],[23063,29687],[31600,100000],[22081,52535],[9602,73785],[10230,24061],[49302,81485],[62978,82656],[56389,100000],[24140,48022],[7445,33379],[64643,100000],[74182,100000],[45646,100000],[81129,100000],[66522,67542],[72217,100000],[61909,94510],[5220,14686],[66536,100000],[62238,100000],[70907,100000],[11300,64157],[15604,79259],[2940,17595],[90342,100000],[34891,76968],[9114,63260],[74346,100000],[35177,54421],[19959,100000],[15072,81490],[22160,70222],[80745,94166],[18155,56366],[43607,100000],[29802,100000],[33693,100000],[43678,100000],[8574,16031],[53215,59578],[19711,89309],[43296,100000],[50948,90653],[41300,76732],[14077,69892],[38434,63905],[25554,57966],[92705,100000],[55236,100000],[97570,100000],[83961,100000],[30328,85389],[69546,100000],[31668,47802],[42094,42280],[51519,83711],[78734,100000],[78101,100000],[29951,69158],[31203,78267],[22872,86783],[62829,100000],[11599,13117],[11644,89119],[761,71426],[31569,42340],[57261,77160],[65869,81573],[89293,97107],[31015,96218],[99588,100000],[44768,89300],[68836,98467],[4623,100000],[50953,100000],[30406,100000],[62109,100000],[28321,100000],[47410,48395],[30332,100000],[99519,100000],[5730,12519],[13650,82374],[90069,100000],[724,94202],[21161,100000],[69398,100000],[90858,100000],[4976,82608],[89476,89550],[12574,77125],[98616,100000],[66781,100000],[41762,100000],[89714,100000],[95510,100000],[4996,29759],[97511,100000],[5642,96834],[99543,100000],[98004,100000],[47902,100000],[31001,74164],[67541,100000],[77725,100000],[95356,100000],[18226,100000],[91560,94727],[30230,56215],[37813,100000],[50830,100000],[14198,54983],[83165,100000],[2439,47393],[8631,62043],[13917,37572],[66349,100000],[42080,63327],[27813,100000],[27826,28578],[98047,100000],[86890,100000],[23735,65741],[6712,75865],[39069,85512],[54302,100000],[58975,100000],[51746,100000],[29484,46921],[86792,98651],[59300,100000],[9934,20227],[74929,84056],[88682,93675],[33211,55288],[11688,53679],[4091,29880],[5717,75457],[30350,84331],[73476,83484],[3080,79945],[64122,81111],[96495,100000],[66994,100000],[57711,75258],[99353,100000],[87829,100000],[91630,100000],[39037,54443],[89346,100000],[42083,100000],[7560,15518],[97700,100000],[42159,48993],[84153,89654],[14340,44919],[71090,100000],[51816,96015],[33157,82960],[92975,100000],[2987,85568],[99737,100000],[8046,42525],[75540,100000],[45655,100000],[33245,100000],[58882,100000],[24887,47469],[85127,100000],[14419,100000],[77926,100000],[74305,100000],[6337,49260],[93528,100000],[74593,100000],[89072,100000],[14738,73504],[9642,45252],[20982,39674],[39521,45193],[20767,56781],[42572,100000],[29023,98340],[36287,100000],[10484,29101],[56159,98358],[74502,84398],[86589,100000],[99867,100000],[52719,63587],[77168,100000],[29836,100000],[176,80104],[92226,100000],[81216,100000],[29967,68749],[12132,76990],[85167,100000],[50315,100000],[96428,100000],[64890,100000],[69069,100000],[98501,100000],[8247,69431],[93580,100000],[42906,50550],[7630,69119],[61426,100000],[52438,85592],[68649,84316],[13602,53839],[17651,100000],[2329,88591],[67019,100000],[6182,28250],[80087,100000],[72702,100000],[5947,21205],[31597,100000],[21368,100000],[96012,100000],[24402,100000],[99595,100000],[12918,40252],[14040,83552],[49704,100000],[47355,54000],[98810,100000],[24681,76298],[1671,97795],[12168,26491],[17831,100000],[89275,100000],[88946,100000],[7207,73997],[8738,33034],[67697,100000],[71446,100000],[56219,67763],[50120,100000],[28498,100000],[89076,100000],[6890,78655],[30503,32831],[40399,86283],[45686,100000],[53866,81103],[78463,100000],[14973,43718],[33959,100000],[22783,56295],[40860,56012],[48085,100000],[87596,100000],[32613,94686],[98471,100000],[69803,100000],[54899,100000],[59190,100000],[9076,34759],[75584,79233],[71237,100000],[5532,100000],[91421,100000],[66307,81395],[37012,61514],[43145,100000],[7371,96570],[63277,95838],[22566,61646],[66880,84766],[13430,30791],[69116,100000],[92024,100000],[40256,100000],[72558,100000],[55520,71950],[18775,33592],[20228,100000],[60752,100000],[47657,94906],[12077,80145],[4543,23904],[90181,100000],[33538,82585],[81216,95246],[69514,100000],[33467,82056],[78304,93128],[63713,99259],[49621,100000],[64078,100000],[18170,46984],[17353,93394],[83892,100000],[31277,63250],[86746,100000],[75477,81977],[10647,100000],[85172,100000],[79729,83468],[33169,61878],[15837,82323],[19230,27099],[35174,69064],[55482,58871],[17855,37768],[51410,97029],[95855,100000],[15642,16293],[49609,82694],[23309,60885],[23936,58888],[35093,56596],[89890,100000],[49846,90453],[81162,100000],[97291,100000],[17500,76308],[62885,100000],[13423,82500],[29491,100000],[98681,100000],[32641,72222],[52332,100000],[52222,100000],[95995,100000],[15243,83042],[76047,100000],[85739,100000],[7278,93915],[65255,100000],[94861,100000],[33865,78970],[38936,100000],[46549,66625],[74368,100000],[28686,57118],[11261,30328],[19299,71928],[14640,34030],[21661,95267],[4961,20389],[9545,38930],[23462,59079],[48796,68378],[23641,43046],[27774,47508],[43245,70925],[82746,100000],[76836,100000],[84300,84604],[70491,100000],[8945,71727],[17139,56684],[28329,100000],[83671,94887],[63145,100000],[97858,100000],[41935,75972],[74560,100000],[65040,100000],[39643,93499],[59250,100000],[58693,96624],[37766,72730],[96818,100000],[83242,100000],[45033,45514],[36211,56996],[23442,100000],[95857,100000],[50887,64421],[57235,100000],[83169,100000],[36283,100000],[98649,100000],[18446,40449],[91614,100000],[93047,100000],[37219,59178],[5396,55508],[53759,64344],[16264,29956],[17728,27308],[78459,100000],[52788,55597],[40218,100000],[42789,46941],[47431,81904],[80429,97191],[43387,93751],[89781,100000],[57537,68838],[27452,88273],[41349,100000],[21613,54056],[3117,85709],[71518,100000],[26376,49313],[88350,100000],[31625,83702],[93044,100000],[23472,55087],[16724,20623],[87807,100000],[70226,100000],[10433,49622],[27332,95172],[99849,100000],[63799,100000],[12793,80542],[84932,96949],[43003,49280],[20415,100000],[61575,92042],[87681,100000],[42672,95962],[10214,55191],[60383,80891],[48865,61164],[65349,100000],[23946,100000],[6181,71516],[87425,89575],[74314,100000],[38043,75247],[15953,25645],[96795,100000],[45237,93406],[1124,29996],[20410,45324],[93416,100000],[5516,98395],[40768,55962],[79719,100000],[94893,100000],[84675,100000],[27714,94053],[79062,100000],[14434,24172],[7065,35658],[98214,100000],[33935,93748],[52421,100000],[86874,100000],[16210,98554],[38556,78452],[82307,100000],[19474,99823],[75817,100000],[31677,36735],[91292,100000],[82752,83951],[55118,88700],[23449,100000],[87842,92685],[95674,100000],[38679,55045],[27588,73761],[32109,77025],[93635,100000],[24385,100000],[19570,71242],[77601,100000],[98343,100000],[33743,57846],[34935,87321],[44112,100000],[92684,100000],[7938,39893],[36213,75627],[28713,100000],[68289,100000],[90716,91076],[56030,100000],[63120,100000],[69570,100000],[2755,79075],[10575,100000],[60454,96425],[57249,82398],[57896,100000],[96789,100000],[71936,100000],[97745,100000],[46133,100000],[40205,100000],[87873,100000],[85674,100000],[69419,94507],[32811,53327],[23289,42829],[48173,52209],[65232,100000],[59231,100000],[61999,100000],[24039,100000],[44001,100000],[69801,100000],[74697,100000],[37347,91210],[26430,76314],[46130,51520],[83285,100000],[91932,100000],[26595,51847],[84451,100000],[15244,23014],[62866,100000],[30619,100000],[63481,100000],[49491,98731],[4067,35819],[97741,97888],[82223,100000],[76291,100000],[22782,82896],[63943,100000],[28217,100000],[4146,52468],[5778,44166],[78311,100000],[95221,100000],[59917,100000],[17872,53761],[98116,100000],[92358,100000],[36218,77408],[81872,100000],[32907,68953],[69386,100000],[53985,98830],[94967,100000],[9592,94121],[98209,100000],[30437,55072],[44968,100000],[64279,100000],[21950,85455],[57253,100000],[21045,72778],[23292,100000],[78977,100000],[69581,100000],[19918,54737],[48949,65608],[57980,75417],[33840,37209],[17720,80741],[90223,100000],[12875,94199],[54146,59041],[83623,100000],[54238,97750],[21728,93053],[8179,17513],[20331,100000],[57953,100000],[34018,100000],[71692,75628],[37288,81521],[93728,100000],[65536,100000],[55395,97121],[94109,100000],[40535,70937],[29149,100000],[54594,93328],[2292,48819],[42639,100000],[24460,73963],[1265,47289],[80064,93292],[25054,97452],[36682,100000],[96608,100000],[85666,100000],[97011,100000],[79234,86869],[323,72192],[31298,67718],[55357,100000],[36354,46869],[26926,71726],[77104,83172],[39738,100000],[25585,76321],[3292,16256],[96548,100000],[34870,61253],[98088,100000],[65615,91726],[1884,51247],[77126,100000],[49185,62056],[12716,65912],[80975,100000],[22900,56567],[10121,55668],[74947,95080],[94992,100000],[49174,100000],[60882,100000],[61123,100000],[78488,100000],[36553,47902],[53584,90885],[21647,100000],[46825,100000],[48179,100000],[55842,88676],[56874,78339],[5754,61883],[98915,100000],[80392,100000],[84079,100000],[90908,100000],[61198,73925],[82071,100000],[59886,100000],[20055,52472],[17665,100000],[51644,100000],[72127,100000],[53660,100000],[26515,57780],[74888,100000],[57452,99762],[97309,100000],[2773,37529],[7029,71333],[78026,100000],[23798,91992],[5043,44779],[84682,100000],[77224,100000],[81450,100000],[3485,56948],[62306,97626],[24311,100000],[57430,100000],[76160,100000],[24246,98782],[37892,87426],[16132,38900],[40794,52023],[47983,100000],[85067,100000],[61343,99718],[13366,50340],[60129,82949],[98116,100000],[85397,100000],[38938,100000],[26694,65411],[56837,100000],[72874,100000],[50568,100000],[29074,98182],[37822,38658],[73935,100000],[46106,100000],[87402,100000],[99838,100000],[55891,100000],[67112,100000],[9980,75991],[85053,100000],[60840,100000],[28505,100000],[90989,100000],[75715,100000],[24762,100000],[62089,100000],[62903,72999],[18966,29878],[29886,92889],[957,100000],[9171,75130],[46935,100000],[52172,100000],[60657,92032],[37106,100000],[30406,100000],[16096,16652],[48444,100000],[85765,100000],[34582,50816],[88859,100000],[28695,55565],[91906,100000],[77777,78454],[15421,50054],[24013,61628],[52876,100000],[84277,100000],[37174,83763],[1544,32824],[64976,100000],[93933,100000],[9822,46287],[9329,56722],[85287,100000],[9433,40034],[68895,100000],[10907,26564],[2557,85633],[49383,71721],[64386,100000],[38493,100000],[28252,38308],[57513,80071],[39881,100000],[38457,80760],[29739,53270],[12727,75429],[88932,100000],[85475,100000],[94591,100000],[68916,81845],[47612,100000],[82415,100000],[80802,100000],[97952,100000],[51036,100000],[64269,100000],[20976,44234],[81697,90554],[83596,100000],[8763,25666],[80285,100000],[96557,100000],[61267,100000],[42827,99465],[28417,82043],[59743,68194],[43097,100000],[16084,100000],[67202,100000],[62701,100000],[98912,100000],[53829,63818],[47756,85835],[74847,85192],[16550,70758],[27943,82010],[78741,100000],[22379,100000],[21766,100000],[70891,100000],[55049,100000],[50661,55650],[15835,97159],[30221,100000],[44547,47850],[14201,14569],[20366,81791],[75146,100000],[97520,100000],[48028,100000],[95654,100000],[64029,87044],[8758,100000],[91898,92676],[34897,82953],[83943,100000],[69028,100000],[73044,100000],[70184,100000],[7266,89892],[22349,100000],[18954,100000],[18774,88377],[38121,50199],[64543,100000],[22543,52528],[91896,100000],[91387,100000],[84457,100000],[49340,65466],[86613,100000],[42735,48594],[94099,100000],[97491,100000],[68192,100000],[76042,100000],[12835,84038],[78353,100000],[58464,100000],[92150,100000],[64208,75099],[76716,100000],[80100,91827],[40140,100000],[94721,100000],[36715,100000],[31024,42034],[65415,99235],[94156,100000],[44961,73908],[13058,44167],[18443,23224],[2015,99732],[46463,100000],[46795,100000],[4986,21181],[65635,100000],[79235,81928],[7943,12045],[2546,6756],[5023,38432],[43124,100000],[62812,100000],[77645,100000],[37193,70446],[20664,94460],[48734,100000],[18426,38577],[36411,100000],[42208,43887],[17842,47293],[73096,100000],[59349,100000],[42917,100000],[26247,33001],[76138,100000],[53759,100000],[13980,100000],[36137,50793],[62923,100000],[37882,88973],[35242,56968],[74901,100000],[51784,100000],[86523,100000],[11008,100000],[54347,63427],[23625,31727],[2308,100000],[79091,100000],[74832,98470],[33607,100000],[54709,58988],[17212,38785],[50913,95190],[47798,100000],[41835,78888],[96738,100000],[94614,100000],[65950,100000],[54837,64171],[98319,100000],[66173,100000],[17247,100000],[76986,100000],[90378,100000],[64179,100000],[51590,100000],[22950,73598],[17692,98517],[87872,100000],[20915,26157],[51831,83609],[68996,76229],[8870,82515],[42347,96226],[55916,100000],[99862,100000],[5703,19843],[36415,65407],[46923,79990],[38563,91291],[4394,58674],[64225,100000],[74144,100000],[43683,100000],[68283,100000],[6758,12987],[98212,100000],[69626,100000],[40828,64202],[11388,94166],[88539,100000],[64638,67416],[72937,100000],[86822,93418],[52234,66940],[68341,100000],[66808,70808],[55775,100000],[69062,100000],[51919,100000],[60673,100000],[82333,100000],[86477,100000],[94196,100000],[51958,100000],[58725,100000],[68340,100000],[59075,73824],[9978,31989],[29401,70962],[1575,65475],[62649,99534],[5730,12167],[67837,78604],[25141,88685],[28554,100000],[97346,100000],[85838,86415],[64189,94757],[73235,100000],[81383,100000],[23478,86041],[30728,73673],[79685,92254],[40793,41413],[12736,43115],[60943,72513],[38897,56422],[72419,100000],[55127,56667],[32949,57225],[34819,89095],[78750,100000],[45281,68338],[78122,100000],[74643,100000],[80073,100000],[31290,72387],[90900,100000],[12505,83118],[66289,100000],[32884,74364],[3957,91754],[17351,90768],[59594,100000],[83663,89747],[51582,100000],[1388,37902],[97268,100000],[36865,42080],[79914,100000],[77635,100000],[691,56801],[1765,6359],[72991,100000],[28172,100000],[42650,69814],[39492,100000],[95214,100000],[10200,54352],[18958,97600],[71336,100000],[80881,100000],[73836,100000],[92057,100000],[40128,100000],[52306,100000],[45687,99501],[15862,24412],[4623,7621],[36693,84173],[59849,100000],[23252,32465],[62519,100000],[47898,100000],[90991,100000],[64924,100000],[97574,100000],[41115,100000],[59723,100000],[71150,100000],[73677,100000],[58706,78462],[58558,100000],[71721,100000],[24495,72474],[85129,100000],[64360,100000],[88226,100000],[45791,100000],[78848,100000],[98824,100000],[68888,79844],[22626,100000],[27397,60378],[65108,78642],[40375,45048],[15204,100000],[16251,52468],[13613,80888],[88308,100000],[9343,37794],[68650,100000],[19392,88674],[36636,59732],[87843,100000],[7994,53974],[35192,57226],[25935,91640],[7622,9917],[76604,100000],[14475,40397],[62073,73409],[31418,48951],[7295,21206],[77691,100000],[53019,83569],[73906,100000],[12866,33644],[32285,97781],[9098,48255],[2366,43458],[87393,100000],[83825,90989],[25761,42774],[19027,61075],[78730,100000],[72378,77753],[73382,100000],[61497,70644],[12986,86628],[17764,91147],[9821,49135],[6325,98139],[82980,100000],[24743,67287],[18609,90252],[38677,100000],[69239,100000],[55229,100000],[88820,100000],[71500,100000],[9493,66950],[40171,47570],[86778,100000],[25999,79996],[54072,94536],[85287,95489],[5453,39078],[38220,100000],[99925,100000],[51171,100000],[33326,77537],[15772,55366],[64691,75266],[56661,100000],[80784,100000],[54956,100000],[55296,92258],[72602,100000],[86880,100000],[20474,66348],[46331,92652],[37809,81708],[31671,100000],[77320,100000],[15314,65894],[4849,13852],[32106,84965],[76005,88709],[81291,92830],[41083,100000],[30552,100000],[58546,98580],[80591,100000],[43919,89574],[26148,60689],[21291,96310],[72389,87313],[87404,100000],[91751,100000],[93005,100000],[54869,100000],[11348,92185],[33546,65619],[70506,74140],[18542,73771],[88586,100000],[41065,92521],[81275,100000],[18042,65226],[49364,70693],[58221,100000],[54581,100000],[77394,100000],[42683,100000],[45792,100000],[50722,100000],[89308,100000],[82689,100000],[28674,98705],[32379,40738],[6705,87442],[85162,100000],[52001,100000],[63929,100000],[76052,91216],[90982,100000],[99429,100000],[2536,94966],[5351,100000],[513,78670],[7940,34339],[25898,49368],[56458,100000],[21297,47146],[40261,100000],[37405,76074],[19024,100000],[62031,100000],[16903,77976],[23694,100000],[19359,91688],[41783,46189],[49571,82210],[72847,100000],[99531,100000],[19006,81021],[93191,100000],[45808,76371],[56837,100000],[42741,66768],[14254,100000],[85251,100000],[86228,92757],[37429,100000],[98449,100000],[72654,100000],[96208,100000],[90330,100000],[84995,100000],[5109,66302],[41965,96595],[90777,100000],[16090,50204],[145,95013],[57833,100000],[25787,66272],[31487,100000],[48288,100000],[24926,64511],[69066,100000],[44414,100000],[8978,59786],[8648,63349],[90249,100000],[10967,95477],[9721,54196],[65973,100000],[61002,72042],[35575,100000],[95134,100000],[81053,100000],[48235,91760],[33223,80217],[11775,80444],[31483,44423],[68427,100000],[23323,64359],[56675,100000],[20229,49604],[39308,100000],[13492,22461],[53441,61139],[17589,60192],[66545,100000],[92350,100000],[37444,68518],[13716,71062],[87738,100000],[15450,38824],[59455,100000],[23488,100000],[23622,44102],[40934,100000],[52177,63237],[57031,100000],[97870,100000],[66336,100000],[82716,100000],[36854,43711],[78635,86998],[23845,100000],[68676,91663],[64463,80997],[39107,100000],[89260,100000],[60119,99700],[51995,100000],[10865,23072],[93517,98844],[61274,100000],[87443,100000],[21163,100000],[35758,85692],[44138,100000],[21830,60691],[70122,100000],[44369,50111],[89246,100000],[47519,88941],[73471,94733],[53059,100000],[57536,58087],[18397,60524],[33781,56517],[60967,76463],[27981,79580],[25312,67207],[28473,80973],[83710,100000],[48958,100000],[59937,98451],[86199,100000],[23050,100000],[41607,97441],[35653,48544],[22606,31945],[8035,84870],[55404,100000],[73478,100000],[50524,100000],[95208,100000],[30818,100000],[37163,74068],[72450,88822],[90039,100000],[74954,100000],[32837,40520],[63320,100000],[92354,100000],[62867,100000],[12301,65041],[3382,11158],[8990,100000],[43687,100000],[76459,96437],[17663,59943],[17006,73096],[35249,55303],[10559,44794],[56595,100000],[16164,51981],[62280,72626],[28323,47620],[15583,24024],[28643,56306]]
    test_inputs.append(big2)

    res_list = []
    s = 0
    e = 6
    for i in range(s, e):
        test = test_inputs[i]
        res_one = max_events_v4(test)
        print(res_one)
        res_list.append(res_one)

    print(res_list)