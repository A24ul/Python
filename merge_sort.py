def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print(f"mid: {mid}, left_side: {arr[:mid]}, right_side: {arr[mid:]}")
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
            print(f"if condition: {sorted_list}")
        else:
            sorted_list.append(right[j])
            j += 1
            print(f"else condition: {sorted_list}")

    sorted_list.extend(left[i:])
    print(f"Left Extend: {sorted_list}")
    sorted_list.extend(right[j:])
    print(f"Right Extend: {sorted_list}")
    return sorted_list

arr = [2,4,1,3,6,8,9,21,45,67,99]
print(merge_sort(arr))



#Different variables:
def merge_sort_2(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    
    merge_sort_2(left_part)
    merge_sort_2(right_part)
    
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0
    
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
    
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort_2(numbers)
    print('Sorted array: ')
    print(numbers)   