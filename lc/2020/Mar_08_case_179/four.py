# @File: four
# @Author: Kevin Huo
# @LastUpdate: 3/8/2020 1:07 AM


def frogPosition(n, edges, t, target):
    """jumped-已经跳过的节点"""
    prob = 0

    d = dict()
    for i in edges:
        if i[0] not in d:
            d[i[0]] = [i[1]]
            continue
        d[i[0]].append([i[1]])

    jumped = []
    c = 0
    target_copy = target
    while True:
        if c > t:
            break
        for i in d:
            if target_copy in d[i]:
                c += 1
                target_copy = i
                continue

