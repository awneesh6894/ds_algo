x=int(input())
for i in range(x):
    y=input()
    arr=[]
    for j in y:
        if j not in arr:
            arr.append(j)
    print("".join(arr))
