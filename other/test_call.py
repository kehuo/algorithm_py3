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


if __name__ == '__main__':
    a = A()
    b = A()
    a()
    print(a==b)
