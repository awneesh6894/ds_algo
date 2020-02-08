string = input()
count = {}
for i in string:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for key,value in count.items():
    print(key,value,sep="",end="")