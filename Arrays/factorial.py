'''tc = int(input())
for i in range(tc):
    x= int(input())
    z=1
    while x>0:
        z*=x
        x-=1
    print(z)
x = int(input())
while x > 0:
    y, z = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(y):
        if arr[i] == z:
            print(i + 1)
            break
    else:
        print(-1)
    x -= 1'''
x=int(input())
while x>0:
    y=int(input())
    z=y//2
    if y == 1:
        print(0)
    count=0
    for i in range(1,z+1):
        if i*i<y:
            if y%i==0:
                count+=i
    print(count)
    x-=1

