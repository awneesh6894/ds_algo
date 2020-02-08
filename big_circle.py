tc = int(input())
for _ in range(tc):
    x,y=map(int,input().split())
    if x==y:
        print(1)
    elif x>y:
        print(x//y)
    else:
        print(y//x)