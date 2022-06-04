# find maximum product subarray

arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]
curr_pro = 1
max_pro = 0

for i in range(len(arr)):
    curr_pro = curr_pro * arr[i]
    if curr_pro > max_pro:
        max_pro = curr_pro
    elif curr_pro < 0:
        curr_sum = 0

print(max_pro)
