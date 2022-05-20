# Given a collection of numbers, find (number of or) all possible pairs that add up to a given sum.

lst = [1, 1, 1, 1]
k = 2
count = 0

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == k:
            print(lst[i], lst[j])
            count = count + 1

print("-----------------------------------")

for i in range(len(lst)):
    for j in range(len(lst) - 1, i, -1):
        if lst[i] + lst[j] == k:
            print(lst[i], lst[j])

print("-----------------------------------")

print(count)
