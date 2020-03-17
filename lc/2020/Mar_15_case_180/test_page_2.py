# @File: test_page_2
# @Author: Kevin Huo
# @LastUpdate: 3/17/2020 8:06 PM


from itertools import combinations

# total = [(10, 2), (5, 1), (1, 1), (7, 1), (4, 7), (2, 3)]

d = {
    # C(6, 1)
    # n = 6, k = 1, pc = 1
    # d["^1#"]["A"] = total[1 - 1][0]
    # d["^1#"]["B"] = total[1 - 1][1]
    # d["^1#"]["p"] = d["^1#"]["A"] * d["^1#"]["B"]
    "^1#": {"A": 10, "B": 2, "p": 20},
    "^2#": {"A": 5, "B": 1, "p": 5},
    "^3#": {"A": 5, "B": 1, "p": 5},
    "^4#": {"A": 5, "B": 1, "p": 5},
    "^5#": {"A": 5, "B": 1, "p": 5},
    "^6#": {"A": 5, "B": 1, "p": 5},

    # C(6, 2)
    # n = 6, k = 2, pc = 2
    # d["^1#^2#"]["A"] = d["^1#"]["A"] + total[2 - 1][0]
    # d["^1#^2#"]["B"] = min(d["^1#"]["B"], total[2 - 1][1])
    # d["^1#^2#"]["p"] = d["^1#^2#"]["A"] * d["^1#^2#"]["B"]
    "^1#^2#": {"A": 15, "B": 1, "p": 15},
    "^1#^3#": {"A": 11, "B": 1, "p": 11},
    "^1#^4#": {"A": 15, "B": 1, "p": 15},
    "^1#^5#": {"A": 15, "B": 1, "p": 15},
    "^1#^6#": {"A": 15, "B": 1, "p": 15},
}


def func(n, speed, efficiency, k):
    """暴力法 -- 已在leetcode证明, 没有计算的错误, 但是会超出时间限制"""
    total = []
    for idx in range(n):
        total.append((speed[idx], efficiency[idx]))

    max_p = None
    for i in range(1, k + 1):
        curr_array = combinations(total, i)
        for each in curr_array:
            A = sum([j[0] for j in each])
            B = min([j[1] for j in each])
            curr_max_p = A * B

            if max_p is None:
                max_p = curr_max_p
            else:
                if max_p < curr_max_p:
                    max_p = curr_max_p
    return max_p


