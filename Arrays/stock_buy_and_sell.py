
#100 180 260 310 40 535 695
T=int(input())
for t in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    l=[]
    while i < n:
        while (i<n-1 and arr[i]>=arr[i+1]):
            i+=1
        start = i
        if (i == n-1):
            break
        while (i<n and arr[i]>=arr[i-1]):
            i+=1
        end = i-1