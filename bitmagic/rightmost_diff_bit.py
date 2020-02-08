t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    binary = bin(x^y)[2:]
    try:
        index = binary[::-1].index('1')
        print(index + 1)
    except:
        print(-1)