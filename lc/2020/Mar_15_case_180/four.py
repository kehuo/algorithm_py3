# @File: four
# @Author: Kevin Huo
# @LastUpdate: 3/15/2020 10:29 AM


from itertools import combinations


def func(m, n):
    """
    C 下面=m, 上面=n
    """
    res, fenmu = None, None

    loop_end = n
    for i in range(0, loop_end):
        if i == 0:
            res = m
            fenmu = n
        else:
            res *= m
            fenmu *= n
        m -= 1
        n -= 1
    return res // fenmu


def brute_force(n, speed, efficiency, k):
    """暴力法 -- 已在leetcode证明, 没有计算的错误, 但是会超出时间限制"""
    total = []
    for idx in range(n):
        total.append((speed[idx], efficiency[idx]))

    max_p = None
    for i in range(1, k + 1):
        curr_array = combinations(total, i)
        for one in curr_array:
            A = sum([j[0] for j in one])
            B = min([j[1] for j in one])
            curr_max_p = A * B

            if max_p is None:
                max_p = curr_max_p
            else:
                if max_p < curr_max_p:
                    max_p = curr_max_p
    return max_p


def maxPerformance(n, speed, efficiency, k):
    """
    https://leetcode-cn.com/problems/maximum-performance-of-a-team/

    思路:
    1. 将 speed 和 efficiency 2个表合并到一起 total, 方便后续操作.
    2. 从 total 中计算出: 只有1个工程师时, 效率值最高的那个男子
    3. 记录以下几个变量:
        我们定义 p = A x B, 其中
        p = 题目中定义的团队表现值 performance
        A = 已经被选择的工程师的 speed 之和, 即p的第一个乘法因子
        B = 已经被选择的工程师的 效率最低的值, 即p的第二个乘法因子
        curr_max_p = 当前已经选择的工程师的团队表现值

        total = [(speed[0], efficiency[0]), (speed[1], efficiency[1]), ... (speed[n-1], efficiency[n-1])]
        res = 一个列表, 将已经选中的工程师, 从total中pop出来, 并放入res

    4. 流程:
        4.1 遍历一个 while True 循环, 当 len(res) == k 时停止循环
        4.2 在每次循环时, 遍历total中的每一项:
            4.2-a tmp_A = A + 当前工程师的speed
            4.2-b tmp_B = min(B, 当前工程师的efficiency)
            4.2-c tmp_p = tmp_A * tmp_B
            4.2-d 判断 tmp_p 是否大于 curr_max_p:
                若大于, 则做以下事:
                    <1> 将当前工程师从 total 中pop出来, 放入res
                    <2> 将 tmp_A 的值累加到 A 上面, 即 A += tmp_A
                    <3> 将 tmp_B 赋值给 B, 即 B = tmp_B
                    <4> 将 tmp_p 的值赋给 curr_max_p, 即 curr_max_p = tmp_p
                    <5> continue, 下一轮while循环
                若小于等于:
                    直接continue 下一轮循环
    """
    A = 0
    B = 0
    curr_max_p = 0
    max_individual_p = None

    res = []
    total = []
    for i in range(n):
        total.append((speed[i], efficiency[i]))
        if i == 0:
            max_individual_p = {"p": speed[i] * efficiency[i],
                                "i": i,
                                "speed": speed[i],
                                "efficiency": efficiency[i]}
        else:
            tmp = speed[i] * efficiency[i]
            if max_individual_p["p"] < tmp:
                max_individual_p["p"] = tmp
                max_individual_p["i"] = i
                max_individual_p["speed"] = speed[i]
                max_individual_p["efficiency"] = efficiency[i]
    # todo 这里需要修改, 最后一个测试用例证明 -- 第一个选p最大的工程师并没有卵用, 需要逐个比较.
    first_engineer = total.pop(max_individual_p["i"])
    res.append(first_engineer)

    A = max_individual_p["speed"]
    B = max_individual_p["efficiency"]
    curr_max_p = max_individual_p["p"]
    still_has_better_engineer = True
    while len(res) < k:
        if still_has_better_engineer is False:
            break
        print("\n循环开始, total=%s" % total)
        print("res=%s, p=%s, A=%s, B=%s" % (res, curr_max_p, A, B))
        while len(total) > 0:
            larger_curr_loop = []
            for idx in range(len(total)):
                one = total[idx]
                tmp_A = A + one[0]
                tmp_B = min(B, one[1])
                tmp_p = tmp_A * tmp_B

                if tmp_p > curr_max_p:
                    print("先放入 larger_curr_loop, tmpA=%s, tmpB=%s, tmp_p=%s" % (tmp_A, tmp_B, tmp_p))
                    larger_curr_loop.append(
                        {"tmp_A": tmp_A,
                         "tmp_B": tmp_B,
                         "tmp_p": tmp_p,
                         "one": one}
                    )

            # 如果larger_curr_loop不为空, 则选出 larger_curr_loop 中最大的一项, 放入 res, 并从 total中移除
            if len(larger_curr_loop) > 0:
                best_engineer = max(larger_curr_loop, key=lambda x: x["tmp_p"])

                print(best_engineer)
                res.append(best_engineer["one"])
                total.remove(best_engineer["one"])

                A = best_engineer["tmp_A"]
                B = best_engineer["tmp_B"]
                curr_max_p = best_engineer["tmp_p"]
            else:
                still_has_better_engineer = False
            break
    print("最后\n res=%s, p=%s, A=%s, B=%s" % (res, curr_max_p, A, B))
    return curr_max_p


