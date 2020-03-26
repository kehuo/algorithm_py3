# @File: m4
# @Author: Kevin Huo
# @LastUpdate: 3/26/2020 8:59 PM


import random


class RandomizedSet:
    """https://leetcode-cn.com/problems/insert-delete-getrandom-o1/
    可以用python 内置的 set 实现"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            self.d.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        注意, 每个元素被选择的概率应该相同
        """
        res = random.choice(list(self.d))
        return res


if __name__ == '__main__':
    r = RandomizedSet()
    r.insert(1)
    r.insert(3)
    r.insert(4)
    r.getRandom()
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
