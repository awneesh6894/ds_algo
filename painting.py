tc = int(input())
for _ in range(tc):
    n,m,k = map(int,input().split())
    arr2d = [[int(j) for j in input().strip().split()] for i in range(n)]
    min_cost = 0

    print(arr2d)
    if k>n or k>m:
        print(-1)
    else:
        cost = 0
        for i in range(n):
            print("i is"+str(i))
            if i>=n-1:
                break
            else:
                for k in range(m):
                    print("k is" + str(k))
                    if k>=m-1:
                        break
                    else:
                        cost+=arr2d[i][k]
        if cost<min_cost:
            min_cost=cost
    print(min_cost)