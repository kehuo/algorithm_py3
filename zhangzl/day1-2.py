# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-03-24 20:59:16
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-03-24 21:28:15
line = input('input record:')
records = {}
while line:
    item = line.split('\\')[-1]
    if item in records:
        records[item] += 1
    else:
        records[item] = 1
    line = input('input record:')
record_list = sorted(records.items(), key=lambda item: item[1])
for i in range(min(len(records), 8)):
    file_name, line_number = record_list[i][0].split()
    count = record_list[i][1]
    file_name = file_name[-16:]
    print(file_name, line_number, count)
