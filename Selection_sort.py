def selection_sort(items):
    index = 0
    sorted_list = []
    for i in range(len(items)):
        minimum = min(items)
        print(items)
        print(minimum)
        sorted_list.append(minimum)
        items.remove(minimum)
        i += 1
    return sorted_list

array_1 = [83, 4, 2, 83, 24, 2]
#print('Selection Sort: ', selection_sort(array_1))




def selection_sort_2(items):
    index = 0
#    sorted_list = []
    for i in range(len(items)): 
        minimum = min(items[index:])
        print('Index: ', index, items[index:])
        print('Minimum: ', minimum)
        min_index = items.index(minimum, index)
        items[min_index], items[index] = items[index], items[min_index]
        print(items)
        index += 1
    return items

array_2 = [83, 4, 2, 83, 24, 2]
print('Selection Sort: ', selection_sort_2(array_2))

array_2 = [83, 2, 4, 83, 24]
print('Min value: ', min(array_2[2:]), 'Min Index: ', array_2.index(4))
print("**************************************************************")


def selection_sort_3(items):
    for i in range(len(items)):
        minimum = min(items[i:])
        min_index = items.index(minimum, i)
        print('Minimum: ', minimum)      
        print("SS3: ", items[i:])  
        print('min_index: ', min_index, 'i:', i)
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
    return items

array_3 = [83, 4, 2, 83, 24, 2]
print('Selection Sort: ', selection_sort_3(array_3))