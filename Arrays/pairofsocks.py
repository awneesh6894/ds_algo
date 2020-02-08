"""def sockMerchant(n, ar):
    ar1=set(ar)
    cout=0
    for i in ar1:
        z=(ar.count(i))
        print(i)
        if z%2==0:

            cout+=z/2
        elif z>2:
            cout+=(z-1)/2
    return int(cout)

ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9,ar))

"""
from collections import Counter
from math import ceil

N = int(input())

C = map(int, input().split(' '))

c = Counter(C)
print(c)
s = 0
for i in c:
    if c[i]>1:
        s += (c[i]/2)
print (int(s))