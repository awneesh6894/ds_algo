x = int(input())
for i in range(x):
    y,z=map(int,input().split())
    if y==z:
        print("YES")
    else:
        while y<z:
            if y==z:
                print("YES")
            y=2*y
            z=z-2





