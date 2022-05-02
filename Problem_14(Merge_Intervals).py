# Merge Intervals

lst = []
n = int(input("Enter the number of intervals : "))

for i in range(n):
    interval = input("Enter interval : ").split()
    lst.append(interval)

print(lst)

res = []

for i in range(n):
    for j in range(i+1, n):
        if int(lst[i][1]) >= int(lst[j][0]) >= int(lst[i][0]):
            new_interval = [lst[i][0], lst[j][1]]
            res.append(new_interval)

print(res)
