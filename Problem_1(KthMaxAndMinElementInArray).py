# Find the "Kth" max and min element of an array.
# Given an array arr[] and an integer K where K is smaller than size
# of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are
# distinct.

arr = input("Enter elements in array : ").split()
arr = [int(x) for x in arr]
size = len(arr)
k = int(input("Enter k : "))

b = len(arr) - 1
for x in range(b):
    for y in range(b-x):
        if arr[y] > arr[y+1]:
            arr[y], arr[y+1] = arr[y+1], arr[y]

print(k, "th Minimum element : ", arr[k-1])
print(k, "th Maximum element : ", arr[-k])
