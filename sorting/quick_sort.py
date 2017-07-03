import math


def quick_sort(array, left, right):
    if right <= left:
        return

    pivot = array[math.floor((left + right) / 2)]
    i = left
    j = right
    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i > j:
            break

        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

        i += 1
        j -= 1

    quick_sort(array, left, j)
    quick_sort(array, i, right)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
quick_sort(array, 0, len(array) - 1)
print(array)
