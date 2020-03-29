# @File: q3
# @Author: Kevin Huo
# @LastUpdate: 3/29/2020 8:17 PM


class UndergroundSystem(object):
    """
    该题已经在leetcode 提交并通过

    https://leetcode-cn.com/contest/weekly-contest-182/problems/design-underground-system/
    涉及地铁系统
    """

    def __init__(self):
        """
        self.d = {"start_station_1": {"end_station_1": [],
                                      "end_station_2": [],
                                      "end_station_3": []
                                    },
                  "start_station_2": {"end_station_1": [],
                                      "end_station_2": []
                                    }
                }

        self.in_train = {
            45: {"start_station": "Shanghai", "check_in_time": 3},
            32: {"start_station": "Beijing", "check_in_time": 8}
        }
        """
        self.in_train = {}
        self.d = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.d:
            self.d[stationName] = {}

        self.in_train[id] = {}
        self.in_train[id]["start_station"] = stationName
        self.in_train[id]["check_in_time"] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        1 - update self.d
        2 - delete self.in_train[id]
        """
        passenger = self.in_train[id]
        start = passenger["start_station"]
        check_in_time = passenger["check_in_time"]

        if stationName not in self.d[start]:
            self.d[start][stationName] = []
        self.d[start][stationName].append(
            {"id": id, "spend_time": t - check_in_time}
        )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        array = self.d[startStation][endStation]
        avg = sum([i["spend_time"] for i in array]) / len(array)
        return avg


if __name__ == '__main__':
    s = UndergroundSystem()
    s.checkIn(45, "Leyton", 3)
    s.checkIn(32, "Paradise", 8)
    s.checkIn(27, "Leyton", 10)
    s.checkOut(45, "Waterloo", 15)
    s.checkOut(27, "Waterloo", 20)
    s.checkOut(32, "Cambridge", 22)
    avg1 = s.getAverageTime("Paradise", "Cambridge")
    print(avg1)
