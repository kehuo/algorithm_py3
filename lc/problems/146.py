# @File: 142
# @Author: Kevin Huo
# @LastUpdate: 5/25/2020 1:52 PM


class LRUCache(object):
    """
    https://leetcode-cn.com/problems/lru-cache/
    Implemented by python built-in data structure list.
    pass lc all test.
    Time used: 4526ms.
    Memory used: 22MB.

    #todo -- Will use LinkedList data structure to optimize this algorithm.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []
        self.curr_len = 0

    def get(self, key: int) -> int:
        res = -1
        for i in range(self.curr_len - 1, -1, -1):
            one = self.data[i]
            # one = [key: value]
            if key == one[0]:
                # remove i from curr place, and append it the tail of the list
                res = one[1]
                self.data.pop(i)
                self.data.append(one)
                break
        return res

    def put(self, key: int, value: int) -> None:
        for i in range(self.curr_len):
            one = self.data[i]
            # update
            if key == one[0]:
                self.data.pop(i)
                self.data.append([key, value])
                return
        # add
        if self.curr_len < self.capacity:
            self.data.append([key, value])
            self.curr_len += 1
            return
        # data[0] == LRU,
        # data[-1] = most recently used
        self.data.pop(0)
        self.data.append([key, value])


class LRUCacheVersion2LinkedList(object):
    """
    v2 - implemented by LinkedList data structure.
    """
    def __init__(self):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
