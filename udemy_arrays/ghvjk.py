x = int(input())
leader = 0
lead = 0
for _ in range(x):
    y,z=map(int,input().split())
    if y>z:

        if y-z>lead:
            leader = 1
            lead = y-z

    else:
        if z-y>lead:
            leader=2
            lead = z-y
print(leader,lead,sep = " ")

