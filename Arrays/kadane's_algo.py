def maxsum(arr,size):
    curmax = arr[0]
    gmax = arr[0]
    for i in range(1,size):
        curmax = max(arr[i],arr[i]+curmax)

        gmax = max(curmax,gmax)

    return gmax

t = int(input())
while t > 0:
    n = int(input())
    ar = list(map(int,input().split()))
    print(maxsum(ar,n))
    t=t-1

'''
1
5
1 2 3 -2 5
curmax : 3
gmax :3
curmax : 6
gmax :6
curmax : 4
gmax :6
curmax : 9
gmax :9
9

Process finished with exit code 0
'''