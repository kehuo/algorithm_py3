# @File: 3
# @Author: Kevin Huo
# @LastUpdate: 8/16/2020 1:07 PM

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        https://leetcode-cn.com/problems/magnetic-force-between-two-balls/

        二分法

        步骤:
        1 - 首先, 对 position 排序
        2 - 第一项 和 最后一项 肯定要选, 这样就已经消耗了 2 颗球了. 所以我们在核心算法中:
            2.1 如果 m<=2 那么直接返回 最后一项 - 第一项 的差，就是结果. 换句话说，把2个球放2边，它们之间的距离肯定最大呀.
            2.2 如果 m>2 那么在核心算法中，我们只需要处理剩下的 m-2 颗球.
        3 - 最大间隔 = (7 - 1) // (球数-1) = 6 // 2 = 3
        为什么要先求出这个 最大间隔呢? 而且为什么是用上面这个公式求呢? 你这样想:
            3.1 假设我们给定一个有序数组 arr = [1, 2, 3, 4, 5, 6, 7], 给定m=3, 首先，有两个球的位置已经固定了，分别是 arr[0] = 1 和 arr[5] = 6
            3.2 然后，我们只需要考虑最后一个球放在哪里。
            3.3 因为数组很短，所以我们可以在每个地方都放一次，试试哪种放置方法，可以让间隔最大。 注意，因为 开头和末尾的位置
                已经被占用了，所以我们只能考虑 [2, 3, 4, 5, 6] 这个子数组:
                A - 放在 2 处, 那么整个数组就被分成了 1~2 和 2~7, 那么间隔分别是 1 和 5 >> 这种放置方法的最小的最大间隔是 1.
                B - 放在 3 处，数组被分成 1~3 和 3~7, 间隔分别是 2 和 4 >> 最小的最大间隔是 2
                C - 放在 4 处, 数组被分成 1~4 和 4~7, 间隔分别是 3 和 3 >> 最小的最大间隔是 3
                D - 放在 5 处, 数组被分成 1~5 和 5~7, 间隔分别是 4 和 2 >> 最小的最大间隔是 2
                E - 放在 6 处, 数组被分成 1~6 和 6~7, 间隔分别是 5 和 1 >> 最小的最大间隔是 2
                综上，C 方案获胜。而且o我们可以发现当我们吧球放的离中心越近，最小的最大间隔就越大，这也说明一个问题：
                这道题，我们要将球摆放的约平均，也就是说每个球之间的间隔约相近，最终的结果就越好。这个很容易理解，因为我们最后
                求的，是一个"最小的"最大间隔，也就是说，不管你别的有多大，我只看你最小的那个。所以，我们要保证每一个间隔都不能
                太小，所以，平均的放置就是最好的办法。
        4 - 解释到这里，相信你应该明白我们为什么要先求出一个 “理论上最大的 最小间隔”，因为，我们摆球的时候，要用到2分法，而这个理论
        的最大值，就是我们每次正在摆一颗球的时候，在二分搜索范围我们要遍历每一项，并且判断是否将当前的球摆在这，那么如何判断呢？
        就要用到这个理论的最大值了。 换句话说，举个例子：
            4.1 已知一个排序数组 arr = [1, 2, 3, 4, 7], 而且已知 m = 3
            4.2 先把前两个球摆好，分别放在 arr[0]（开头） 和 arr[-1] （末尾）的位置.
            4.3 现在开始用二分法，摆最后一颗球。
            4.4 摆之前，如我们所说，先求出 “理论上的最大值”，也就是 (7 - 1)//(3-1) = 6//2 = 3
            4.5 也就是说，理论上，两颗球之前最大的 最小间隔，不可能超过 3.
            4.6 那么，我们来进行二分法，并且利用这个 "理论上最大的最小间隔,即3" 来作为一颗球是否应该放在某个位置的判断依据。
                以下是2分法的步骤：
                arr = [1, 2, 3, 4, 7]
                a - 初始化3个索引值:
                    left = 1
                    right = len(arr) - 2
                    mid = (left + right) // 2
                    (为什么左右是1和 len-1你？因为我之前说了，开头0 和 末尾 len-1 已经被2个球占了，所以2分法只在剩下的子数组中进行
                    而子数组的就是arr 去头去尾，所以初始化的Left不是0而是1，right不是len-1而是 len-2)
                b - 初始化完成后, 我们的中间索引是 2, 所以 arr[2] = 3
                c - 我们的第一次二分搜索范围，是从 arr[left] 到 arr[right], 即 [2, 3, 4] 这个数组.
                d - 我们将上面求出的 "最大间隔", 和左侧最近的球的索引相加，得到 3 + arr[0] = 3+1=4
                e - 我们用这个求出的值 4, 和 arr[mid] 比较, 结果是 4 > arr[mid](即arr[2]=3), 所以，我们只在二分范围的右半边搜索. (也就是只搜索右半边 [3, 4])
                f - 在这个范围内，从左到右遍历 [3, 4] 的每一项, 并且将当前项和 “理论上最大的最小间隔, 即 3+(距离最近的左边的一颗球的值)”进行比较:
                    注意，因为当前距离最近的左侧的球时 arr[0] = 1, 所以要比较的标准值=3+1 = 4, 也就是说，判断 [2, 3, 4]中的每一项是否 <4
                    d-1 当前项arr[2] = 3, 它 < 4, 所以说明: 暂时不用把球放在这里，还可以继续往后移.
                    d-3 当前项arr[3] = 4, 它 == 4, 所以说明: 这个球就是当前能选择的最优解了，必须把这颗球放在这里，为什么呢？因为"理论上最大的间隔就是3"，如果你放在
                        当前的位置，就已经达到最大值了，你就算再往右移动，造成的结果也只是让后面的球之间的间隔变得更小，没有用。
                        所以，把当前球放在这里。
                    （这次二分搜索到此结束）
            4.7 我们在上面的步骤中，通过1次二分法，成功的放置了一颗球，但是我们可能有很多球，所以我们在做完一次二分搜索后，要
                做一些后续步骤，来更新一些变量，并且做一些判断，来决定是否需要继续二分搜索，还是可以直接返回结果了呢？
                a - 我们每做一次2分法，必定要放一颗球，所以，每次二分法开始前，我们可以 m -= 1
                b - 在一次二分法结束后，我们判断 m是否为0:
                    >> 若为0，则说明没有球可以放了，直接范湖结果即可，结束算法。
                    >> 若不为0, 则说明还有球需要放，那我们更新以下参数，为下一次的二分法做准备:
                        1 - 我们要记录一个 "距离当前搜索范围最近的一个 左侧的球的值", 刚开始的时候，这个值初始化=arr[0]=1
                            第一次二分结束后，假设我们把球放在了 arr[3]=4的位置上，那我们把这个值更新成 4.
                            (PS: 为什么需要这个值呢？因为我们在二分搜索中遍历每一项的时候，比较的基准值= 理论最大间隔+上面这个值
                            比如第一次二分法，我们遍历时，比较的基准值= 最大间隔+这个值 = 3+arr[0] = 3 + 1 = 4
                            因为我们只有3个球，所以只用一次二分法就够了，假如哦们还要做一次二分法的话，下一次遍历时，作为判断
                            依据的基准值，应该就变成了 理论最大间隔+更新后的上面提到的值 = 3+arr[3] = 3+4 = 7.
                            以此类推.
                            )
                        2 - 二分搜索的 3 个索引都要更新:
                            left = 上一次二分法中 放球的位置索引 + 1
                            (举例，我们第一次，也是唯一的一次微分搜索中，放置球的索引是arr[3], 那么，这次二分结束后，我们将
                            left 的值更新为 3+1 = 4, 也就是说，下次二分搜索将从 arr[4] 开始)

                            right 不变

                            mid = (left + right) // 2



        """
        # 1 排序
        position = sorted(position)
        lenPos = len(position)

        # 2
        if m == 2:
            print(position[-1] - position[0])
            return position[-1] - position[0]

        # 3 核心代码, 处理剩下的 m-2 颗球
        # 求出理论上最大的 最小间隔
        max_min_distance = (position[-1] - position[0]) // (m - 1)

        # 求出理论上最小的最小间隔
        min_min_distance = min([position[i + 1] - position[i] for i in range(lenPos - 1)])
        if lenPos == m:
            return min_min_distance

        # 不用二分，就用最简单的从左到右的遍历实现
        balls = [position[0], position[-1]]
        latest_left_ball_value = position[0]
        count = m - 2
        start, end = 1, lenPos - 1
        while count > 0:
            count -= 1
            for i in range(start, end):
                curr = position[i]
                # 当且仅当 curr == max_min_distance + latest_left_ball_value 时候，直接将球放下
                if curr == max_min_distance + latest_left_ball_value:
                    latest_left_ball_value = position[i]
                    balls.append(latest_left_ball_value)
                    start = i + 1
                    break
                if curr < max_min_distance + latest_left_ball_value:
                    # 贪心，不放球，还可以继续右移
                    continue
                if curr > max_min_distance + latest_left_ball_value:
                    # 已经超了，这里判断 i 是否是start:
                    if i == start:
                        # 放球
                        latest_left_ball_value = position[i]
                        balls.append(latest_left_ball_value)
                        start += 1
                        break
                    # 如果不是，那么去前一个值, 因为前一个值肯定没超过理论的最大值
                    latest_left_ball_value = position[i - 1]
                    balls.append(latest_left_ball_value)
                    start = i + 1
                    break
        balls.sort()
        print(balls)
        lenBalls = len(balls)
        res = min([balls[i + 1] - balls[i] for i in range(lenBalls - 1)])
        print("res = %s" % res)
        return res

        # todo 一下二分的思路，以后实现
        # # 开始第一次二分法, 初始化一些值
        # left = 1
        # right = lenPos - 2
        # latest_left_ball_value = position[0]
        #
        # # 一共需要执行 m-2 次二分搜索
        # count = m - 2
        # while left <= right:
        #     count -= 1
        #     mid = (left + right) // 2
        #     check_standard = max_min_distance + latest_left_ball_value
        #
        #     # 遍历搜索范围内的每一项，并且和 基准值比较
        #     # 如果数组值 > 基准值: 结束遍历, 去当前项的前一项, 因为当前项已经超过理论最大值了.
        #     # 如果数组值 < 基准值: 继续往右移动, 因为当前项还没有到达理论最大值，还可以再贪一步.
        #     # 如果数组值 = 基准值: 结束遍历，将球放在当前位置，更新参数，准备进行下一次二分搜索.
        #     # 先用 arr[mid] 和 check_standard 比较，来确认搜索左半边 (left - mid) 还是 右半边 (mid - right)


if __name__ == '__main__':
    # 答案 = [3, 999999999, 2, 45, 5, 7]

    tests = [
        {"position": [1, 2, 3, 4, 7], "m": 3},
        {"position": [5, 4, 3, 2, 1, 1000000000], "m": 2},
        {"position": [1, 2, 3, 5, 7], "m": 3},
        {"position": [10, 12, 14, 17, 25, 27, 31, 33, 46, 55, 60, 70, 71, 88, 100], "m": 3},
        {"position": [79, 74, 57, 22], "m": 4},
        # 下面这个题打错了，我的答案是6，正确答案是7
        {"position": [82, 68, 79, 17, 70, 51, 5, 46, 27, 44, 39, 57, 94, 45, 88, 56], "m": 9}
    ]
    question_index = int(input("please type question index: "))
    t = tests[question_index - 1]
    s = Solution()
    r = s.maxDistance(**t)
