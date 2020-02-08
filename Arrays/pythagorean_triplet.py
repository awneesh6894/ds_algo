'''Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that
satisfies a2 + b2 = c2.

Input:
The first line contains T, denoting the number of testcases. Then follows description of testcases.
Each case begins with a single positive integer N denoting the size of array. The second line contains the
N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whether it is Pythagorean Triplet or not (without quotes).'''
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    count = 0
    for x in arr:
        for y in arr:
            if(x!=y and (x**2+y**2)**0.5 in arr):
                print('Yes')
                count = 1
                break
        if(count == 1):
            break
    if(count==0):
        print('No')