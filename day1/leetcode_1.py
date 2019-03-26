# -*- coding: UTF-8 -*-
arr=list(map(int,input('type a list here: ').split()))
line2=input('type a target number here: ')

#arr=list(map(int,line1))
#arr=int,arr)
target=int(line2)
res=[]
print(arr)
print(target)
print('len(arr) ',len(arr),'\n')

if len(arr)<2:
    print('typeError, try again.')
    exit()

for i in range(0,len(arr)):
    for j in range(1,len(arr)-1):
        if arr[i]+arr[j]==target and i!=j:
            res.append(i)
            res.append(j)
            print(res)
        else:
            print('no')
print('final res: ',res)
print('finish')
