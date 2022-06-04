# Next Permutation

def solution(arr1):
    for i in range(len(arr1) - 1, 0, -1):
        if arr1[i - 1] < arr1[i]:
            pivot = i - 1
            swap = i
            while swap < len(arr1) - 1 and arr1[swap + 1] > arr1[pivot]:
                swap += 1
            arr1[pivot], arr1[swap] = arr1[swap], arr1[pivot]
            arr1[i:] = arr1[i:][::-1]
            return arr1
    else:
        arr1.reverse()


arr = input("Enter elements : ").split()
arr = [int(x) for x in arr]
print(solution(arr))
