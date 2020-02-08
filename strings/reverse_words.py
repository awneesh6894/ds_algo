x=int(input())
for i in range(x):
    y=input()
    arr=y.split(".")
    print( ".".join(arr[::-1]))