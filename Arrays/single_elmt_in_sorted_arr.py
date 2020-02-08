t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in a:
        x^=i
    print(x)