def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"low: {low}, high: {high}, mid: {mid}")  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

import time
start_time = time.time()
arr = []
for i in range(1, 1000001):
#    if i not in arr:
    arr.append(i)
#print(arr)
print(binary_search(arr, 66666))
print(binary_search(arr, 80099))
print("--- %s seconds ---" % (time.time() - start_time))