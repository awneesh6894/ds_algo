# Python program for implementation of Selection
# Sort
import sys

'''A = [23, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            print(A)

            # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]'''


arr=[12,14,11,7,34,56]
for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j

    arr[i],arr[min_idx]=arr[min_idx],arr[i]
print(arr)




'''# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i])'''