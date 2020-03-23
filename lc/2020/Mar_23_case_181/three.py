# @File: three
# @Author: Kevin Huo
# @LastUpdate: 3/22/2020 12:42 AM

import os
import json
from copy import deepcopy


def hasValidPath(grid):
    class Node(object):
        """
        """

        def __init__(self, node_idx):
            """
            self.idx[0] 是该节点在 grid 所在的行 (比如第0行)
            self.idx[1] 是该节点在 grid 所在的列
            is_root: 只有 grid[0][0] 是根节点
            """
            self.idx = node_idx
            self.is_root = True if node_idx == [0, 0] else False
            self.next = {"node": None, "direction": None}

            self.valid = True
            if (self.idx[0] < 0) or (self.idx[1] < 0) or (self.idx[0] >= len(grid)) or (self.idx[1] >= len(grid[0])):
                print("当前node非法: %s" % self.idx)
                self.valid = False

        def find_next_node(self, _direction_map, _visited):
            """
            找到当前节点的所有可能的 下一个节点
            当 self.is_root -- True >> 直接返回 False
            当self.is_root == False时, 肯定只返回一个结果

            下面这个map的意思, 是说对于值为1的节点, 他的下一个节点的值, 只可能在自己的 left 或者 right 侧.
            _direction_map = {1: ["left", "right"],
                              2: ["up", "down"],
                              3: ["left", "down"],
                              4: ["right", "down"],
                              5: ["left", "up"],
                              6: ["right", "up"]}
            """
            if (self.valid is False) or (self.is_root is True):
                return
            _curr_value = grid[self.idx[0]][self.idx[1]]
            for _available_direction in _direction_map[_curr_value]:
                _tmp_idx = deepcopy(self.idx)
                # print("循环开始, _tmp_idx=%s" % _tmp_idx)
                if _available_direction == "up":
                    _tmp_idx[0] -= 1
                elif _available_direction == "down":
                    _tmp_idx[0] += 1
                elif _available_direction == "left":
                    _tmp_idx[1] -= 1
                elif _available_direction == "right":
                    _tmp_idx[1] += 1
                # print("循环中, 当前方向%s, _tmp_idx=%s" % (_available_direction, _tmp_idx))
                _tmp_node = Node(_tmp_idx)
                if _tmp_node.valid:
                    if _tmp_idx not in _visited:
                        # 如果tmp_node 是一个合法node, 那么写入node.next
                        self.next["node"] = _tmp_node
                        self.next["direction"] = _available_direction
            # print("%s值%s, 它的下一个node可能得方向是%s :下一个node是 %s, next_direction=%s" % (self.idx, _curr_value, _direction_map[_curr_value], self.next["node"].idx, self.next["direction"]))

    class Path(object):
        def __init__(self, start_node, max_row, max_col):
            self.start_node = start_node
            self._visited = [[0, 0]]
            self.max_row = max_row
            self.max_col = max_col
            self.has_valid_path = True

        def find_valid_path_for_single_node(self, _direction_map, _node_map):
            """
            搜索一个(非root)节点的路径
            """
            # 1. 有点多余, 但是宁可多写, 也避免报错
            if self.start_node.idx == [0, 0]:
                self.has_valid_path = False
                return

            # 对于 _node, 使用 while True 循环, 判断他是否可以顺利走到 grid[max_row - 1][max_col - 1]
            c = 0
            while True:
                c += 1
                # print("寻找节点循环, 当前node=%s" % self.start_node.idx)
                if self.start_node.idx == [self.max_row - 1, self.max_col - 1]:
                    # print("已到达终点, curr_idx = %s, 退出循环" % self.start_node.idx)
                    break
                # time.sleep(1)

                # 将当前 node 的 idx 放入 visited, 表明已经访问过该节点
                self._visited.append(self.start_node.idx)

                # 根据主函数中定义的 direction_map, 找到唯一的 "下一个节点"
                self.start_node.find_next_node(_direction_map=_direction_map, _visited=self._visited)
                if self.start_node.next["node"] is None:
                    self.has_valid_path = False
                    return

                curr_value = grid[self.start_node.idx[0]][self.start_node.idx[1]]
                next_node = self.start_node.next["node"]
                next_direction = self.start_node.next["direction"]

                next_value = grid[next_node.idx[0]][next_node.idx[1]]
                # print("curr_idx=%s, next_idx=%s, next_value=%s, next_direction=%s" % (
                #     self.start_node.idx, next_node.idx, next_value, next_direction
                # ))

                # 若同时符合这些要求, 则可以作为下一个节点进行进一步的搜索.
                if (0 <= next_node.idx[0] < m) \
                        and (0 <= next_node.idx[1] < n) \
                        and (self.start_node.idx != next_node.idx) \
                        and (next_value in node_map[curr_value][next_direction]):
                    self.start_node = next_node
                    continue
                else:
                    self.has_valid_path = False
                    break
            print("一共经历了%d个节点" % c)

    # 主函数开始
    # 最多 300 行, 300 列
    m = len(grid)
    n = len(grid[0])
    res = True
    if m == 1 and n == 1:
        return res
    if grid[0][0] == 5:
        res = False
        return res

    # 这个Map存储了: 对于一个节点, 他支持的"下一个节点"的值
    node_map = {
        1: {"right": [1, 3, 5],
            "left": [1, 4, 6]},
        2: {"up": [2, 3, 4],
            "down": [2, 5, 6]},
        3: {"left": [1, 4, 6],
            "down": [2, 5, 6]},
        4: {"right": [1, 3, 5],
            "down": [2, 5, 6]},
        5: {"left": [1, 4, 6],
            "up": [2, 3, 4]},
        6: {"up": [2, 3, 4],
            "right": [1, 3, 5]}
    }

    # 该Map用来寻找一个(非root)节点的唯一一个"下一个节点"
    direction_map = {1: ["left", "right"],
                     2: ["up", "down"],
                     3: ["left", "down"],
                     4: ["right", "down"],
                     5: ["left", "up"],
                     6: ["right", "up"]}

    # 该map用来获得不同 root 节点的 "下一个节点" - 我将他和 direction_map 单独分开的原因是: 对于值=4的root节点, 它有2个能走的下一个节点, 比较麻烦
    start_node_map = {1: [[0, 1, "right"]],
                      2: [[1, 0, "down"]],
                      3: [[1, 0, "down"]],
                      4: [[1, 0, "down"], [0, 1, "right"]],
                      5: [],
                      6: [[0, 1], "right"]}

    root_value = grid[0][0]
    for each_start_node_idx in start_node_map[root_value]:
        sliced_each_node_idx = each_start_node_idx[:2]
        s = Node(sliced_each_node_idx)
        # print("路径的第一个子节点: %s" % s.idx)
        if grid[each_start_node_idx[0]][each_start_node_idx[1]] not in node_map[root_value][each_start_node_idx[2]]:
            res = False
            continue

        p = Path(start_node=s, max_row=m, max_col=n)
        p.find_valid_path_for_single_node(direction_map, node_map)
        res = p.has_valid_path
        if res is True:
            return res
    return res


