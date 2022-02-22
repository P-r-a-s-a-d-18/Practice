# Write a program to cyclically rotate an array by one.

arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]

for i in range(len(arr)-1):
    arr[i-1], arr[i] = arr[i], arr[i-1]

print(arr)
