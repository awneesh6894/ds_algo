#x=int(input())

lm=0
rm=0
#arr=list(map(int,input().split()))
arr1=[6,9, 9]
x=len(arr1)
for i in range(int(x/2)):
    lm=max(lm,arr1[i])
    rm=max(rm,arr1[x-i-1])
print(lm,rm)