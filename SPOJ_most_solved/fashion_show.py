x=int(input())
while x>0:
    y=int(input())
    arr1=list(map(int,input().split()))
    arr2 = list(map(int, input().split()))
    sum=0
    for i in range(y):
        sum+=arr1[i]*arr2[i]
    print(sum)
    x-=1