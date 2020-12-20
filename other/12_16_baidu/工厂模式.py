# @File: 工厂模式
# @Author: Kevin Huo
# @LastUpdate: 12/16/2020 12:38 AM


class Person(object):
    """抽象类 只提供接口"""
    def __init__(self, h=180, w=100):
        self.height = h
        self.weight = w

    def eat(self):
        pass


class Man(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print("init method for man")

    def eat(self):
        print("man eat quickly")


class Woman(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print("woman init method")

    def eat(self):
        print("woman eat slowly")


class PersonFactory(object):
    def get_person(self, name, gender):
        if gender == "M":
            return Man(name)
        if gender == "F":
            return Woman(name)
        print("Gender should be M or F")


def main():
    f = PersonFactory()
    new_man = f.get_person("kevin", "M")
    new_woman = f.get_person("kathy", "F")


