arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)
z = int(n**(1/2))
#print(z)
count=0
for i in range(0,len(arr)-1,z):
    #print(i)

    if arr[i]>x:
        break
    count += z
#print("count " +str(count))
print(count-z)
for j in range((count-z)+1,n-1):
    if arr[j]==x:
        print(j)
        break
else:
    print(-1)

