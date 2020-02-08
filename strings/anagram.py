x = int(input())
for i in range(x):
    x, y = map(str, input().split())
    if len(x) == len(y):
        if sorted(x) == sorted(y):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
