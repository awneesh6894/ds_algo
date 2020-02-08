'''#code
def leader(a,n):
    maxx=-1
    l=[]
    for i in range(n-1,-1,-1):
        if a[i]>=maxx:
            maxx=a[i]
            l.append(maxx)
    length=len(l)
    for i in range(length-1,-1,-1):
        print(l[i],end=' ')
    print()
t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    leader(arr,n)'''
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
for j in arr[::-1]:
    print(j)