def maxPerformance_v2(n, speed, efficiency, k):
    """
    由于上面的版本被证明没用, 我暂时留着作为参考, 并且将新的方法实现在这个v2函数中.

    这个V2函数使用的办法基本就是遍历每一种可能, 求出每一种可能得 团队表现值. 但是:
    我会将已经求出的值, 有效的存储在一个 字典中, 防止重复计算.

    答案 = C(6, 1) + C(6, 2) + C(6, 3) + ... + C(6, k)
    然后求这些所有情况中的最大的p

    这个算法的可行性在于:
    假设 total = [(10, 2), (5, 1), (1, 1), (7, 1), (4, 7), (2, 3)]

    1. 当我们求 C(6, 1)的所有6种情况时, 可以将6个p值都记录在 d["1"] 中. 示例:
        d = {"C_6_1": {"1": {"raw": [(10, 2)], "A": 10, "B": 2, "p": 20},
                       "2": {"raw": [(5, 1)], "A": 5, "B": 1, "p": 5},
                       "3": {"raw": [(1, 1)], "A": 1, "B": 1, "p": 1},
                       "4": {"raw": [(7, 1)], "A": 7, "B": 1, "p": 7},
                       "5": {"raw": [(4, 7)], "A": 4, "B": 7, "p": 28},
                       "6": {"raw": [(2, 3)], "A": 2, "B": 3, "p": 6}
                }
            }
    2. 当我们求 C(6, 2) 一共15种情况时, 我们也会将所有答案全部记录在 d["2"] 中, 但是, 再计算d["2"], 我们会复用 d["1"]的结果.

    3. 一直求 C(6, 3) -- C(6, 6) 后, 最终的d 结构如下:
    d = {
        # C(6, 1) = 6 种情况
        "C_6_1": {"1": {"raw": [(10, 2)], "A": 10, "B": 2, "p": 20},
                  "2": {"raw": [(5, 1)], "A": 5, "B": 1, "p": 5},
                  "3": {"raw": [(1, 1)], "A": 1, "B": 1, "p": 1},
                  "4": {"raw": [(7, 1)], "A": 7, "B": 1, "p": 7},
                  "5": {"raw": [(4, 7)], "A": 4, "B": 7, "p": 28},
                  "6": {"raw": [(2, 3)], "A": 2, "B": 3, "p": 6}
                  },

        # C(6, 2) = 15 种情况
        "C_6_2": {"1": {"2": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "3": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "4": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "5": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "6": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15}
                        },
                  "2": {"3": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "4": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "5": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "6": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15}
                        },
                  "3": {"4": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "5": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "6": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15}
                        },
                  "4": {"5": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        "6": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15}
                        },
                  "5": {"6": {"raw": [(10, 2), (5, 1)], "A": 15, "B": 1, "p": 15},
                        }
                  },

        # C(6, 3) = (6x5x4) // (3x2x1) = 20 种情况
        "C_6_3": {"1": {"2": {"3": {"raw": [(10, 2), (5, 1), (1, 1)], "A": 16, "B": 1, "p": 16},
                              "4": {"raw": [(10, 2), (5, 1), (7, 1)], "A": 22, "B": 1, "p": 22},
                              "5": {"raw": [(10, 2), (5, 1), (4, 7)], "A": 19, "B": 1, "p": 19},
                              "6": {"raw": [(10, 2), (5, 1), (2, 3)], "A": 17, "B": 1, "p": 17}
                              },
                        "3": {"4": {"raw": [(10, 2), (1, 1), (7, 1)], "A": 16, "B": 1, "p": 16},
                              "5": {"raw": [(10, 2), (1, 1), (4, 7)], "A": 16, "B": 1, "p": 16},
                              "6": {"raw": [(10, 2), (1, 1), (2, 3)], "A": 13, "B": 1, "p": 13}
                              },
                        "4": {"5": {"raw": [(10, 2), (7, 1), (4, 7)], "A": 21, "B": 1, "p": 21},
                              "6": {"raw": [(10, 2), (7, 1), (2, 3)], "A": 19, "B": 1, "p": 19}
                              },
                        # max here!!!
                        "5": {"6": {"raw": [(10, 2), (4, 7), (2, 3)], "A": 16, "B": 2, "p": 32},
                              }
                        },
                  "2": {"3": {"4": {},
                              "5": {},
                              "6": {}
                              },
                        "4": {"5": {},
                              "6": {}
                              },
                        "5": {"6": {},
                              }
                        },
                  "3": {"4": {"5": {},
                              "6": {}
                              },
                        "5": {"6": {},
                              }
                        },
                  "4": {"5": {"5": {},
                              "6": {}
                              },
                        }
                  },
        # C(6, 4) 共 (6x6x4x3) // (4x3x2x1) = 15 情况
        "C_6_4": {"1": {"2": {"3": {"4": {},
                                    "5": {},
                                    "6": {}
                                    },
                              "4": {"5": {},
                                    "6": {}
                                    },
                              "5": {"6": {}
                                    }
                              },
                        "3": {"4": {"5": {},
                                    "6": {}
                                    },
                              "5": {"6": {}
                                    }
                              },
                        "4": {"5": {"6": {}
                                    }
                              }
                        },
                  "2": {"3": {"4": {"5": {},
                                    "6": {}
                                    },
                              "5": {"6": {}
                                    }
                              },
                        "4": {"5": {"6": {}
                                    }
                              }
                        },
                  "3": {"4": {"5": {"6": {}
                                    }
                              }
                        }
                  },

        # C(6, 5) = C(6, 1) = 共6种情况
        "C_6_5": {"1": {"2": {"3": {"4": {"5": {},
                                          "6": {}
                                          },
                                    "5": {"6": {}
                                          }
                                    },
                              "4": {"5": {"6": {}
                                          }
                                    }
                              },
                        "3": {"4": {"5": {"6": {}
                                          }
                                    }
                              }
                        },
                  "2": {"3": {"4": {"5": {"6": {}
                                          }
                                    }
                              }
                        },
                  },

        # C(6, 6) = 唯一的 1 种情况, 全选.
        "C_6_6": {"1": {"2": {"3": {"4": {"5": {"6": {}
                                                }
                                          }
                                    }
                              }
                        }
                  }
    }



    *注意, 我的算法会在循环的过程中, 动态地维护一个变量 max_p, 这个值一直保持为当前已经计算的所有结果中, 最大的 performance值*
    最后返回的就是 max_p
    """
    all_chosen_engineers = []
    max_p = 0

    total = []
    for i in range(n):
        total.append((speed[i], efficiency[i]))

    d = {}
    # 一共有 k 个 sub_d, 代表 C(n, 1) - C(n, k)
    for i in range(0, k):
        idx = i + 1
        sub_d = {}
        # key的数量 = n - (i + 1)

        # sub_d 一共有 idx 层深度(1 ~ n), 每层中有  个 key-value 对
        key_count = n - (i + 1)
        for j in range(0, key_count):
            pass
        # 将 sub_d 写入 d
        d["C_%s_%s" % (str(n), str(i + 1))] = sub_d
        pass

    print(total)
    return max_p


