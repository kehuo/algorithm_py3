# @File: fiv
# @Author: Kevin Huo
# @LastUpdate: 3/17/2020 3:25 PM


from itertools import product, combinations

total = [(10, 2), (5, 1), (1, 1), (7, 1), (4, 7), (2, 3)]

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


def recursive_loop(total_d, curr_i, max_i, test_d):
    """一共 max_i 层循环, 当前是第 curr_i 层"""
    if curr_i == max_i:
        test_d = 1


def cal_single_C_n_k(array, k):
    """
    假设 n = 6
    一共分配 k 个指针, 其中 1 <= k <= len(array).
    pointer_count = k

    最外层的循环 for i in range(0, k):
        # 0 <= i < k
        第 i 个指针去遍历 array[i] ~ array[n - pointer_count + i] 个数据, 比如:
        k = 1: (1个指针, pointer_count = 1)
            i = 0, 遍历 array[0] ~ array[6 - 1 + 0]  = array[0] ~ array[5] --> tmp = [array[0], array[1], array[2], array[3], array[4], array[5]]
            LOOP END


        k = 2: (2个指针, pointer_count = 2)
            i = 0, 遍历 array[0] - array[6 - 2 + 0] = array[0] ~ array[4]
            i = 1, 遍历 array[1] - array[6 - 2 + 1] = array[1] ~ array[5]
            LOOP END

        k = 3: (3个指针, pointer_count = 3)
            i = 0, 遍历 array[0] - array[6 - 3 + 0] = array[0] ~ array[3]
            i = 1, 遍历 array[1] - array[6 - 3 + 1] = array[1] ~ array[4]
            i = 2, 遍历 array[2] - array[6 - 3 + 2] = array[2] ~ array[5]
            LOOP END

        k = 4: (4个指针, pointer_count = 4)
            i = 0, 遍历 array[0] - array[6 - 4 + 0] = array[0] ~ array[2]
            i = 1, 遍历 array[1] - array[6 - 4 + 1] = array[1] ~ array[3]
            i = 2, 遍历 array[2] - array[6 - 4 + 2] = array[2] ~ array[4]
            i = 3, 遍历 array[3] - array[6 - 4 + 3] = array[3] ~ array[5]
            LOOP END

        k = 5: (5个指针, pointer_count = 5)
            i = 0, 遍历 array[0] - array[6 - 5 + 0] = array[0] ~ array[1]
            i = 1, 遍历 array[1] - array[6 - 5 + 1] = array[1] ~ array[2]
            i = 2, 遍历 array[2] - array[6 - 5 + 2] = array[2] ~ array[3]
            i = 3, 遍历 array[3] - array[6 - 5 + 2] = array[3] ~ array[4]
            i = 4, 遍历 array[3] - array[6 - 5 + 2] = array[4] ~ array[5]
            LOOP END

        k = 6: (6个指针, pointer_count = 6)
            if n == k: 不需要指针, 直接 将 array 中所有结果 copy 到 res 中即可.
            LOOP END
    """
    n = len(array)

    # 指针数量 = k
    pointer_count = k
    res = {}
    t = {}
    # for i in range(0, k):
    #     start = i
    #     end = n - pointer_count + i + 1
    #     t[i + 1] = array[start:end]

    i = 0
    while True:
        if i == k:
            break
        tmp_data = []
        start = i
        end = n - pointer_count + i + 1
        t[i] = array[start:end]
    print(t)
    return res


def func(array, k):
    n = len(array)
    pointer_count = k
    res = {}
    for i in range(0, k):
        start = i
        end = n - pointer_count + i + 1
    res = combinations(array, k)
    res_array = [m for m in res]
    print(res_array)
    return res


if __name__ == '__main__':
    tests = [(10, 2), (5, 1), (1, 1), (7, 1), (4, 7), (2, 3)]
    for key in range(1, 7):
        r = func(total, k=key)
        print("")

