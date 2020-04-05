class LFUCache:
    """
    每日一题 - 4月5日
    最不经常使用的缓存 (LFU)


    题目链接
    =======
    https://leetcode-cn.com/problems/lfu-cache


    题目描述
    =======
    计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

    get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。

    put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。
    在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

    进阶：
    你是否可以在 O(1) 时间复杂度内执行两项操作？


    个人理解
    =======
    1 该题难点, 在于用某种数据结构, 对于每一个key, 维护一个动态的 "使用时间" 和 "使用次数" 2个维度的数据, 满足:
    每次 get 一个 key1 后, 会动态更新这个数据结构, 更新2个数据:
        <1> 将这个 key1 的 "使用时间" 更新为 "所有key中最近的"
        <2> 这个key1 的 "使用次数" + 1

    2 可能适用的数据结构 - 最小堆. 原因:
        2.1 该题的 put 方法中, 要将 "最近最少使用的键将被去除", 也就是一个最小堆中的 min_heap[0], 可以达到 O(1) 的要求.
        2.2 但是局限在于: 每次更新最小堆时, build_heap 的操作, 根据算法导论, 理论上要 O(lgn), 不满足 O(1) 的要求.

    3. 最小堆的实现:
        3.1 用 heapq 模块实现.
        3.2 heapq 的索引代表 某个key "最近一次" 或者 "最久远的一次" 被使用的时间.
        3.3 heapq 的值, 代表 某个key 一共被使用的次数. (get 一次, 则该值 += 1)
    """
    def __init__(self, capacity: int):
        self.c = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        return key

    def put(self, key: int, value: int)-> None:
        pass
