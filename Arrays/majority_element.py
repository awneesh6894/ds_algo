'''t=int(input())
for _ in range(t):
    z=int(input())
    arr=list(map(int,input().split()))
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for key,value in dict.items():
        if dict[key]>z//2:
            print(key)
            break
    else:
        print(-1)'''
from collections import Counter
# best time
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    p = Counter(arr)
    flag = 0
    for elem in p:
        if p[elem] > n/2:
            flag = 1
            print(elem)
            break
    if flag == 0:
        print(-1)