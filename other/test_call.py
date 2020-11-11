# @File: test_call.py
# @Author: Kevin Huo
# @LastUpdate: 10/29/2020 1:26 PM


"""
测试 python 中的 __call__ 方法
"""


class A(object):
    def __init__(self, name="kevin", age=12):
        self.name = name
        self.age = age
        self.__instance = None

    def __call__(self, *args, **kwargs):
        print("__call__ is called")
        if self.__instance is None:
            self.__instance = 1
        return self.__instance


from collections import defaultdict
def main():
    d = defaultdict(list)
    d[1].append(2)
    d[2].append(3)

    keys = list(d.keys())
    keys.sort()


if __name__ == '__main__':
    main()

