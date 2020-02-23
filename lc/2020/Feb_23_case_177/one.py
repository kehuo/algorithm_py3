from datetime import datetime


def daysBetweenDates_v1(date1, date2):
    """
    这道题是个误会, 其实就用 datetime 包来解答即可, 较简单.
    但是我以为要手写实现, 所以下面的v2是我手写的方法... 其实不用的, 但是既然已经写出来了, 就记录下做个参考..
    """
    d1 = datetime.strptime(date1, "%Y-%m-%d").date()
    d2 = datetime.strptime(date2, "%Y-%m-%d").date()
    return abs((d1 - d2).days)


def daysBetweenDates_v2(date1, date2):
    def is_leap_year(a_year):
        """
        功能函数 - 判断是否是闰年
        """
        return (a_year % 4) == 0 and (a_year % 100) != 0 or (a_year % 400) == 0

    def get_earlier_and_later_date(d1arr, d2arr):
        """功能函数 - 比较2个date, 判断哪个早哪个晚"""
        all = [d1arr, d2arr]
        # 先确定谁晚
        if d1arr[0] > d2arr[0]:
            later = d1arr
        elif d1arr[0] < d2arr[0]:
            later = d2arr
        else:
            # 看月份
            if d1arr[1] > d2arr[1]:
                later = d1arr
            elif d1arr[1] < d2arr[1]:
                later = d2arr
            else:
                # 看日期
                if d1arr[2] > d2arr[2]:
                    later = d1arr
                elif d1arr[2] < d2arr[2]:
                    later = d2arr
                else:
                    # 完全是同一天, 则规定d2是晚一点的
                    later = d2arr
        all.remove(later)
        earlier = all[0]
        return earlier, later

    # 先把 str 转成 list
    d1_arr = [int(i) for i in date1.split("-")]
    d2_arr = [int(i) for i in date2.split("-")]

    # 判断谁早谁晚
    earlier, later = get_earlier_and_later_date(d1_arr, d2_arr)
    print(earlier, later)

    # 先计算年
    res = 0
    # 1 先把中间完整的年的天数算出来. 比如2017-2020, 那么先把中间完整的 2018, 2019 这2个完整年的天数(365, 265)加进去.
    if later[0] - earlier[0] > 1:
        for y in range(earlier[0] + 1, later[0]):
            print("complete year: %s" % y)
            res += 366 if is_leap_year(y) else 365

    print("加完完整年后res=%s" % res)

    # 2 计算月份
    month_map = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    # 月份计算分成2种情况: <1> 同一年 <2> 不同的年
    # todo 情况太杂 以后再说
    # 2.1 如果 earlier[0] == later[0] >> 计算的结果分3部分:
    #   <A> earlier[1] + 1 到 later[1] 之间所有完整月份的天数之和. 比如 earlier = 2008-09-03, later=2008-11-13
    #       那么 先计算 9月和11月之间，所有完整月份的天数之和. 即res += 10月的天数(31)
    # 2部分 = earlier这一年中, 所有完整月份的天数 + later这一年中, 所有完整月份的天数

    # 2.1 先算开头year
    # 2.1-a 先将 earlier year 的中间完整的月份 算进去. 比如 2019-06-30, 那么先算 2017 年的完整月份 7, 8, 9, 10, 11, 12
    if earlier[1] < 12:
        for m in range(earlier[1] + 1, 13):
            if m == 2:
                res += month_map[m] if is_leap_year(earlier[0]) else month_map[m] + 1
            else:
                res += month_map[m]

    # 2.1-b 再将 later year 的中间完整的月份 算进去.
    if later[1] < 12:
        for m in range(later[1] + 1, 13):
            if m == 2:
                res += month_map[m] if is_leap_year(later[0]) else month_map[m] + 1
            else:
                res += month_map[m]

    print("加完月份后 res=%s" % res)
    return res

    # 3 最后, 计算 earlier 和 later 当前月份的天数. 比如 date=2019-11-07, 那么把11月的这7天算进去.


def main():
    d1 = "1999-06-29"
    d2 = "2001-06-30"
    print(daysBetweenDates_v1(d1, d2))


if __name__ == '__main__':
    main()