if __name__ == '__main__':
    tests = [
        [
            6,
            [2, 10, 3, 1, 5, 8],
            [5, 4, 3, 9, 7, 2],
            2
        ],
        [
            3,
            [2, 8, 2],
            [2, 7, 1],
            2
        ],
        [
            447,
            [29810, 40211, 42893, 41516, 39690, 43822, 71333, 75889, 12065, 28857, 31951, 9481, 72248, 95574, 2820,
             1300, 98400, 64653, 20209, 65724, 10107, 87196, 23537, 18552, 40059, 92973, 78892, 16555, 18571, 94717,
             41428, 88107, 97804, 26927, 39181, 70451, 6365, 87528, 33108, 89402, 56384, 32797, 57593, 59417, 51867,
             22482, 63673, 84731, 74791, 8169, 46524, 18126, 16401, 33963, 52141, 52571, 80275, 30610, 981, 69298,
             65654, 57452, 83770, 29587, 41024, 90040, 29500, 54034, 73454, 95450, 36075, 28767, 9379, 84580, 20902,
             26719, 39154, 39265, 48709, 91919, 96524, 77933, 16154, 67365, 49441, 20419, 55936, 74648, 99320, 64885,
             51591, 83490, 50329, 21601, 95669, 68705, 33448, 13245, 96588, 18236, 86471, 91804, 58335, 50116, 52068,
             42660, 16559, 63959, 15623, 78733, 53507, 86575, 36396, 49657, 526, 69254, 75902, 4039, 79381, 34131,
             22657, 19453, 26274, 40782, 99277, 89592, 22018, 46787, 55046, 27387, 50235, 37231, 3166, 74621, 71472,
             88332, 85117, 9855, 48986, 40797, 65934, 46769, 42427, 16240, 94106, 45904, 70687, 44482, 89577, 64527,
             84892, 50121, 72993, 36389, 78403, 96806, 66973, 60501, 67753, 97601, 40022, 22324, 81270, 69594, 47111,
             462, 51009, 55820, 44042, 76603, 91686, 64580, 83933, 38128, 2724, 94541, 20459, 52078, 23351, 79360,
             45804, 92802, 89789, 39803, 60565, 63511, 61225, 5950, 66884, 97616, 55391, 46554, 86094, 2588, 66475,
             21185, 12197, 83359, 36150, 39899, 69219, 31095, 35268, 9816, 68577, 48262, 67046, 96565, 22093, 85599,
             93512, 35359, 79911, 30424, 73538, 22592, 34017, 43208, 29140, 79948, 32012, 4003, 52770, 56593, 35271,
             9508, 95988, 75910, 76210, 19423, 34339, 69022, 18170, 93815, 47329, 98485, 31522, 94131, 94173, 40042,
             13945, 52037, 64535, 24480, 7254, 3052, 89562, 64810, 69277, 80371, 44885, 35990, 80379, 22635, 29107,
             30569, 58959, 98385, 30372, 37178, 71699, 51065, 59205, 33801, 65056, 14542, 10336, 2021, 62967, 50220,
             37646, 52420, 99427, 19959, 1990, 19029, 71117, 74023, 33315, 10423, 85480, 1893, 70384, 68801, 5612,
             15393, 11933, 3621, 83561, 97599, 90017, 86903, 51080, 82715, 34059, 83311, 32169, 77061, 22974, 56161,
             91496, 83674, 7970, 71687, 70530, 93278, 55591, 9187, 35009, 80041, 98594, 32976, 12658, 7696, 56113, 6923,
             11957, 61495, 48530, 40985, 16598, 4350, 87066, 51799, 58470, 96551, 35389, 32770, 11245, 4482, 7624,
             34211, 96367, 34119, 15354, 39813, 55684, 65896, 26924, 44390, 51262, 63066, 17004, 58801, 73223, 76201,
             68168, 3968, 97410, 26212, 51019, 42497, 53675, 16564, 8502, 39387, 69951, 54735, 41786, 35740, 98139,
             65675, 68961, 19498, 95264, 42935, 9024, 36650, 59526, 97208, 10246, 7354, 6387, 64511, 33020, 92133,
             97865, 47393, 48515, 40290, 78416, 69748, 21994, 19446, 90079, 73765, 14780, 53885, 81226, 13006, 89302,
             93672, 26784, 8753, 74871, 84022, 9544, 84311, 67041, 2864, 48249, 93098, 28828, 78392, 30831, 59270,
             48125, 24750, 95135, 33628, 26394, 97883, 49902, 63843, 52920, 66856, 76625, 5259, 60091, 24873, 91226,
             84159, 70881, 39670, 97893, 71176, 74970, 37029, 53928, 67878, 79007, 76161, 59313, 17164, 58220, 18393,
             21361, 83449, 55598, 86711, 4752, 55165, 36904, 98437, 2403, 11801, 50256],
            [52409144, 5509941, 25073597, 77712955, 32997178, 13548961, 82059612, 79988739, 32896498, 2734556, 53925148,
             35978917, 9518234, 10083751, 85279542, 39033408, 48209851, 62925888, 13547194, 44035972, 68353067,
             23252163, 20073998, 42920683, 14344887, 69035996, 39391494, 27748248, 73214826, 4262748, 83688455,
             74215897, 92555899, 23911542, 58067690, 21192570, 95942114, 33191627, 8645527, 59954387, 73721763,
             72662479, 72217179, 1458481, 45455404, 34624026, 3276054, 55926364, 2538189, 92838862, 77855755, 79664441,
             18588592, 37166813, 75708455, 23108833, 11978561, 65229374, 23834131, 42579452, 87085776, 92142233,
             98169793, 31994108, 66447473, 64267057, 95676586, 45224865, 82045517, 87698900, 86760377, 6468938,
             68678099, 49484751, 68670060, 41849361, 92953423, 74130846, 22169912, 94123667, 62381496, 11404911,
             81350059, 76669555, 23659351, 33634347, 29208286, 96582765, 6997203, 91487697, 96254682, 46705288,
             69129620, 73044360, 5463828, 12133523, 84348931, 35906765, 11236700, 82799272, 92157812, 11006966,
             32345170, 58105753, 22112937, 58804673, 83537456, 28456190, 57882805, 71679588, 15849776, 39658053,
             33315038, 75077925, 25479720, 58891125, 2823227, 84225193, 32512794, 27730164, 38222742, 72791567,
             36671733, 78616435, 33672843, 59914327, 73199263, 65875307, 16347721, 76577204, 27490709, 14514199,
             15847293, 1773821, 39783827, 97216020, 18333339, 67158723, 76850157, 58675855, 90900690, 70919839, 113377,
             59366425, 60337868, 40909455, 53606930, 98131095, 76694029, 15179404, 50675006, 27368881, 520182, 85299790,
             96943869, 97761582, 26693124, 80642358, 54890399, 95580346, 94340555, 60315856, 89770242, 26489362,
             70624121, 91073195, 77758531, 54392013, 83433073, 98493102, 9092678, 33236521, 87073139, 84513597,
             54626478, 84458121, 85058138, 36273509, 9853306, 1359367, 35511764, 55182268, 73047564, 20410486, 34809483,
             22766268, 68494858, 36348909, 13237907, 79273853, 9362263, 8992441, 59389134, 22030332, 95327344, 92670308,
             53945290, 92463699, 81200910, 28036660, 27878141, 44821397, 9201186, 93844369, 88420620, 62805392,
             74846641, 6676310, 39846057, 98661632, 74657575, 47761591, 99300303, 52688395, 53648926, 64910915,
             81926714, 96106913, 34731191, 94850369, 88696471, 83544102, 42483824, 33343240, 25488064, 84005065,
             22230419, 59535838, 97743772, 81370827, 61658488, 21815186, 18535199, 59147254, 41575534, 53788561,
             15547373, 27674242, 91455784, 9157169, 30550600, 43133574, 13418312, 6037203, 80196915, 29065895, 4659159,
             94479026, 97168531, 59362807, 88976311, 15846699, 92964157, 12781669, 53647598, 66440847, 50720111,
             22628784, 31640052, 62085874, 77837256, 28441679, 95956960, 44307589, 79674139, 28702153, 6203269, 701612,
             42892555, 77880342, 26291144, 21483953, 86710609, 4087842, 51978739, 89229451, 7666475, 50934271, 17445468,
             62127947, 40721868, 4760655, 8167385, 17304056, 36720664, 58050499, 25516258, 67063506, 17490145, 37483093,
             25759943, 60064361, 44265676, 35966750, 86114542, 32627221, 8077773, 79254965, 46924497, 81249071,
             75196502, 70084709, 47409400, 55384949, 26758766, 71995043, 88903900, 95770584, 99761764, 96786456,
             9701824, 23834179, 20268187, 27292708, 6027141, 85513177, 68832164, 67260236, 13325421, 5384539, 71332033,
             59505400, 17207132, 94978827, 3304402, 70398482, 12130142, 43676345, 40512228, 51571311, 98328737,
             42037891, 17448963, 51027324, 90971680, 12624314, 32935688, 74783098, 44306234, 68359791, 78401987,
             14050977, 87587125, 70296049, 96553750, 94125049, 71889567, 39101099, 21076465, 49707787, 69937862,
             13070135, 46356024, 77162533, 5848487, 87391451, 42097414, 40039965, 47327338, 43659510, 69806991, 1155797,
             16356308, 42561888, 43697659, 76921522, 60641417, 64383955, 48877454, 51073567, 77707695, 18063186,
             70291398, 77256263, 32932323, 77011969, 45452682, 86369228, 54032650, 62353742, 45694651, 68121148,
             3902022, 33571278, 29679847, 17905659, 24776639, 97705167, 6724984, 73243675, 35665572, 14352922, 35124454,
             84844541, 70649184, 10535657, 29176348, 23268960, 57994116, 79236664, 65320138, 38084604, 26895286,
             66251930, 57102138, 90677543, 73078374, 64714177, 9756702, 54668275, 1111304, 71402264, 69026003, 10255970,
             82657264, 77615576, 57122680, 47221323, 859161, 40178651, 92789343, 739148, 16112120, 68785506, 42352675,
             86576855, 74004543, 70548491, 72751454, 54801202, 84552504, 41306769, 40521727, 67956765, 78687514,
             73819008, 33922695, 1289271, 98802406, 75954956, 49440866, 53974168, 88448415, 89882431, 12143598, 646710,
             36087820],
            238
        ]
    ]

    all_res = []
    finish = 1
    for idx in range(0, finish):
        one = tests[idx]
        # pp = func(*one)
        d = []
        for jj in range(one[0]):
            d.append((one[1][jj], one[2][jj]))
        print(d)
