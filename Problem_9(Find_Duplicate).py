# find duplicate in an array of N+1 Integers :
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

n = int(input("Enter max element n : "))
arr = input("Enter n+1 elements : ").split()
arr = [int(x) for x in arr]

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print("Repeated element : ", arr[i])