def hasValidPath_v2(grid):
    """
    todo 已经把类 和 deepcopy 都删了, 但是还会超时
    """
    def __is_valid_n(__n):
        if (__n[0] < 0) or (__n[1] < 0) or (__n[0] >= len(grid)) or (__n[1] >= len(grid[0])):
            return False
        return True

    def __find_next_n(__curr_n, __direction_map, __visited):
        """功能函数 -- 找到当前节点的下一个节点"""
        # print("__curr_n=%s, 值%s" % (__curr_n, grid[__curr_n[0]][__curr_n[1]]))
        __next_n = []
        __next_n_direction = None
        if (not __is_valid_n(__curr_n)) or (__curr_n == [0, 0]):
            return __next_n, __next_n_direction

        __curr_value = grid[__curr_n[0]][__curr_n[1]]
        for __available_direction in __direction_map[__curr_value]:
            __row, __col = __curr_n[0], __curr_n[1]
            if __available_direction == "up":
                __row -= 1
            elif __available_direction == "down":
                __row += 1
            elif __available_direction == "left":
                __col -= 1
            elif __available_direction == "right":
                __col += 1
            if __is_valid_n([__row, __col]):
                if [__row, __col] not in __visited:
                    # 如果tmp_node 是一个合法node, 那么写入node.next
                    __next_n = [__row, __col]
                    __next_n_direction = __available_direction
        # print("最终__next_n=%s, 方向%s" % (__next_n, __next_n_direction))
        return __next_n, __next_n_direction

    node_map = {
        1: {"right": [1, 3, 5],
            "left": [1, 4, 6]},
        2: {"up": [2, 3, 4],
            "down": [2, 5, 6]},
        3: {"left": [1, 4, 6],
            "down": [2, 5, 6]},
        4: {"right": [1, 3, 5],
            "down": [2, 5, 6]},
        5: {"left": [1, 4, 6],
            "up": [2, 3, 4]},
        6: {"up": [2, 3, 4],
            "right": [1, 3, 5]}
    }

    start_map = {1: [[0, 1, "right"]],
                 2: [[1, 0, "down"]],
                 3: [[1, 0, "down"]],
                 4: [[1, 0, "down"], [0, 1, "right"]],
                 5: [],
                 6: [[0, 1, "right"]]}

    # 该Map用来寻找一个(非root)节点的唯一一个"下一个节点"
    direction_map = {1: ["left", "right"],
                     2: ["up", "down"],
                     3: ["left", "down"],
                     4: ["right", "down"],
                     5: ["left", "up"],
                     6: ["right", "up"]}

    # 主函数从这里开始
    if len(grid) == 1 and len(grid[0]) == 1:
        return True
    if grid[0][0] == 5:
        return False

    root = grid[0][0]
    res = True
    for one in start_map[root]:
        d = one[2]
        n = one[:2]

        # 特殊情况 grid = [[2, 6]], len(grid) = 1, len(grid[0]) = 2, n = [1, 0]
        if (n[0] > len(grid) - 1) or (n[1] > len(grid[0]) - 1):
            return False

        if grid[n[0]][n[1]] not in node_map[root][d]:
            # 比如 root, 即[0, 0] 的值为1, 是连接左右的; 但是n, 即[0, 1]的值为2, 是连上下的, 因为root和n无法连通, 故返回False
            return False

        # 对于 n, 使用 while True 循环, 判断他是否可以顺利走到grid的最后一个节点上.
        c = 1
        visited = [[0, 0]]
        while True:
            c += 1
            # print("寻找节点循环, 当前node=%s" % self.start_node.idx)
            if n == [len(grid) - 1, len(grid[0]) - 1]:
                # print("已到达终点, curr_idx = %s, 退出循环" % self.start_node.idx)
                break

            # 将当前 node 的 idx 放入 visited, 表明已经访问过该节点
            visited.append(n)

            # 根据主函数中定义的 direction_map, 找到唯一的 "下一个节点"
            next_n, next_direction = __find_next_n(n, direction_map, visited)
            if (len(next_n) == 0) and (next_direction is None):
                # 当一个节点没有任何可以继续向前的节点, 则说明没有路可以走了, 直接返回False, 结束该算法.
                print("%s节点的前面是个死路%s" % (n, next_n))
                return False

            curr_value = grid[n[0]][n[1]]
            next_value = grid[next_n[0]][next_n[1]]

            # 若同时符合这些要求, 则可以作为下一个节点进行进一步的搜索.
            if (0 <= next_n[0] < len(grid)) \
                    and (0 <= next_n[1] < len(grid[0])) \
                    and (n != next_n) \
                    and (next_value in node_map[curr_value][next_direction]):
                n = next_n
                continue
            else:
                return False
        print("一共经历了%d个节点" % c)
        if res is True:
            break

    return res


def hasValidPath_v3(grid):
    """基于vw进一步优化时间
    这个版本, 会将 root = [0, 0] 调整成 i = j = 0, 尽量将所有可以避免的数组, 全部改成整形数字, 降低时间.
    """
    res = True
    return res


if __name__ == '__main__':
    # https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid/
    # todo 目前 [[3, 4, 3, 4, ...]] 这个测试用例会超时.
    with open("./test_data/q3.json", "r", encoding="utf-8") as f:
        tests = json.load(f)

    # [True, True, False, False, True, True, True, True, True, False, True, True, True]
    print([hasValidPath_v2(i) for i in tests])
