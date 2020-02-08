x=int(input())
for i in range(x):
    y=int(input())
    arr=list(map(int,input().split()))
    arr1=[]
    for j in range(0,len(arr),2):
        #print(j)
        if arr[j]==1:
            print("arr[j] is 1")
            arr1.append(arr[j+1])
        elif arr[j]==2:
            print(arr[j+1])
            arr1.remove(arr[j+1])
        elif arr[j]==3:
            print("arr[j] is 3")
            print(arr1[0])
