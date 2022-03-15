# Merge 2 sorted arrays without using Extra space.

arr1 = input("Elements of first array : ").split()
arr1 = [int(x) for x in arr1]
arr2 = input("Elements of second array : ").split()
arr2 = [int(x) for x in arr2]

for j in range(len(arr2) - 1, -1, -1):
    last = arr1[len(arr1) - 1]
    i = len(arr1) - 2
    while i >= 0 and arr1[i] > arr2[j]:
        arr1[i + 1] = arr1[i]
        i = i - 1
    if i != len(arr1) - 2 or last > arr2[j]:
        arr1[i + 1] = arr2[j]
        arr2[j] = last

print(arr1, "\t", arr2)
print(arr1+arr2)
