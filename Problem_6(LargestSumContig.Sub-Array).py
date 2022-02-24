# find Largest sum contiguous Subarray [V. IMP]

arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]

res = []
ele = []

for i in range(len(arr)):
    for j in range(len(arr), i+1, -1):
        ele.append(arr[i:j])
        res.append(sum(arr[i:j]))

res = res[::-1]
ele = ele[::-1]

res.pop()
ele.pop()

m = max(res)
n = res.index(m)

print("\n", m)
print("\n", ele[n])
