tc = int(input())
for _ in range(tc):
    x = input()
    dic = {}
    count=0
    for i in x:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
            count+=1
    print(count)