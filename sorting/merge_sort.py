import math


def merge(array, left, right, division):
    merged_length = right - left
    merged = []
    index1 = left
    index2 = division
    for i in range(0, merged_length):
        if index1 >= division:
            merged.append(array[index2])
            index2 += 1
        elif index2 >= right:
            merged.append(array[index1])
            index1 += 1
        elif array[index1] <= array[index2]:
            merged.append(array[index1])
            index1 += 1
        else:
            merged.append(array[index2])
            index2 += 1

    for i in range(0, merged_length):
        array[left + i] = merged[i]


def merge_sort(array, left, right):
    if right - left <= 1:
        return

    division = math.floor((left + right) / 2)
    merge_sort(array, left, division)
    merge_sort(array, division, right)
    merge(array, left, right, division)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
merge_sort(array, 0, len(array))
print(array)
