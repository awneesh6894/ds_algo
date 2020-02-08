#using XOR
def finder(arr1,arr2):
    result = 0
    for i in arr1+arr2:
        result ^= i
        print("xor is: "+str(result))
    print(result)

arr1=[5,7,8,9]
arr2=[5,7,9]
finder(arr1,arr2)