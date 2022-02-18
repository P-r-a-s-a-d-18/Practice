# Given a collection of numbers, find (number of or) all possible pairs that add up to a given sum.

lst = [2, 4, 9, 8, 7, 6, 1, 3]
sum = 13
count = 0

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == sum:
            print(lst[i], lst[j])

print("\n")

for i in range(len(lst)):
    for j in range(len(lst) - 1, i, -1):
            if lst[i] + lst[j] == sum:
                print(lst[i], lst[j])
