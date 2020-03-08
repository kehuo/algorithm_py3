# @File: tow
# @Author: Kevin Huo
# @LastUpdate: 3/8/2020 1:06 AM


def numTimesAllBlue(light):
    """0-off, 1-on, 2-blue"""
    all_light = [0] * len(light)
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
    test = [[1,2,3,4,5,6], [2,1,3,5,4]]
    start = 0
    end = 2
    for j in range(start, end):
        c = numTimesAllBlue(test[j])
        print(c)
        print("")
