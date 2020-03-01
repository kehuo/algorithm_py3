class MaxHeap(object):
    """
    这个类的实现, 完全基于<算法导论 第六章 - 第三版>
    The implementation of this class is based on <Introduction to Algorithms - Third Edition>
    """
    def __init__(self, raw_array):
        """for a heap, index should between 1 - len(array), not 0 - [len(array) - 1]"""
        self.array = raw_array
        self.heap_size = len(self.array)

    def parent(self, i):
        return int(((i + 1) / 2) - 1)

    def left(self, i):
        return int((2 * (i + 1)) - 1)

    def right(self, i):
        return int((2 * (i + 1) + 1) - 1)

    def max_heapify(self, i):
        """
        A = self.array
        1 <= i <= A.heap_size

        Max_Heapify(A, i)

        1. left = LEFT(i)
        2. right = RIGHT(i)
        3. if (left <= A.heap_size) and (A[left] > A[i])
        4.     largest = left
        5. else: largest = i
        6. if (right <= A.heap_size) and (A[right] > A[largest])
        7.     largest = right
        8. if largest != i
        9.     exchange A[i] with A[largest]
        10.    Max_Heapify(A, largest)
        """
        left = self.left(i)
        right = self.right(i)
        if (left < self.heap_size) and (self.array[left] > self.array[i]):
            largest = left
        else:
            largest = i

        if (right < self.heap_size) and (self.array[right] > self.array[largest]):
            largest = right

        if largest != i:
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        Build_Max_Heap(A)

        for i = [A.length / 2] down to 1
            Max_Heapify(A, i)
        """
        start = int((len(self.array) / 2) - 1)
        end = 0
        for i in range(start, end - 1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        """
        1. Build_Max_Heap(A)
        2. for i = A.length down to 2
        3.     exchange A[1] with A[i]
        4.     A.heap_size = A.heap_size - 1
        5.     Max_Heapify(A, 1)

        example:
        before: [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        after:  [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        """
        start = len(self.array) - 1
        end = 1
        for i in range(start, end - 1, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size = self.heap_size - 1
            self.max_heapify(0)
        # 注释, 下面这行代码在算法导论中是没有的, 我加这一行, 是保证一个堆可以被多次 build_max_heap > heap_sort
        # 所以每次排序之后, 我再把 heap_size 恢复到原来是长度, 保证下一次 sort时, heap_size又可以从原始长度逐次减一
        self.heap_size = len(self.array)

    def heap_increase_key(self, i, key):
        """
        Heap_Increase_Key(A, i, key):

        A = self.array

        1. if key < A[i]:
        2.     error "new key is smaller that current key A[i]"
        3. A[i] = key
        4. while (i > 1) and (A[parent[i]] < A[i]):
        5.     exchange A[i] with A[parent(i)]
        6.     i = parent(i)
        """
        if key < self.array[i]:
            print("New key %s is smaller that current key A[i] %s where current i=%s" % (key, self.array[i], i))
            return
        self.array[i] = key
        while (i > 0) and (self.array[self.parent(i)] < self.array[i]):
            self.array[i], self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)

    def heap_extract_max(self):
        """
        注意, 这个方法实现2个任务:
        <1> 获取当前 堆 中的最大值, 并且返回
        <2> 将返回的这个最大值, 从堆中删掉.

        ***在以下算法中, 获取最大值其实很简单, 只需要step3, 即max=A[1], 其余步骤4-6都在完成第二个任务 --> 将max从堆中删掉***
        Heap_Extract_Max algorithm:

        1. if A.heap_size < 1:
        2.    error "heap underflow"
        3. max = A[1]
        4. A[1] = A[A.heap_size]
        5. A.heap_size = A.heap_size - 1
        6. Max_Heapify(A, 1)
        7. return max
        """
        # step 1- 2
        if self.heap_size < 1:
            print("error: heap underflow.")
            return
        # step 3
        max_element = self.array[0]
        # step 4
        self.array[0] = self.array[self.heap_size - 1]
        # step 5
        self.array = self.array[:-1]
        self.heap_size = self.heap_size - 1
        # step 6
        self.max_heapify(0)

        return max_element


class MaxPriorityQueue(object):
    def __init__(self, raw_max_heap):
        if len(raw_max_heap.array) == 0:
            self.q = raw_max_heap
        else:
            raw_max_heap.build_max_heap()
            self.q = raw_max_heap

    def maximum(self):
        """
        O(1)
        A = self.q

        Heap_Maximum(A) = A[0]
        """
        return self.q.array[0] if len(self.q.array) > 0 else None

    def increase_key(self, i, key):
        """
        O(lgn)

        Call MaxHeap.heap_increase_key
        """
        self.q.heap_increase_key(i, key)

    def insert(self, key):
        """
        O(lgn)
        A = self.q

        1. A.heap_size = A.heap_size + 1
        2. A[A.heap_size] = Negative infinity
        3. Heap_Increase_Key(A, A.heap_size, key)
        """
        self.q.array.append(-float("inf"))
        self.q.heap_size = self.q.heap_size + 1
        self.q.heap_increase_key(self.q.heap_size - 1, key)

    def extract_max(self):
        """
        O(lgn)

        A = self.q

        call MaxHeap.heap_extract_max to achieve 2 things:
        <1> get the max value as the return of this func.
        <2> delete the max value from the current queue.
        """
        return self.q.heap_extract_max()


if __name__ == '__main__':
    # test = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    test = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    max_heap = MaxHeap(raw_array=test)
    print(max_heap.array)
    max_heap.build_max_heap()
    print(max_heap.array)
    max_heap.heap_sort()
    print(max_heap.array)
    max_heap.build_max_heap()
    print(max_heap.array)

    test = []
    mpq = MaxPriorityQueue(raw_max_heap=MaxHeap(test))
    # print(mpq.q.array)

