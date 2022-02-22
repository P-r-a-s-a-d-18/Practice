# Find the Union and Intersection of the two sorted arrays.

def union(arr1, arr2):
    i = j = 0
    U = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            U.append(arr1[i])
            i = i + 1
        elif arr1[i] > arr2[j]:
            U.append(arr2[j])
            j = j + 1
        else:
            U.append(arr2[j])
            i = i + 1
            j = j + 1
    while i < len(arr1):
        U.append(arr1[i])
        i = i + 1
    while j < len(arr2):
        U.append(arr2[j])
        j = j + 1
    return U


def intersection(arr1, arr2):
    i = j = 0
    I = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i = i + 1
        elif arr1[i] > arr2[j]:
            j = j + 1
        else:
            I.append(arr2[j])
            i = i + 1
            j = j + 1
    return I


arr1 = input("Enter elements for first array : ").split()
arr1 = [int(x) for x in arr1]
arr2 = input("Enter elements for second array : ").split()
arr2 = [int(x) for x in arr2]

print(union(arr1, arr2))
print(intersection(arr1, arr2))
