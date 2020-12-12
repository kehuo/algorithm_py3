# @File: 5.py
# @Author: Kevin Huo
# @Date: 2020/10/31

class A(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = A(1)
aleft = A(2)
aright = A(3)
a.left = aleft
a.right=aright


b = A(1)
bleft = A(2)
bright = A(3)
b.left = bleft
b.right=bright
print(a)
print(b)
print(a==b)
