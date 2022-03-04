# Minimum number of jumps to reach end of an array
# Given an array of N integers arr[] where each element represents
# the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the
# end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

def min_jump(arr):
    count = 0
    curr_jump = 0
    max_jump = 0

    for i in range(len(arr) - 1):
        max_jump = max(max_jump, i + arr[i])

        if i == curr_jump:
            count += 1
            curr_jump = max_jump
        if arr[i] == 0 and i == curr_jump:
            return -1
    return count


arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]

print(min_jump(arr))
