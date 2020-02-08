T=int(input())
for t in range(T):
    x=int(input())
    arr=sorted(list(map(str,input().split())),key=len)
    y=len(arr[0])
    i=arr[0]
    count=1
    for j in arr[1::]:
        print("i is " + str(i))
        print("j is "+ str(j))
        if i in j:
            count+=1
        else:
            i=arr[0][:y-1:]
    if count==len(arr):
        print(i)
    else:
        print(-1)


