"""Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1"""

t=int(input())
for _ in range(t):
    x=int(input())
    arr=list(map(int,input().split()))
    for i in range(x-1):
        for j in range(i+1,x):
            if arr[j]>arr[i]:
                print(arr[j], end=" ")
                break
        else:
            print(-1, end=" ")
    print(-1)