class Node(object):
    """从这里开始是自己的实现"""
    def __init__(self, idx_in_speed, is_root, layer, A, B, parent_node, child_node_list):
        self.idx_in_speed = idx_in_speed
        self.is_root = is_root
        self.layer = layer
        self.child_node_list = child_node_list

        self.A = A
        self.B = B
        self.p = None
        self.parent_node = parent_node


class CustomTree(object):
    def __init__(self, root, max_layer):
        """
        max_layer = k

        speed 长度 = n
        共 k 层.
        root节点在 speed 中的索引 = root.idx_in_speed
        一共可以构建 n-k+1 棵树. 比如n=6, k=2, 则可以构建6-2+1=5棵树.
        """
        self.root = root
        self.max_layer = max_layer
        self.max_p = root.p

    def _add_child_node(self, n, speed, efficiency, node):
        """
        功能函数 - 给一个节点添加相关的子节点
        k 已经在 __init__ 中通过 max_layer 传入

        一个节点的子节点:
            数量: 通过5个值, 可以唯一的确定: n, k, root_idx_in_speed, curr_node.idx_in_speed, curr_layer
            开始的索引: 自己的索引+1
            结束的索引: 第x层的节点的子节点的索引, 最大可以到 n-k+x. 比如:
                当k=3, n=6 时, 第1层(root层)的子节点, 最大可以到 n-k+x=6-3+1 = 4
                当k=3, n=6 时, 第2层的子节点, 最大可以到 n-k+x = 6-3+2 = 5

        当一个节点的 layer == k 时, 当前节点为叶子结点
        """
        if node.is_root:
            pass
            # print("第%s层,索引为%s的root node.A=%s, node.p=%s, max_p=%s" % (node.layer, node.idx_in_speed, node.A, node.p, self.max_p))
        if node.layer == self.max_layer:
            # 最后一层
            return
        start = node.idx_in_speed + 1
        end = n - self.max_layer + node.layer + 1
        # print(start, end)
        for idx in range(start, end):
            sub_node = Node(idx_in_speed=idx,
                            is_root=False,
                            layer=node.layer + 1,
                            A=node.A + speed[idx],
                            B=min(node.B, efficiency[idx]),
                            parent_node=node,
                            child_node_list=[]
                            )
            sub_node.p = sub_node.A * sub_node.B
            if self.max_p is None:
                self.max_p = sub_node.p
            else:
                if self.max_p < sub_node.p:
                    self.max_p = sub_node.p
            # print("第%s层,索引为%s的node.A=%s, B=%s, parent_node.A=%s, parent_node.B=%s, parent_node.p=%s, node.p=%s, max_p=%s" % (sub_node.layer, idx, sub_node.A, sub_node.B, sub_node.parent_node.A, sub_node.parent_node.B, sub_node.parent_node.p, sub_node.p, self.max_p))

            node.child_node_list.append(sub_node)

        for j in node.child_node_list:
            self._add_child_node(n, speed, efficiency, node=j)

    def run(self, n, speed, efficiency):
        self._add_child_node(n, speed, efficiency, self.root)


