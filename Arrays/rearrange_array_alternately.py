
t=int(input())
'''
for T in range(t):
    x=int(input())
    arr=list(map(int,input().split()))
    arr1 = arr[:int(x / 2) - 1:-1]
    arr2 = arr[:int(x / 2):]
    arr3=[]
    if len(arr)%2==0:
        for i in range(len(arr1)):
            arr3.append(arr1[i])
            arr3.append(arr2[i])
    else:
        for i in range(len(arr1) - 1):
            arr3.append(arr1[i])
            arr3.append(arr2[i])
        arr3.append(arr1[-1])
    for j in arr3:
        print(j,end=" ")
    print()'''
#solution
for i in range(t):
    length = int(input())
    arr = list(input().split())
    start = 0
    end = length - 1
    for j in range(length):
        if j % 2 == 0:
            print(arr[end], end=" ")
            end -= 1
        else:
            print(arr[start], end=" ")
            start += 1
    print()


