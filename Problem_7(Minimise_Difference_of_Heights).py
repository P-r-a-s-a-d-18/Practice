# Minimise the maximum difference between heights [V.IMP]
# Given an array arr[] denoting heights of N towers and a
# positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only
# once. After modifying, height should be a non-negative integer. Find out the minimum possible difference of the
# height of shortest and longest towers after you have modified each tower.

def solution(arr1, h):
    avg = int((max(arr1) - min(arr1)) / 2)
    for i in range(len(arr1)):
        if arr1[i] <= avg:
            arr1[i] = arr1[i] + h
        else:
            arr1[i] = arr1[i] - h

    print(arr1)
    res = max(arr1) - min(arr1)
    return res


arr = input("Enter heights : ").split()
arr = [int(x) for x in arr]
k = int(input("Enter value for k : "))

if max(arr) - min(arr) <= k:
    print(max(arr) - min(arr))
else:
    print(solution(arr, k))
