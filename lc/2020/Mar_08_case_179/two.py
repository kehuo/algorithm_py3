# @File: tow
# @Author: Kevin Huo
# @LastUpdate: 3/8/2020 1:06 AM


def numTimesAllBlue(light):
    """
    https://leetcode-cn.com/problems/bulb-switcher-iii/

    opened: 已经打开过的灯泡的索引
    largest: 已经打开过的灯泡中, 索引值最大的那个

    思路:
    1. 每打开一个灯泡, 就把索引写入opened数组. 并且更新 largest 变量.
    2. 当打开第n个灯泡时, 如果 largest == len(opened), 那么res +=1

    比如: 当largest = 3, 也就是最大的灯泡索引是3, 那么要保证123灯都亮, 才能res+1, 所以当前opened  = [1, ,2, 3], 长度也等于3.
    所以 largest = len(opened) ,这时可以 res += 1
    """
    opened = []

    res = 0

    largest = None
    for i in range(len(light)):
        all_idx = light[i] - 1
        opened.append(all_idx)
        if largest is None:
            largest = light[i]
        else:
            if largest < light[i]:
                largest = light[i]

        if len(opened) == 1:
            if all_idx == 0:
                res += 1
                continue

        if largest == len(opened):
            res += 1
        print("i=%s, all_idx=%s, largest=%s, opened=%s" % (i, all_idx, largest, opened))
    return res


if __name__ == '__main__':
    test = [[1, 2, 3, 4, 5, 6], [2, 1, 3, 5, 4]]
    start = 0
    end = 2
    all_res = []
    for j in range(start, end):
        c = numTimesAllBlue(test[j])
        print(c)
        all_res.append(c)
        print("")
    # 正确答案: [6, 3]
    print("所有答案: %s" % all_res)
