#Method 1: when pivot value is the first elemet of the list
def quick_sort_1(array):
    if len(array) == 0:
        return []

    pivot = array[0]
    print('pivot: ', pivot)
    rest_array = array[1:]
    left = [x for x in rest_array if x <= pivot]
    print('left: ', left)
    right = [x for x in rest_array if x > pivot]
    print('right: ', right)
    
    return quick_sort_1(left) + [pivot] + quick_sort_1(right)

array_1 = [3, 6, 8, 10, 1, 2, 1]
#array_1 = [83, 4, 2, 83, 24, 2]
print('Array 1 : ', quick_sort_1(array_1))

#Method 2: when pivot value is the last elemet of the list
def quick_sort_2(array):
    if len(array) == 0:
        return []

    pivot = array[-1]
    rest_array = array[:-1]
    left = [x for x in rest_array if x <= pivot]
    right = [x for x in rest_array if x > pivot]
    
    return quick_sort_2(left) + [pivot] + quick_sort_2(right)

array_2 = [3, 6, 8, 10, 1, 2, 1]
#array_2 = [83, 4, 2, 83, 24, 2]
print('Array 2 : ', quick_sort_2(array_2))