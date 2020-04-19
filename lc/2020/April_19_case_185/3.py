# @File: 3.py
# @Author: Kevin Huo
# @Date: 2020/4/19


def minNumberOfFrogs(croakOfFrogs: str) -> int:
    """
    变量解释:
    ======
    state数组维护一个字典, 代表 "对每个下一个即将到来的字母, 目前有哪些青蛙可以叫出这个字母"
    比如 state["a"] = [2, 42], 代表了 "当遇到一个字母 a, 我有2个青蛙可以叫他, 分别是2号和42号青蛙", 2和42是d字典的key值

    d字典维护了每个已经创建出来的青蛙的喊叫状态. 比如 d[131] = ["c", "r", "o"], 代表:
    131号青蛙目前已经喊了 cro 3个字母, 当下一个字母a来临时, 这个131号青蛙可以叫它.

    q 数组维护一个队列, 里面是 "当前空闲的青蛙", 当一个新的 "c" 字母来临时, 先看state有没有青蛙可以叫它, 如果没有, 再看
    q 里面有没有空闲青蛙, 如果也没有, 才会创建一个新青蛙, 并将这个新青蛙放到 state["c"] 中.

    示例数据:
    =========
    d = {1: [c, r], 2:[c], 3: [c, r, o], ..., 42: [c, r], ... ,131: [c, r ,o ,a]}
    state = {c: [], r: [2], o: [1, 42], a: [3], k: [131]}
    q(空闲青蛙队列) = [55, 62, 71]
    """
    next_map = {"c": "r", "r": "o", "o": "a", "a": "k", "k": "c"}
    d = {1: []}
    q = []
    state = {"c": [1], "r": [], "o": [], "a": [], "k": []}
    # c = {"c": 0, "r": 0, "o": 0, "a": 0, "k": 0}
    for i in range(len(croakOfFrogs)):
        s = croakOfFrogs[i]
        # c[s] += 1
        # 先挑青蛙 (是创建新的 / 还是d中已经有青蛙需要这个s / 还是非法字符直接返回-1)
        if len(state[s]) == 0:
            if s == "c":
                # 如果当前所有d中青蛙都在忙, 而且q里没有空闲青蛙, 那么分2个情况
                if len(q) == 0:
                    # 重新建一个新青蛙, 放到 state 中
                    new_frog_idx = max(d) + 1
                    state["c"].append(new_frog_idx)
                # 如果q有空闲青蛙, 那么拿一只出来用
                else:
                    available_frog = q.pop()
                    state["c"].append(available_frog)
            # 遇到 "o" 而且没有任何青蛙可以接, 那么直接返回 -1
            else:
                return -1

        # step 1 更新d: curr_frog = 1
        curr_frog = state[s].pop()

        # d[1] = ["c"]
        if curr_frog not in d:
            d[curr_frog] = []

        # 比如第131个青蛙叫了一个字母o,  叫之前d[131] = ["c", "r"]
        d[curr_frog].append(s)
        # 叫之后 d[131] = ["c", "r", "o"]

        # step 2 利用 next_map 更新 state, 以131号青蛙为例. 因为它已经叫了o, 所以131号青蛙下一个接受的字母是 "a"
        # 所以 state["a"] 里面就可以把 131 号青蛙放进去
        # state["a"] = [131], 代表下次循环时, 遇到下一个"a"字母时, 有一个青蛙(131号)可以叫它.
        # 如果是next_c = "k", 那么有一只青蛙又闲了
        next_c = next_map[s]
        if s == "k":
            # 遇到k时, 说明有一个青蛙可以空闲出来了 (他已经叫完了一次 croak, 现在是待命状态, 可以放到q里, 并将d[131]置为一个空数组,
            # 等待下一个 croak 的来临)
            q.append(curr_frog)
            d[curr_frog] = []
        state[next_c].append(curr_frog)

    for frog in d:
        # 只要有没有叫完整 croak 的青蛙, 比如d[131] = "cro", 或者 d[22] = "cr", 就说明字符串不符合规定, 返回-1
        # 因为比如每次第131号青蛙完成一次完整 croak, 我都会把青蛙的 d[131] 清空, d[131] = []
        # 所以如果所有字符串遍历完毕后, 还有青蛙没有完成一个完整的 croak, 就说明字符串不合理.
        if len(d[frog]) > 0:
            return -1
    return len(d)


if __name__ == '__main__':
    # 标准答案 229
    tests = [
        "ccccccccccrrccccccrcccccccccccrcccccccccrcccccccccccrcccccrcccrrcccccccccccccrocrrcccccccccrccrocccccrccccrrcccccccrrrcrrcrccrcoccroccrccccccccorocrocccrrrrcrccrcrcrcrccrcroccccrccccroorcacrkcccrrroacccrrrraocccrrcrrccorooccrocacckcrcrrrrrrkrrccrcoacrcorcrooccacorcrccccoocroacroraoaarcoorrcrcccccocrrcoccarrorccccrcraoocrrrcoaoroccooccororrrccrcrocrrcorooocorarccoccocrrrocaccrooaaarrcrarooaarrarrororrcrcckracaccorarorocacrrarorrraoacrcokcarcoccoorcrrkaocorcrcrcrooorrcrroorkkaaarkraroraraarooccrkcrcraocooaoocraoorrrccoaraocoorrcokrararrkaakaooroorcororcaorckrrooooakcarokokcoarcccroaakkrrororacrkraooacrkaraoacaraorrorrakaokrokraccaockrookrokoororoooorroaoaokccraoraraokakrookkroakkaookkooraaocakrkokoraoarrakakkakaroaaocakkarkoocokokkrcorkkoorrkraoorkokkarkakokkkracocoaaaaakaraaooraokarrakkorokkoakokakakkcracarcaoaaoaoorcaakkraooaoakkrrroaoaoaarkkarkarkrooaookkroaaarkooakarakkooaokkoorkroaaaokoarkorraoraorcokokaakkaakrkaaokaaaroarkokokkokkkoakaaookkcakkrakooaooroaaaaooaooorkakrkkakkkkaokkooaakorkaroaorkkokaakaaaaaocrrkakrooaaroroakrakrkrakaoaaakokkaaoakrkkoakocaookkakooorkakoaaaaakkokakkorakaaaaoaarkokorkakokakckckookkraooaakokrrakkrkookkaaoakaaaokkaokkaaoakarkakaakkakorkaakkakkkakaaoaakkkaoaokkkakkkoaroookakaokaakkkkkkakoaooakcokkkrrokkkkaoakckakokkocaokaakakaaakakaakakkkkrakoaokkaakkkkkokkkkkkkkrkakkokkroaakkakaoakkoakkkkkkakakakkkaakkkkakkkrkoak"
    ]

    t = tests[0]

    r = minNumberOfFrogs(t)
    print(r)
