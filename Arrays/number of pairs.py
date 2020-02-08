'''
Given two arrays X and Y of positive integers, 
find number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.
Input
1
3 2
2 1 6
1 5

Output
3

Explanation:
Testcase 1: The pairs which follow xy > yx are as such: 21 > 12,  25 > 52 and 61 > 16
,,,
'''
t=int(input())
for T in range(t):
    x,y=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    count=0
    for i in range(x):
        for j in range(y):
            if arr1[i]**arr2[j]>arr2[j]**arr1[i]:
                count+=1
    print(count)