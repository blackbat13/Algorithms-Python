def find_min(array, begin):
    min_index = begin
    for i in range(begin + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index


def selection_sort(array):
    for i in range(0, len(array)):
        min_index = find_min(array, i)
        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
selection_sort(array)
print(array)
