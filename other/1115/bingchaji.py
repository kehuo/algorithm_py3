# @File: bingchaji
# @Author: Kevin Huo
# @LastUpdate: 11/15/2020 5:32 PM


"""
# # 并查集
# 1. find -> 给定一个数字n，查找它在哪个集合里
# 2. union -> 给定两个数字，x,y 把他们所在的的集合合并起来


# 集合1: 1,2,3,4
# 集合5: 5,6,7,8

# find(2)  --> 1
# find(7)  --> 5

# union(3,8) --> 新集合：1,2,3,4,5,6,7,8 叫做集合1， 集合5没了
# find(2)  --> 1
# find(7)  --> 1


1. 假如我共有n个元素，我初始化一个parent数组，长度n：parent[i]=x的含义表示元素i 的父亲是x
初始化的时候，每个元素都是自己的父亲
初始化为：
[0,1,2,3,4]

2. 如果一个元素是自己的父亲，那么它就是整个集合的的代表比如 parent[k]==k表示元素k在集合k里，并且是这个集合的代表（root）

假如在某个时候，parent数组为
[0,0,1,2,4]

0的父亲是0  parent[0] 0是根
1的父亲是0  parent[1] ，祖宗是0
2的父亲是1 祖宗是0
3的父亲是2 祖宗是0
4的父亲是4 4是根


class UnionFind(object):
    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        self.parent[x] = x

    def find(self, x):
        # 好
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #路径压缩
        return self.parent[x]

        # 不好
        # cur=x
        # while self.parent[cur]!=cur:
        #     cur=self.parent[cur]
        # return cur

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        self.parent[x_root] = y_root

1,3,5,7,9

uf=UnionFind()
for i in [1,3,5,7,9]:
    uf.make_set(i)












class UnionFind(object):
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        if self.rank[x_root] == self.rank[y_root]:  # 按秩合并
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root



"""