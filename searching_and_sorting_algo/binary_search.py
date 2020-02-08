arr=[12,15,16,36,24,54,67]

def binary_search(arr,l,r,x):
    found=False
    if r>=l:
        mid=l+(r-l)//2
        print(arr[mid])
        if arr[mid]==x:
            found=True
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    return found


print(binary_search(arr,0,len(arr)-1,15))
