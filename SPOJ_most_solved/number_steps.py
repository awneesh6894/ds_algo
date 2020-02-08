tc = int(input())
for i in range(tc):
    x,y= map(int,input().split())
    if x==y:
        if x==y==0:
            print(0)
        elif x%2==0:
            print(x+y)
        elif x%2==1:
            print(x+y-1)
    elif x-y==2:
        if x%2==0:
            print(x+y)
        elif x%2==1:
            print(x+y-1)
    else:
        print("No Number")
