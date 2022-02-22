# Move all the negative elements to one side of the array

arr = input("Enter elements : ").split()
arr1 = []
arr2 = []

arr = [int(x) for x in arr]

for i in range(len(arr)):
    if arr[i] > 0 or arr[i] == 0:
        arr1.append(arr[i])
    elif arr[i] < 0:
        arr2.append(arr[i])

print(arr1 + arr2)
