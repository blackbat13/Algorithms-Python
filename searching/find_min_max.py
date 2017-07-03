import math


def find_min_max_naive(array):
    min = array[0]
    max = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]

    return [min, max]


def find_min_max_optimal(array):
    min_candidates = []
    max_candidates = []
    for i in range(1, len(array), 2):
        if array[i - 1] < array[i]:
            min_candidates.append(array[i - 1])
            max_candidates.append(array[i])
        else:
            min_candidates.append(array[i])
            max_candidates.append(array[i - 1])

    if len(array) % 2 != 0:
        min_candidates.append(array[len(array) - 1])
        max_candidates.append(array[len(array) - 1])

    min = min_candidates[0]
    max = max_candidates[0]
    for i in range(1, len(min_candidates)):
        if min > min_candidates[i]:
            min = min_candidates[i]
        if max < max_candidates[i]:
            max = max_candidates[i]

    return [min, max]


def find_min_max_recursive(array, left, right):
    if left == right:
        return [array[left], array[left]]

    middle = math.floor((left + right) / 2)
    left_min_max = find_min_max_recursive(array, left, middle)
    right_min_max = find_min_max_recursive(array, middle + 1, right)
    min_max = [0, 0]
    if left_min_max[0] < right_min_max[0]:
        min_max[0] = left_min_max[0]
    else:
        min_max[0] = right_min_max[0]

    if left_min_max[1] > right_min_max[1]:
        min_max[1] = left_min_max[1]
    else:
        min_max[1] = right_min_max[1]

    return min_max


array = [3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11]
print('Naive algorithm')
result = find_min_max_naive(array)
print(f'Min: {result[0]}, Max: {result[1]}')

print('Optimal algorithm')
result = find_min_max_optimal(array)
print(f'Min: {result[0]}, Max: {result[1]}')

print('Recursive algorithm')
result = find_min_max_recursive(array, 0, len(array) - 1)
print(f'Min: {result[0]}, Max: {result[1]}')
