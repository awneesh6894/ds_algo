for i in range(int(input())):
    x = int(input())
    arr = list(map(int, input().split()))
    if x == 1:
        print(arr[0])
    else:
        lsum = 0
        arr_sum = sum(arr)
        for j in range(x):
            arr_sum -= arr[j]
            if lsum == arr_sum:
                print(j + 1)
                break
            lsum += arr[j]
        else:
            print(-1)

'''#optimal solution
def max(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i + 1
        left_sum += num
    return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(arr))'''
