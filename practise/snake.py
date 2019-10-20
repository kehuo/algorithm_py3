def build_raw_res(row_length, column_length):
    """
    功能函数 -- 创建初始res 2维列表
    """

    res = []
    for _ in range(row_length):
        tmp = []
        for _ in range(column_length):
            tmp.append("empty")
        res.append(tmp)

    return res


def move_i_j_by_direction(direction, i, j):
    """
    功能函数 -- 根据当前i, j, 方向，返回下一个数字的 i, j
    """

    # i行， j列
    if direction == "right":
        j += 1
    elif direction == "down":
        i += 1
    elif direction == "left_down":
        i += 1
        j -= 1
    elif direction == "right_up":
        i -= 1
        j += 1

    return i, j


def snake(raw, m, n):
    """
    主函数
    m行, n列
    raw_data = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]
    res = [
            [1, 3, 4, 9],
            [2, 5, 8, 10],
            [6, 7, 11, 12]
    ]

    第一步:
    若 i ==0 and j == 0 --> res[i][j] = raw[i][j]

    然后:
    4条边上的处理方式:
    左边j=0:
    >> 尝试 右上 --> 若右上 != empty --> 向下一格 --> 再右上

    右边j=len(raw[i]) - 1:
    >> 尝试 左下 --> 若左下 != empty --> 向下一格 --> 再左下

    上边i=0:
    >> 尝试 左下 --> 若左下 != empty --> 向右一格 --> 再左下

    下边i=len(raw[i] - 1):
    >> 尝试 右上 --> 若右上 != empty --> 向右一格 --> 再右上

    res = [
        [1, 2, 6, 7],  # res[0]
        [3, 5, 8, 11],  # res[1]
        [4, 9, 10, 12]  # res[2]
    ]

    流程
    i=0, j=0 >> num=raw[0]=1 >> res[0][0]=1 >> 判断下个方向 >> 当前i=0, j=0(开始) >> 向右(j+1) >> i=0, j=1.
    i=0, j=1 >> num=raw[1]=2 >> res[0][1]=2 >> 判断下个方向 >> 当前i=0, j>0(顶部) >> 左下是empty >> 左下(i+1, j-1) >> i=1, j=0
    i=1, j=0 >> num=raw[2]=3 >> res[1][0]=3 >> 判断下个方向 >> 当前i=1, j=0(左边) >> 右上不为empty >> 向下(i+1) >> i=2, j=0
    i=2, j=0 >> num=raw[3]=4 >> res[2][0]=4 >> 判断下个方向 >> 当前i>0, j=0(底部+左边) >> 右上是empty >> 右上(i-1, j+1) >> i=1, j=1
    i=1, j=1 >> num=raw[4]=5 >> res[1][1]=5 >> 判断下个方向 >> 当前i不为0也不为len(m)-1, j不为0也不为len(n)-1 >> 方向不变 >> 右上(i-1, j+1) >> i=0, j=2
    i=0, j=2 >> num=raw[5]=6 >> res[0][2]=6 >> 判断下个方向 >> 当前i=0, j>0(顶部) >> 左下不为empty >> 向右(j+1) >> i=0, j=3
    i=0, j=3 >> num=raw[6]=7 >> res[0][3]=7 >> 判断下个方向 >> 当前i=0, j=len(n)-1>0(顶部+右边) >> 左下为empty >> 左下(i+1, j-1) >> i=1, j=2
    i=1, j=2 >> num=raw[7]=8 >> res[1][2]=8 >> 判断下个方向 >> 当前i和j都不是0或者len()-1 >> 方向不变 >> 左下(i+1, j-1) >> i=2, j=1
    i=2, j=1 >> num=raw[8]=9 >> res[2][1]=9 >> 判断下个方向 >> 当前i=len(m)-1, j>0(底部) >> 右上不为empty >> 向右(j+1) >> i=2, j=2
    i=2, j=2 >> num=raw[9]=10 >> res[2][2]=10 >> 判断下个方向 >> 当前i=len(m)-1, j>0(底部) >> 右上为empty >> 右上(i-1, j+1) >> i=1, j=3
    i=1, j=3 >> num=raw[10]=11 >> res[1][3]=11 >> 判断下个方向 >> 当前i>0, j=len(n)-1(右边) >> 左下不是empty >> 向下(i+1) >> i=2, j=3
    i=2, j=3 >> num=raw[11]=12 >> res[2][3]=12 >> END
    """

    # 3行 x 4列 矩阵
    res = build_raw_res(m, n)

    direction = "right"
    i, j = 0, 0
    count = 0
    while True:
        num = raw[count]
        print(i, j, num)

        res[i][j] = num

        count += 1

        # 遇到最后一个数字, 则说明 raw 中的数字全部处理，跳出循环
        if count == len(raw) - 1:
            res[m-1][n-1] = raw[-1]
            break

        # 如果row或者col = 1， 那特殊处理
        if m == 1:
            i, j = move_i_j_by_direction("right", i, j)
            continue
        if n == 1:
            i, j = move_i_j_by_direction("down", i, j)
            continue

        # 以下程序判断: 将num填到 res 中的哪个位置
        # 顶部
        if i == 0:
            if j == 0:
                i, j = move_i_j_by_direction(direction, i, j)
                continue

            # 当前 顶部 >> 判断左下
            else:
                if res[i+1][j-1] == "empty":
                    direction = "left_down"
                    i, j = move_i_j_by_direction(direction, i, j)
                    continue
                else:
                    # 右上角
                    if j == n - 1:
                        direction = "down"
                        i, j = move_i_j_by_direction(direction, i, j)
                        continue
                    else:
                        direction = "right"
                        i, j = move_i_j_by_direction(direction, i, j)
                        direction = "left_down"
                        continue

        # 底部 >> 判断右上
        elif i == m - 1:
            if res[i-1][j+1] == "empty":
                direction = "right_up"
                i, j = move_i_j_by_direction(direction, i, j)
                continue
            else:
                direction = "right"
                i, j = move_i_j_by_direction(direction, i, j)
                direction = "right_up"
                continue

        # 不在顶部, 也不在底部
        else:
            # 当前左边 >> 判断右上
            if j == 0:
                if res[i-1][j+1] == "empty":  # 可以右上
                    direction = "right_up"
                    i, j = move_i_j_by_direction(direction, i, j)
                    continue
                else:  # 不能右上，只能往右
                    direction = "down"
                    i, j = move_i_j_by_direction(direction, i, j)
                    direction = "right_up"
                    continue

            # 当前右边 >> 判断左下
            elif j == n - 1:
                if res[i+1][j-1] == "empty":
                    direction = "left_down"
                    i, j = move_i_j_by_direction(direction, i, j)
                    continue
                else:
                    direction = "down"
                    i, j = move_i_j_by_direction(direction, i, j)
                    direction = "left_down"
                    continue
            # 非顶非底, 非左非右, 使用当前方向
            else:
                i, j = move_i_j_by_direction(direction, i, j)

    return res


if __name__ == '__main__':
    """
    raw = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    res = [
        [1, 2, 6, 7],
        [3, 5, 8, 11],
        [4, 9, 10, 12]
    ]
    """

    # raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    raw_data = range(1, 11)
    row = 10
    col = 1
    print("输入:%d x %d: %s" % (row, col, raw_data))

    snake_list = snake(raw_data, row, col)
    print("结果:")
    for r in snake_list:
        print(r)
