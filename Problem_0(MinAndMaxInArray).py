# Find minimum and maximum element in array.

arr = input("Enter elements in array : ").split()
arr = [int(x) for x in arr]
size = len(arr)

b = len(arr) - 1
for x in range(b):
    for y in range(b-x):
        if arr[y] > arr[y+1]:
            arr[y], arr[y+1] = arr[y+1], arr[y]

print("Minimum element : ", arr[0])
print("Maximum element : ", arr[b])
