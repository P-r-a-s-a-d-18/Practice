# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algorithm.

arr = input("Enter elements (only 0, 1 and 2) : ").split()
arr = [int(x) for x in arr]
arr1 = []

count_0 = 0
count_1 = 0
count_2 = 0

for i in arr:
    if i == 0:
        count_0 = count_0+1
    elif i == 1:
        count_1 = count_1+1
    else:
        count_2 = count_2+1

while count_0 !=0:
    arr1.append(0)
    count_0 = count_0-1

while count_1 != 0:
    arr1.append(1)
    count_1 = count_1-1

while count_2 != 0:
    arr1.append(2)
    count_2 = count_2-1

print(arr1)

