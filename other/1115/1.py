# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 11/15/2020 3:19 PM


"""
https://repl.it/@LucienZhang/huoke#graph.py

# from heapq import heappop, heappush
# from typing import List
# # SSSP


# from heapq import heappop, heappush

# def dijkstra(matrix, source) -> dict:
#     # optimized by heap
#     h = [(0, source)]
#     visited = {}  # 返回一个字典，key=节点,value到源的记录
#     while h and len(visited) < len(matrix):
#         weight, cur = heappop(h)
#         if cur in visited:
#             continue
#         visited[cur] = weight
#         for i, w in enumerate(matrix[cur]):
#             if w > 0 and i not in visited:
#                 heappush(h, (weight + w, i))
#     return visited

# # 路由表的维护
# 每个节点到（指定）源头到最短距离

# # 当前路由到任意其它路由器的最短距离

# # R0



# 旁边的路由器R1会传给我它的路由表

# 我更新我R0的路由表=
#     它的路由表+我R0到R1的距离（当这个结果比我当前路由表小，我更新）
#     否则不管


# R1收到的字典为： 到R0距离为0
# R1初始字典到R0距离为无穷大
# 更新后我的字典为
# R0:10
# R1:0
# 把它传给R2
# R2更新后为


# 目标服务器的ip: 888.77.78.9

# 路由表是：
# 到123.456.0.0走接口1找R1
# 到789.123.0.0走接口2找R2

# 0.0.0.0走接口5找R5（默认路由）

# ip:39.98.132.45
# 39.0.0.0 -> R1


# 我RW

# 39.98.0.0 -> R10  慢
# 39.98.0.0 -> R11  快

# R11：
# 39.98.0.0 -> R100   weight 100
# 39.98.132.0  -> R101  weight 200


# RW 到 R11消耗1

# 到39.98.0.0 -> R11  + 权重  101
# 到39.98.132.0 -> R11  + 权重  201
# 到我自己 权重0

# 把一个图（有向/无向）生成树的时候，有三种边：
# 1. 树向边（生成的树的一部分）
# 2. 回边
# 3. 交叉边


# visited=set()

# stack=[root]
# while stack:
#     node=stack.pop()
            # 可操作
#     for n in node.children:
#         if n not in visited:
#             stack.append(n)



# visited=set()
# 最小生成树
# h=[(0,root)]
# while stack:
#     #node=stack.pop()
#     w,node=heappop(h)
        # 可操作
        # if node in visited:
        #     continue
        # 连接。
        # visisted.add(node)
#     for n in node.children:
#         if n not in visited:
#             heappush(h,(weight,n))




# visited=set()
# 单源最短路径
# h=[(0,root)]
# while stack:
#     #node=stack.pop()
#     w,node=heappop(h)
#     for n in node.children:
#         if n not in visited:
#             heappush(h,(weight+w,n))
"""