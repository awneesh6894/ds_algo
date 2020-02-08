'''x = int(input())
for i in range(x):
    y = int(input())
    arr=sorted(list(map(int,input().split())))
    count=0
    for j in range(y):
        k=j+1
        while k<y:
            if (arr[j]+arr[k]) in arr:
                count+=1
            k+=1
    if count==0:
        print(-1)
    else:
        print(count)''' #not optimised solution time limit exceeded
t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    my_dict = {} #create a blank dict

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            val = arr[i] + arr[j]
            if val in my_dict:
                my_dict[val] += 1 #counting number of times the sum occurred for every possible sum
            else:
                my_dict[val] = 1

    count = 0
    ''' going through each element of the array and looking into the dictionary that how many two numbers are having sum
    equal to that number of the array'''
    for i in arr:
        if i in my_dict:
            count += my_dict[i]

    if count == 0:
        print('-1')
    else:
        print(count)
    t -= 1




