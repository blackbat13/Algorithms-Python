def find_min(array: list, begin: int) -> int:
    min_index = begin
    for i in range(begin + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index


def selection_sort(array: list):
    for i in range(len(array)):
        min_index = find_min(array, i)
        array[i], array[min_index] = array[min_index], array[i]


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
selection_sort(array)
print(array)
