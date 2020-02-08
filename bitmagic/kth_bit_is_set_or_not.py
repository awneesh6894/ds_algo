t=int(input())
for _ in range(t):
    y=int(input())
    z=int(input())
    x=bin(y)[2:]
    if x[-z-1]=='1':
        print("YES")
    else:
        print('NO')
