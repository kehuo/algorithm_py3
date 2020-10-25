
# @File: 4
# @Author: Kevin Huo
# @LastUpdate: 10/25/2020 10:23 AM
d = {"b":100,

    "a": 100,
    "c":50
}

arr = list([i, d[i]] for i in d)

arr.sort(key=lambda x: ord(x[0]), reverse=True)
print(arr)
res= max(arr, key=lambda x:x[1])
print(res)