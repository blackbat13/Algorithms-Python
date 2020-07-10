def stooge_sort(array: list, begin: int, end: int):
    if array[end] < array[begin]:
        array[begin], array[end] = array[end], array[begin]

    if end - begin + 1 > 2:
        t: int = (end - begin + 1) // 3
        stooge_sort(array, begin, end - t)
        stooge_sort(array, begin + t, end)
        stooge_sort(array, begin, end - t)


array: list = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
stooge_sort(array, 0, len(array) - 1)
print(array)
