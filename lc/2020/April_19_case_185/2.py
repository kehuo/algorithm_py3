
# @File: 2.py
# @Author: Kevin Huo
# @Date: 2020/4/19


from typing import List

def displayTable(orders: List[List[str]]) -> List[List[str]]:
    # items 是菜单列表, d是统计
    items = ["Table"]
    d = {}
    for order in orders:
        # order = ["James","12","Fried Chicken"]
        table_num = order[1]
        food = order[2]
        if food not in items:
            items.append(food)
        if table_num not in d:
            d[table_num] = {food: 1}
            continue
        if food not in d[table_num]:
            d[table_num][food] = 1
            continue
        d[table_num][food] += 1

    # 写入最终结果
    res = []
    res.append(items)
    # sorted_d = [3, 5, 10] 按照桌号生序排列
    sorted_d = sorted(d, key=lambda x:int(x))
    # print(sorted_d)
    checked = items[1:]
    print("排序前: %s" % checked)
    checked.sort()
    print("排序后: %s" % checked)
    for idx in sorted_d:
        # one = {"water": 2, "chicken": 1}
        one = d[idx]
        tmp = [idx]

        for f in checked:
            # print("f=%s, tmp=%s" % (f, tmp))
            if f not in one:
                tmp.append("0")
            else:
                tmp.append(str(one[f]))
        res.append(tmp)

    return res


if __name__ == '__main__':
    tests = [
        [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
         ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    ]

    t = tests[0]
    r = displayTable(t)
    print(r)
