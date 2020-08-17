# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 8/16/2020 1:07 PM


class Solution:
    """
    https://leetcode-cn.com/contest/weekly-contest-202/problems/minimum-number-of-days-to-eat-n-oranges/
    有空用动态规划实现 - 可以实现但是提交可能会超时
    """

    def minDaysDP(self, n: int) -> int:
        """
        答案已提交，确实超时了。。。但是答案是对的
        动态规划的解法 - 应该会超时，但是实现DP纯粹是为了练习动态规划.

        todo - 如果想用 DP 通过提交，必须要加入 LRU cache 算法优化才行，这个以后可以考虑加入.

        动态规划有多种解法:
        第一种 -- dp[i]代表以下:
        某种状态下，它有两种选择:
            A，快速减1降到除二的状态
            B，快速减1降到除三的状态
        然后选两者中小的

        第二种 -- dp[n]代表 "一共 n 个橘子，全部吃完最少要几口"
        0个橘子 = 一共吃0口
        1个橘子 = 一共吃1口
        2个橘子 = 一共吃2口
        当 n >= 3 时, 每个状态中有 A和 B 这2个选择:
            A - A.1 先以 "每次吃 1 个橘子"的方式，吃 x 口, 将 n 吃成一个可以被 2 整除的数; x = n%2;
                A.2 再以 "这一口吃 n//2 个橘子", 这次吃 y 口, 其中 y 永远等于 1;
                A.3 再加上 "吃完 A.1 和 A.2 以后，剩下的最少吃 z 口". 其中 z = dp[(n - n%2) - n//2];
                所以 方案 A = x + y + z = n%2 + 1 + dp[(n - n%2) - n//2]

            B - B.1 先以 "每次吃 1 个橘子"的方式，吃 x 口, 将n吃成一个可以被 3 整除的数; x = n%3;
                B.2 再以 "这一口吃 2*(n//3) 个橘子", 这次吃 y 口, 其中 y 永远等于 1;
                B.3 再加上 "吃完A.1 和 A.2 以后，剩下的最少吃 z 口". 其中 z = dp[(n - n%3) - 2*(n//3)]
                所以 方案 B = x + y + z = n%3 + 1 + dp[(n - n%3) - 2*(n//3)]
            然后 dp[n] = min(方案A, 方案B)

        最终返回 dp[n]

        注意:
        关于方程A和B, 假设n=11时:
        那dp[11] 就是以下3部分组成的：

        方案A中:
        x - 把11吃成10，需要1步
        y - "吃10//2 =5", 需要1步
        z - 然后剩下5个，所以需要 dp[5]步，这里的5就等于 (11-11%2)-11//2

        方案B中:
        x - 把11吃成9，需要2步
        y - “吃 2*(9//3)", 需要1步
        z - 然后剩下 3 个，所以还需要 dp[3] 步，这里 3就等于 (11 - 11%3) - (2 * 11//3) = 9 - 6 = 3
        """
        dp = list()
        dp.append(0)
        dp.append(1)
        dp.append(2)
        # n > 2 时需要用到状态转移方程
        for i in range(3, n+1):
            # A = i%2 + 1 + dp[(i - i%2) - i//2]
            # B = i%3 + 1 + dp[(i - i%3) - 2*(i//3)]
            A = i % 2 + 1 + dp[i//2]
            B = i % 3 + 1 + dp[i // 3]
            dp.append(min(A, B))

        return dp[n]

    def minDaysPerfect(self, n: int) -> int:
        """
        最好的解法
        """
        pass


if __name__ == '__main__':
    tests = [10, 6, 1, 56, 2, 16, 99999999, 182]
    # 答案 = [4, 3, 1, 6, 2, 5, 30, 8]
    t = tests[6]
    s = Solution()
    r = s.minDaysDP(t)

    print(r)
