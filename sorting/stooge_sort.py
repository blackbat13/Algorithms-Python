import math


def stooge_sort(array, begin, end):
    if array[end] < array[begin]:
        tmp = array[begin]
        array[begin] = array[end]
        array[end] = tmp

    if end - begin + 1 > 2:
        t = math.floor((end - begin + 1) / 3)
        stooge_sort(array, begin, end - t)
        stooge_sort(array, begin + t, end)
        stooge_sort(array, begin, end - t)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
stooge_sort(array, 0, len(array) - 1)
print(array)
