# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 11/29/2020 10:20 AM


from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        todo 暂时没做出来，这个解法也有待商榷.
        1 先排序
        2 - 值判断2头的值的差
        3 - 如果：
            3.1 left 和 right都是奇数 >> 将小的x2 再比较
            3.2 left 和 right都是偶数 >> 将大的除以2 再比较
            3.3 left 和 right 一奇一偶：
                A - 如果奇数>偶数 >> 直接返回 奇数-偶数
                B - 如果奇数<偶数:
                    B-1 先将 奇数x2 临时存为 tmp_ji_x_2
                    B-2 再将 偶数除以2, 临时存为 tmp_ou_chuyi_2
                    最后比较差值，选择 min(abs(r - tmp_ji_x_2), abs(l - tmp_ou_chuyi_2))
                    注意，我觉得这里就是有问题, 因为这个选择可能会影响后面的选择


        以下是zl给的解法建议

        """
        n = len(nums)
        nums.sort()
        l, r = nums[0], nums[n - 1]
        res = r - l
        while True:
            #  一奇一偶 而且 奇数>偶数, 那么结束循环
            if l % 2 == 1 and r % 2 == 0:
                if l > r:
                    # print("1奇1偶 且 奇>偶, l=%s, r=%s, nums=%s" % (l, r, nums))
                    break
            if l % 2 == 0 and r % 2 == 1:
                if r > l:
                    # print("1奇1偶 且 奇>偶, l=%s, r=%s, nums=%s" % (l, r, nums))
                    break

            # 都是奇数
            if l % 2 == 1 and r % 2 == 1:
                # print("2奇, l=%s, r=%s, nums=%s" % (l, r, nums))
                if l <= r:
                    # l*=2
                    nums[0] *= 2

                elif l > r:
                    # r*=2
                    nums[n - 1] *= 2
                res = min(res, abs(r - l))
                # 把乘2后的 值 排序到正确的位置
                nums.sort()
                l = nums[0]
                r = nums[n - 1]
                # print("END 2奇, l=%s, r=%s, nums=%s\n" % (l, r, nums))

            # 都是偶数
            if l % 2 == 0 and r % 2 == 0:
                if l <= r:
                    # r//=2
                    nums[n - 1] //= 2
                elif l > r:
                    # l//=2
                    nums[0] //= 2
                res = min(res, abs(r - l))
                # 把除以2后的 值 排序到正确的位置
                nums.sort()
                l = nums[0]
                r = nums[n - 1]

            #  一奇一偶 而且 奇数<偶数
            if l % 2 == 1 and r % 2 == 0 and l < r:
                # print("1奇1偶 且 l奇<r偶, l=%s, r=%s, nums=%s" % (l, r, nums))
                tmp_ji_x_2 = l * 2
                tmp_ou_chuyi_2 = r // 2
                diff_ji = abs(tmp_ji_x_2 - r)
                diff_ou = abs(l - tmp_ou_chuyi_2)
                # 选小的
                if diff_ji <= diff_ou:
                    l *= 2
                    nums[0] *= 2
                    res = min(res, diff_ji)
                elif diff_ji > diff_ou:
                    r //= 2
                    nums[n - 1] //= 2
                    res = min(res, diff_ou)
                nums.sort()
                l = nums[0]
                r = nums[n - 1]
                # print("end, l=%s, r=%s, nums=%s\n" % (l, r, nums))

            if l % 2 == 0 and r % 2 == 1 and r < l:
                # print("1奇1偶 且 r奇<l偶, l=%s, r=%s, nums=%s" % (l, r, nums))
                tmp_ji_x_2 = l * 2
                tmp_ou_chuyi_2 = r // 2
                diff_ji = abs(tmp_ji_x_2 - r)
                diff_ou = abs(l - tmp_ou_chuyi_2)
                # 选小的
                if diff_ji <= diff_ou:
                    # l//=2
                    nums[0] //= 2
                    res = min(res, diff_ji)
                elif diff_ji > diff_ou:
                    # r*=2
                    nums[n - 1] *= 2
                    res = min(res, diff_ou)
                nums.sort()
                l = nums[0]
                r = nums[n - 1]

        return res


if __name__ == '__main__':
    tests = [
        [1, 2, 3, 4]
    ]
    t = tests[0]
    s = Solution()
    s.minimumDeviation(t)
