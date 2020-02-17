class ProductOfNumbers:
    """
    第二题 - https://leetcode-cn.com/problems/product-of-the-last-k-numbers/submissions/
    用时 533ms / 内存160MB
    """

    def __init__(self):
        """
        变量解释
        nums: 普通的nums 数组, 调用add方法时, 会将传入的num 放入这个数组
        no_zero_nums: 和Nums数组功能类似, 但是多一个检查步骤：
            如果add(0), 那么不直接放入, 而是放入一个 1 作为代替.

        prev_product: 该数组用来记录 当前传进来所有数字的乘积。
            比如当前一共传进来3个数, nums = [4, 3, 0], 那么 prev_product = [4, 12, 0], 其中
            prev_product[0] 就是传入1个数字时候，所有数的乘积, 就是 4
            prev_product[1] 就是传入2个数字时候，所有数的乘积, 就是 4x3 = 12
            prev_product[3] 就是传入3个数字时候，所有数的乘积，就是 4x3x0 = 0

        no_zero_prev_product: 功能和 prev_product 类似, 不过这里的乘积，用no_zero_nums 计算。保证没有0
            比如 当前nums = [4, 3, 0], 那么 no_zero_nums = [4, 3, 1], 那么
            no_zero_prev_product = [4, 12, 12], 分别是
            4
            4x3
            4x3x1

        most_recent_zero_index: 该变量用来记录, 最近一次add进来的 0 在整个 nums数组中的索引
        比如 nums = [4, 3, 0], 那么 这个变量值就是 2, 因为 nums[2] = 0
        又比如: nums = [4, 3, 0, 2, 3, 0], 那么这个变量值就是 5, 因为虽然nums有2个0，他们的索引分别是2和5, 但是最近的是5
        """
        self.nums = list()
        self.no_zero_nums = list()

        self.prev_product = list()
        self.no_zero_prev_product = list()

        self.most_recent_zero_index = None
        return

    def add(self, num: int) -> None:
        """
        该函数做3件事
        1 把num直接放入 nums
        2 判断num是否为0, 并放入 no_zero_nums, 判断规则如下:
            2.1 num==0 > 将1放入 no_zero_nums
            2.2 num!=0 > 将num 放入 no_zero_nums
        PS:注意，如果 num==0, 还需要顺便更新变量 most_recent_zero_index

        3 把self.nums[-1]和 prev_product[-1]相乘，将结果tmp直接放入 prev_product
        4 把self.no_zeros_nums[-1] 和 no_zero_prev_product[-1] 相乘，将结果 no_zero_tmp 放入 no_zero_prev_product
        """
        # 1
        self.nums.append(num)
        # 2
        if num == 0:
            self.no_zero_nums.append(1)
            self.most_recent_zero_index = len(self.nums) - 1
        else:
            self.no_zero_nums.append(num)

        # 3
        if len(self.prev_product) == 0:
            self.prev_product.append(num)
        else:
            tmp = num * self.prev_product[-1]
            self.prev_product.append(tmp)

        # 4
        if len(self.no_zero_prev_product) == 0:
            self.no_zero_prev_product.append(self.no_zero_nums[-1])
        else:
            no_zero_tmp = self.no_zero_nums[-1] * self.no_zero_prev_product[-1]
            self.no_zero_prev_product.append(no_zero_tmp)
        return

    def getProduct(self, k: int) -> int:
        """
        比如 self.nums = [3, 0, 2, 5, 4]
        k = 2, 也就是计算最后2个值得乘积 5x4

        当前 self.most_recent_zero_index = 1 (因为从后往前数, 离的最近的一个0的索引是1 >> nums[1] = 0)
        同时, 最后的k个值得最小的一个索引 = need_to_cal_least_index = len(nums) - k = 5 - 2 = 3, 也就是 nums[3] = 5

        因为 need_to_cal_least_index(3) > self.most_recent_zero_index(1)
        索引最后的k个数字里面没有0. 可以正常计算.

        加入最后k个数字有0, 那么直接返回 0, 函数结束
        """
        # 1 先检查最近出现的 0, 是否包含在最后这k个数字里
        need_to_cal_least_index = len(self.nums) - k

        # 2.1 整个数组中不存在0
        if self.most_recent_zero_index is None:
            if k >= len(self.nums):
                res = self.prev_product[-1]
            else:
                res = self.prev_product[len(self.nums) - 1] // self.prev_product[len(self.nums) - 1 - k]

        # 2.2 整个数组中存在0
        else:
            # 2.2-a 而且 最后的k个数字中也存在 0
            if need_to_cal_least_index <= self.most_recent_zero_index:
                res = 0

            # 2.2-b 但是 最后的k个数字中不存在 0
            # 使用 self.no_zero_prev_product进行计算
            else:
                if k >= len(self.nums):
                    res = self.no_zero_prev_product[-1]
                else:
                    res = self.no_zero_prev_product[len(self.nums) - 1] // self.no_zero_prev_product[len(self.nums) - 1 - k]
        return res


if __name__ == '__main__':
    nums = [[3], [0], [2], [5], [4], [2]]
    funcs = ["add", "add", "add", "add", "add", "getProduct"]
    res_list = []
    pon = ProductOfNumbers()
    for i in range(len(nums)):
        res_list.append(pon.__getattribute__(funcs[i])(nums[i][0]))

    print(res_list)
