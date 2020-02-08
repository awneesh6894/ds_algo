'''T=int(input())
for _ in range(T):
    z=int(input())
    arr=list(bin(z))
    i=len(arr)-1
    count=0
    while i>=2:
        count+=1
        if int(arr[i])==1:
            print(count)
            break
        i-=1'''
t=int(input())
for _ in range(t):
    n=int(input())
    binary=bin(n)[2:]
    try:
        index=binary[::-1].index('1')
        print(index+1)
    except:
        print(0)