if __name__ == '__main__':
    tests = [
        {"n": 6, "speed": [2, 10, 3, 1, 5, 8], "efficiency": [5, 4, 3, 9, 7, 2], "k": 2},
        {"n": 6, "speed": [2, 10, 3, 1, 5, 8], "efficiency": [5, 4, 3, 9, 7, 2], "k": 3},
        {"n": 3, "speed": [2, 8, 2], "efficiency": [2, 7, 1], "k": 2},
        {"n": 6, "speed": [10, 5, 1, 7, 4, 2], "efficiency": [2, 1, 1, 1, 7, 3], "k": 6}
    ]

    all_res = []
    s_idx, e_idx = 0, 4
    for z in range(s_idx, e_idx):
        test = tests[z]
        n = test["n"]
        k = test["k"]
        speed = test["speed"]
        efficiency = test["efficiency"]

        # 对于 n, k, 一共有 n-k+1棵树, 所以一共有n-+k个root节点.
        # n=6, k=2, 则一共6-2+1=5棵树, root节点为 0/1/2/3/4

        # 如果k的最大值为6, 则:
        # k=1 >> 6-1+1=6棵树
        # k=2 >> 6-2+1=5棵树
        # k=3 >> 6-3+1=4棵树
        # k=3 >> 6-3+1=4棵树
        # k=4 >> 6-4+1=3棵树
        # k=5 >> 6-5+1=2棵树
        # k=6 >> 6-6+1=1棵树
        max_k = k
        max_p_list = []

        for every_k in range(max_k):
            tree_count = n - every_k
            # print("C(%s %s), 共%s棵树" % (n, every_k+1, tree_count))
            for tree_idx in range(tree_count):
                # C(n, every_k)
                # max_layer = every_k + 1
                # root 索引 = tree_idx
                test_root_node = Node(idx_in_speed=tree_idx,
                                      is_root=True,
                                      layer=1,
                                      A=test["speed"][tree_idx],
                                      B=test["efficiency"][tree_idx],
                                      parent_node=None,
                                      child_node_list=[])
                test_root_node.p = test_root_node.A * test_root_node.B
                test_tree = CustomTree(root=test_root_node, max_layer=every_k + 1)
                test_tree.run(test["n"],
                              test["speed"],
                              test["efficiency"]
                              )
                # print(test_tree.max_p)
                max_p_list.append(test_tree.max_p)
        print(max(max_p_list))
    # 正确答案: 60, 68, 56, 32
