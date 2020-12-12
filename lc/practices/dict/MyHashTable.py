# @File: MyHashTable
# @Author: Kevin Huo
# @LastUpdate: 12/10/2020 10:30 PM


class MyHashTable(object):
    """
    自己实现哈希表
    """
    def __init__(self, elements=None):
        """
        1. 哈希表的存储容量有不同的取值方式, 常见的方式是和需要存储的数据的长度相同
        注意: python中定义桶的数量的原则是:
            1.1 默认8
            1.2 当key的数量动态增长而且超过了当前桶容量时, 用一下规则增加桶容量:
                如果当前桶容量 < 50000, 那么每次对当前容量乘以4, 即 self.bucket_size = self.bucket_size * 4
                如果当前桶容量 >= 50000, 那么每次乘以2, 即self.bucket_size = self.bucket_size * 2


        2. 计算索引的方式也采用 散列值对容量取余 (还有一种做法, 是对小于等于容量的最近的一个质数取余, 但是2种办法都可以)
        3. 散列函数我不具体实现, 直接使用Python内置的 hash(), 但是我们需要知道，对一个哈希函数, 它有3个特点要满足:
            3.1 - 哈希值 (散列值) 的计算速度需要很快
            3.2 - 计算出的哈希值需要不可逆, 也就是说不能用哈希值倒推出原始键值.
            3.3 - 输入不同长度的键, 要保证输出的哈希值长度固定.
        """
        # 一共多少个桶 (python源代码中默认尺寸是8, 并且递增的方式是 8, 16, 32, 这种以2的幂增长)
        self.bucket_size = len(elements) if elements else 8
        # 这里初始化每个桶. 有很多种选择, 比如用简单的python内置列表, 或者用链表, 或者甚至用红黑树(仅当数据很大时使用)
        # 我们用python内置数组实现
        self.buckets = [[] for _ in range(self.bucket_size)]
        if elements:
            self._assign_buckets(elements)

    def __getitem__(self, key):
        """这个函数支持使用 d["key"] 的方式访问元素"""
        return self._get_value(key)

    def __setitem__(self, key, value):
        """该函数支持使用 d["key"] = new_v 的方式更新值"""
        self._write_val(key, value)

    def __str__(self):
        """在print(d) 时候被调用"""
        return str(self.buckets)

    def _assign_buckets(self, elements):
        """
        该函数仅当初始化 MyHashTable 时传入elements 时候被调用
        elements 有2种可能的传入方式:
        第一种 -- 数组 + 子数组形式 = [[key1, val1], [key2, val2], ...]
        第二种 -- 传入一个python内置字典 {"key1": "val1", "key2": "val2"}
        """
        check_list = elements.items() if isinstance(elements, dict) else elements

        for k, v in check_list:
            hashed_val = hash(k)
            bucket_idx = hashed_val % self.bucket_size
            self.buckets[bucket_idx].append([k, v])

    def _get_value(self, input_key):
        """哈希表的查询"""
        hashed_k = hash(input_key)
        idx = hashed_k % self.bucket_size
        for k, v in self.buckets[idx]:
            if k == input_key:
                return v

    def _write_val(self, input_key, new_val):
        """哈希表的写入
        如果self.buckets[idx] 中已有该key, 则是属于更新操作.
        如果self.buckets[idx] 为空, 则属于新建key-val操作
        """
        hashed_k = hash(input_key)
        idx = hashed_k % self.bucket_size
        # 空桶, 属于新建操作
        if not self.buckets[idx]:
            self.buckets[idx].append((input_key, new_val))
            return
        # 如果桶不为空, 那么属于更新操作
        for i in range(len(self.buckets[idx])):
            currk, currv = self.buckets[idx][i]
            if currk == input_key:
                # 更新v
                self.buckets[idx][i][1] = new_val
                return
        # 如果程序能执行到这里, 说明桶既不为空, 而且没有找到对应k, 那说明哈希冲突了, 我们实现的冲突解决方案是 "链表法", 也就是在当前桶中将所有
        # 具有相同哈希值的key-val对都存在里面.
        self.buckets[idx].append([input_key, new_val])


if __name__ == '__main__':
    raw = {"name": "huoke", "city": "lanzhou"}
    d = MyHashTable(raw)
    print(d["name"])
    # 新增
    d["age"] = 18
    print(d)
    # 更新
    d["city"] = "shanghai"
    print(d)
