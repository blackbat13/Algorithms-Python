def bubble_sort(array: list):
    for i in range(0, len(array) - 2):
        swap = False
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j-1], array[j]
                swap = True

        if not swap:
            return


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
bubble_sort(array)
print(array)
