def check(arr, s):
    for i in range(len(arr)):
        j = i
        s1 = 0
        while (j < len(arr) and s1 <= s):
            s1 = s1 + arr[j]
            if (s1 == s):
                return i + 1, j + 1
            j = j + 1

    return -1, -1


t = int(input())
for _ in range(t):
    ns = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = check(arr, ns[1])
    if (ans[0] != -1):
        print(ans[0], ans[1])
    else:
        print(-1)
