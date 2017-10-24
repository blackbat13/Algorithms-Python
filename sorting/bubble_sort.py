def bubble_sort(array):
    for i in range(0, len(array) - 2):
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
bubble_sort(array)
print(array)
