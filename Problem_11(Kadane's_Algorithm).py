# Kadane's Algorithm

arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]
curr_sum = 0
max_sum = 0

for i in range(len(arr)):
    curr_sum = curr_sum + arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    elif curr_sum < 0:
        curr_sum = 0

print(max_sum)
