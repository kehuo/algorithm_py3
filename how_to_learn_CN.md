# 并查算法
> * union find 对应于**不相交集合数据结构** 《算法导论第21章》
> * 有两种实现方法，快速查找 quick find （链表） 和 快速求并 quick union （树）
> * UnionFind.py中实现了这种数据结构
> * LinkedList 定义了链表类
> * UnionFind 定义了该数据结构的抽象类
> * QuickFind 以快速查找的方式，利用自定义的链表实现了这种结构
> * QuickFind2 以快速查找的方式，用Python自带的list实现了这种结构
> 
> ## 阅读顺序
> 1. 阅读算法导论21.1-21.2，理解这种数据结构的基本操作
> 2. 理解QuickFind2 如何实现了这种结构
> 3. 运行文件查看demo
> 4. 理解UnionFind如何定义了抽象类
> 5. 理解LinkedList如何自定义了链表，及该链表如何实现了迭代器
> 6. 理解QuickFind如何用自定义链表实现了该结构
> 7. 阅读算法导论21.3-21.4，理解基于森林的结构实现，理解路径压缩和按秩合并
> 8. 理解data_structure.py下的Tree结构，注意递归和非递归的求深度算法
> 9. 理解QuickUnion类，注意路径压缩算法的非递归实现方法
> 10. 理解QuickUnion2类，注意如何用数组模拟了树的结构，如何实现了路径压缩，及get_sets()为什么要使用字典来记录不同集合的索引（考虑字典查询的时间复杂度）
> 11. Competition目录下的quick_union.py是为比赛写的最精简方便的类，注意如何使用它
> 
> ## 了解深拷贝和浅拷贝，思考以下问题
> UnionFind.py中，205-220行，如果改为以下代码会如何，比较demo中check_size()的结果
```python3
        if rx.get_depth() >= ry.get_depth():
            rx.children.append(ry)
            ry.parent = rx
            for t in self.forest:
                if t is ry:
                    t = None
                    break
            self.size -= 1
        else:
            ry.children.append(rx)
            rx.parent = ry
            for t in self.forest:
                if t is rx:
                    t = None
                    break
            self.size -= 1
```

# 堆结构，贪心算法，最小生成树问题，Prim算法，堆优化，RSTP协议
《算法导论》第6章，16章，23章   
> 1. 复习树和二叉树概念，理解data_structure.py中Tree类和BinaryTree类
> 2. 阅读第6章，了解堆的概念，理解Heap类，注意它与BinaryTree的继承关系，注意它的初始化用了自顶向下的构造方法
> 3. 理解MinHeap类，注意如何在改变prior函数后完成一个minimum heap类
> 4. 理解DeepHeap类，注意在堆化过程中，交换值和交换指针的区别
> 5. 理解DeepMinHeap类，注意双重继承
> 6. 运行文件，查看demo，理解如何用堆实现堆排序
> 7. 理解Heap2类，注意如何用数组模拟树的结构，注意叶子与非叶子节点的索引范围，及如何找到某一节点的父母或子女
> 8. 阅读第16章，了解贪心算法的原理
> 9. 阅读第23章，了解最小生成树问题，及Prim算法背后的贪心原理
> 10. 查看Prim.py中的Prim2函数，理解如何实现Prim算法，注意查找和删除最小值是如何实现的，分析这里的时间复杂度
> 11. 理解堆优化，查看Prim函数，注意如何用最小堆来实现查找和删除最小值，分析这里的时间复杂度，思考经过堆优化的Prim算法，整体的时间复杂度
> 12. Prim算法相关：计算机网络二层，RSTP协议，rapid spanning tree protocol

# 单源最短路径问题，Dijkstra算法
> 注意和Prim算法的比较   
> 算法相关：计算机网络三层路由协议：OSPF协议

# 最小生成树问题，Kruskal算法
> 利用并查集，依次从小到大加入边，使得结果无环，直到所有节点都在树中
